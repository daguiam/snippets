# Translates a dictionary to an object
class dict2obj():
    def __init__(self,d):
        self.__dict__ = d
        
        
# Finds the index of the array element nearest to the provided value
def get_arrayValueIdx(array,value):
    return (np.abs(array-value)).argmin();

# Implemented smooth moving average algorithm
def smooth(data,N=5):
    return np.convolve(data,np.ones(N)/N,'same');

# Implemented weighted moving average 
def smoothweighted(data,weights,N=5):
    datalen = len(data)
    lowhalf = int(N/2);
    upperhalf = (N-lowhalf);
    out = np.array([]);
    for i in range(0,datalen):
        startidx = i;
        endidx = startidx +N;
        if i <lowhalf:
            print 'lower than'
            startidx = 0;
            endidx = i-lowhalf+N;
        if i > datalen- upperhalf:
            print ' upper than'
            startidx = i;
            endidx = datalen;        
        print i, startidx,endidx, N, lowhalf,datalen-upperhalf
        value = np.average(data[startidx:endidx],weights=weights[startidx:endidx]);
        out=np.append(out,value);

    
    return out;
        
        
        
        
        
# Computes the spectrogram of a broadband reflectometry signal using a sliding window short-time fourier transform
# Adapted to python from ref_stft() by CFN-IST Portugal
def calc_stft(x,y,Fs=1,window=128,padding=4096,step=10,windowtype=1):
        

        Fs = Fs;
        freqramp = x
        signal = y;
        n = len(signal);
        nf = len(freqramp)
        N = padding;
                
        # Produces the wanted window
        def get_fft_window_type(window=128,windowtype=1):
    
            if (windowtype==1):
                WIN = np.ones(window);
            elif (windowtype==2):
                WIN = np.hamming(window);
            elif (windowtype==3):
                WIN = np.hanning(window);
            elif (windowtype==4):
                WIN = np.blackman(window);
        
            return WIN;
        
        WIN = get_fft_window_type(window,windowtype);

        if window < step:
            step = window

        if step==0:
            stft_x = int(math.floor(n/window));
            step=window;
        else:
            stft_x = int(math.floor( (n-window)/step) +1);
            
        #stft_x,step = calc_stftStep(window,step,n)

        stft_y = padding
        stft = np.zeros( ( stft_y,stft_x ));

        halfwin = window/2;
        pfindex = np.array([],dtype='int');
        fmax = Fs
        fb = np.linspace(0,fmax,stft_y);
        win_i = 0;
        # Calculates the fft in each window
        for i in range(0,stft_x):
            win_i =  i*step;
            win_f = win_i+window;
            sigwindow =  signal[win_i:win_f];
            len_sig = len(sigwindow);
            if len_sig < window:
                auxwindow = get_fft_window_type(len_sig,windowtype);
                sigwindow = auxwindow * sigwindow;
            else:
                sigwindow = WIN * sigwindow;

            stft[:,i]=np.abs(np.fft.fft(sigwindow,padding))[0:stft_y];

            # Each probing frequency bin is at the middle of the FFT window
            pfindex = np.append(pfindex,win_i+halfwin);
        pf = freqramp[pfindex];

        # FFT shift
        for i in range(0,len(pf)):
            stft[:,i]=np.fft.fftshift(stft[:,i]);
        fb = fb-max(fb)/2;
        
        # Outputs
        stft = stft;
        pf = pf;
        fb = fb;

        return pf,fb,stft

