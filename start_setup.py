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
    
    if param == "random":
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
        center = N//2-0.5
        r = 2*N//5
        for i in range(N):
            for j in range(N):
                if (i-center)**2 +(j-center)**2 < r**2:
                    LL[i,j] = -1
        return LL
    
    if param=="square":
        LL = np.ones([N,N], dtype=int)
        for i in range(N):
            for j in range(N): 
                if  2* N/10  <= i < 8*N /10  and  2*N/10 <=j< 8*N/10 :
                    LL[i,j] = -1
        return LL
    
    if param == "chessboard":             
        LL = np.zeros([N,N],dtype=int)
        cell_size = N // 10 
        for i in range(N):
            for j in range(N):
                
                if (i // cell_size + j // cell_size) % 2 == 1:
                    LL[i, j] = 1 
                else:
                    LL[i, j] = -1 
        return LL
