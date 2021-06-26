import numpy as np

def start_setup(N, param):
    """
    Generuj układ początkowy sieci kwadratowej.
    N: rozmiar sieci
    param: typ układu
    """
    if param == "order up":
        return np.ones([N,N], dtype=int)
    
    if param == "order down":
        return -1*np.ones([N,N],dtype=int)
    
    if param == "mess":
        LL =np.ones(shape= (N,N), dtype=int) 
        for i in range(N):
            for j in range(N):
                LL[i,j] = np.random.choice([-1,1], p= [0.5, 0.5]) #generuj 1, -1 z prawdopodobieństwem 1/2
        return LL 
    
    if param == "vertical stripes":
        L_1 = np.ones([N,int(N/2)], dtype=int)
        L_2 = -1*np.ones([N, int(N/2)], dtype=int)
        return np.concatenate((L_1,L_2) , axis=1)
    
    if param == "horizontal stripes":
        L_1 = np.ones([int(N/2),N], dtype=int)
        L_2 = -1*np.ones([int(N/2),N], dtype=int)
        return np.concatenate((L_1,L_2) , axis=0)
    
    if param == "circle":
        LL = np.ones([N,N], dtype=int)
        for i, x in  zip(range(N),range(-N//2+1, N//2+1) ):
            for j,y in zip(range(N), range(-N//2+1, N//2+1)): 
                if x**2 +y **2 < (3/8*N)**2:
                    LL[i,j] = -1
        return LL
    
    if param=="square":
        LL = np.ones([N,N], dtype=int)
        for i in range(N):
            for j in range(N): 
                if  N/4<i < 3/4*N  and N/4<j< 3/4*N :
                    LL[i,j] = -1
        return LL
    
    if param == "chessboard":       
        LL = np.ones([N,N],dtype=int)
        step = N//9 #5,7,9,11,13,15, 17,19,21,23,25
        l = [[i,j] for i,j in zip(range(0,N,step), range(step,N+step,step))]
        h = [l[i] for i in range(len(l)) if i%2]
        for i in range(N):
            for j in range(N): 
                    for el in  h :
                        if el[0]<i<el[1] or el[0]<j<el[1]:
                            LL[i,j] = -1                   
        return LL
    
    if param== "diagonal stripes":
        LL =  np.ones([N,N], dtype=int)
        for i in range(N):
            for j in range(N):
                if  j-25<i <j +25 or j-125<i<j-75 or j+75<i<j+125:
                    LL[i,j] = -1
        return LL