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
        
        
        
