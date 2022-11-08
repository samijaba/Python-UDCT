import numpy as np



def udctmddec(im, param_udct, udctwin):
    imf=np.fft.fftn(im)
    fband=0*imf

    fband [udctwin[1,1,:1]]=imf [np.matmul(udctwin[1,1,:1],udctwin[1,1,:2])]
    cband = np.fft.fftn(fband)
    coef[1,1]=downsamp(cband,2**(param_udct.res-1)*np.ones(1,param_udct.dim))
    coef[1,1]=np.sqrt()

