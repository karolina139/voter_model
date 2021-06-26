import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable
import streamlit as st
from mpl_toolkits.axes_grid1 import make_axes_locatable
plt.style.context('ggplot')
from matplotlib import cm
from matplotlib.collections import LineCollection


def model(M,LL,q,p,f,option, model_type):
		"""
		Model q-wyborcy:konformizm + niezależność
		M: liczba kroków Monte Carlo,
		LL: tablica początkowa
		q: roamiar grupy wpływu
		p: prawdopodobieństwo nonkonformizmu
		f: prawdopowodbieństow niezależności/ tylko do modelu konformizm + niezależność
		option: parametr wyboru typu losowania q-sąsiadów (z powtórzeniami lub bez)
		model_type: konformizm + niezależność || konformizm + antykonformizm
		"""
		
		N = len(LL[0:])
		Nn = N**2
		modulo = max(200//N,1)
		values = np.zeros([M])

		placeholder = st.empty()
		ploting(np.array([0,0]),LL, 0,placeholder)

		for k in range(M):
 

				for _ in range(N**2): # jeden krok Monte Carlo
				
						i, j = np.random.randint(0,N-1), np.random.randint(0,N-1) # losuj osobę z sieci

						neighbours =  np.array([LL[(i-1)%N,j], LL[i, (j+1)%N], LL[(i+1)%N, j], LL[i, (j-1)%N]])

						#rozszerzona opcja sąsiadów
						# neighbours = np.array([LL[(i-1)%N,j], LL[i, (j+1)%N], LL[(i+1)%N, j], LL[i, '(j-1)%N], LL[(i-1)%N, (j-1)%N], LL[(i+1)%N, (j+1)%N], LL[(i-1)%N, (j+1)%N], LL[(i+i)%N,(j-1)%N]])

						if option=="with repetition":
								neighbours_choosed = np.random.choice(neighbours,size =q, replace=True)
						if option=="without repetition":
								neighbours_choosed = np.random.choice(neighbours,size =min(q, len(neighbours)), replace=False)

						if np.random.uniform(0,1) < p :
								
								#MODEL A
								if model_type=="model_a" and np.random.uniform(0,1)  < f:  #independence            
										LL[i,j] = -1*LL[i,j]

								#MODEL B
								if model_type=="model_b": #antykonformizm

										if np.count_nonzero(neighbours_choosed ==1)== len(neighbours_choosed):
												LL[i,j]=-1
										if np.count_nonzero(neighbours_choosed ==-1) == len(neighbours_choosed):
												LL[i,j]=1

						else: #konformizm, czesc wspolna dla obu modeli

								if np.count_nonzero(neighbours_choosed ==1) == len(neighbours_choosed):
										LL[i,j]=1
								if np.count_nonzero(neighbours_choosed ==-1) == len(neighbours_choosed):
										LL[i,j]=-1


				values[k] = np.sum(LL==1) /Nn
				if k%modulo ==0 :
						ploting(values,LL, k,placeholder)

		return       

def ploting(values,LL,k, placeholder):

		#PLOT HEATMAP
		fig2 = plt.figure()
		ax = plt.gca()
		img = ax.imshow(LL, interpolation= 'None', cmap= 'viridis', vmin=-1, vmax = 1)
		divider = make_axes_locatable(ax)
		cax = divider.append_axes('right', size='5%', pad=0.2)
		fig2.colorbar(img, cax=cax)
		ax.set_title('State of the system, MCS = {}'.format(k+1), fontsize=25, pad=20)
		ax.set_xlabel("fill", color= 'w',fontsize = 19)


		##PLOT TRAJECTORY
		fig, axs= plt.subplots()

		points = np.array([np.arange(k),  values[:k]]).T.reshape(-1, 1, 2)
		segments = np.concatenate([points[:-1], points[1:]], axis=1)
	
		# Create a continuous norm to map from data points to colors
		norm = plt.Normalize(0,1)
		lc = LineCollection(segments, cmap='viridis', norm=norm)
		# Set the values used for colormapping
		lc.set_array(values[:k])
		lc.set_linewidth(2)
		line = axs.add_collection(lc)
		fig.colorbar(line, ax=axs)


		plt.xlim(0, k+1)
		plt.ylim(-0.1, 1.1)
		plt.title("Trajectory", fontsize=25, pad=20)
		plt.xlabel("t[MCS]", fontsize=20)
		plt.ylabel("c",  fontsize=20)
		plt.xticks([0, k//6 , 2*k//6, 3*k//6, 4*k//6, 5*k//6, k], fontsize=15)
		plt.yticks(fontsize=15)
	

		#insert plots to app
		col1, col2 = placeholder.beta_columns(2)
		col2.pyplot(fig)
		col1.pyplot(fig2)    
	
	
		plt.clf() 





