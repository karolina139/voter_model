import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable
import streamlit as st
from mpl_toolkits.axes_grid1 import make_axes_locatable
plt.style.context('ggplot')
from matplotlib import cm
from matplotlib.collections import LineCollection
import plotly.graph_objects as go
import plotly.express as px


def model(M,LL,q,p,f,option, model_type, klatki):
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
		modulo = klatki
		values = np.zeros([M])

		placeholder = st.empty()
		ploting(np.sum(np.copy(LL))/Nn,np.copy(LL), -1,placeholder)

		for k in range(M):
 

				for _ in range(1,N**2): # jeden krok Monte Carlo
				
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


				values[k] = np.sum(np.copy(LL)) /Nn
				if k%modulo ==0 :
						ploting(values,np.copy(LL), k,placeholder)

		return       

def ploting(values,LL,k, placeholder):

		# #PLOT HEATMAP
		N = len(LL[0:])
		fig2 = go.Figure(data=go.Heatmap(z=LL, zmin=-1, zmax=1))

		if k==-1:
			fig2.update_layout(title = 'State of the system, MCS = {}'.format(0), margin=dict(l=10, r=0, t=50, b=0), font=dict(size=20))
		else:
			fig2.update_layout(title = 'State of the system, MCS = {}'.format(k+1), margin=dict(l=10, r=0, t=50, b=0), font=dict(size=20))

		fig2.layout.height = 510
		fig2.layout.width = 550
		
		if k==-1:
			print(values,LL)
			fig = go.Figure()
			fig.add_trace(go.Scatter(	
						x=[0], 
						y=[values]))
		else:
			fig = go.Figure()
			fig.add_trace(go.Scatter(	
						x=np.arange(k), 
						y=values[:k],
	                    mode='lines',
	                    name='lines'))

					
		fig.update_layout(title='Opinion',
                   xaxis_title='t[MCS]',
                   yaxis_title='Average',
                   width=800,
                   margin=dict(l=10, r=100, t=50, b=0),
                   font=dict(size=20))


		fig.update_yaxes(range=[-1.1, 1.1])

		#insert plots to app
		col1, col2 = placeholder.beta_columns(2)
		col2.write(fig)
		col1.write(fig2)    
	






