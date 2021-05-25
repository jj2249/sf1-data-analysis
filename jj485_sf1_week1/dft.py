def dft(xt):

    # extract data length, N
    N = xt.size
    axis = np.arange(N)
    
    # build a fourier matrix by multiplying appropriate matricies
    k,l = np.meshgrid(axis, axis)
    F = np.matmul(l, k) / N
    
    # raise complex exponential to powers in F
    w = np.exp(-2*np.pi*1j/N)
    W = np.power(w, F)
    
    # simple matrix multiplication to extract dft
    Xw = np.matmul(W, xt)
    
    return Xw