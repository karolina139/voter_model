from start_setup import start_setup
from voter_model import model
import streamlit as st

def gui():
	st.set_page_config(layout="wide", initial_sidebar_state="auto")
	st.write('# Q-voter model')

	st.sidebar.markdown("## Select type of model and parameters")
	select_event = st.sidebar.selectbox('Which model do you want to chose?',
																			['conformity + independence', 'conformity + nonconformism'])

	start_grid = ['order up', 'order down', 'mess' , 'vertical stripes', 'horizontal stripes', 'circle', 'square', 'chessboard']

	if select_event == 'conformity + independence':
		MA = st.sidebar.slider("Choose size of N square grid", 10 ,200, step = 10)
		pA = st.sidebar.slider("Choose nonconformism propability p", min_value =0.0 ,max_value=1.0, step=0.05)
		fA = st.sidebar.slider("Choose f",  min_value =0.0 ,max_value=1.0, step=0.05)
		MCSA = st.sidebar.number_input('Choose MCS', value=100, step=1)
		start_setupA = st.sidebar.selectbox('How to set up start grid', start_grid)
		qA = st.sidebar.slider("Choose number of neighbours", 0,10)
		random_qA = st.sidebar.selectbox('How to choose neighbours?', 
			['with repetition', 'without repetition'])
		framesA = st.sidebar.slider("Choose frames per iteartion", 1,20)
	else:
		MB= st.sidebar.slider("Choose size N of square grid ", 10 ,200, step =10)
		pB = st.sidebar.slider("Choose p",  min_value =0.0 ,max_value=1.0, step=0.05)
		MCSB = st.sidebar.number_input('Choose MCS', value=100, step=1)
		start_setupB= st.sidebar.selectbox('How to set up start grid', start_grid)
		qB = st.sidebar.slider("Choose number of neighbours", 0,10)
		random_qB = st.sidebar.selectbox('How to choose neighbours?', 
		['with repetition', 'without repetition'])
		framesB= st.sidebar.slider("Choose frames per iteartion", 1,20)


	


	set_start = st.button('Set')
	button_start = st.button('Animation')
	

	if set_start:
		if select_event == 'conformity + independence':
			#try:		
			LLA = start_setup(MA, start_setupA)
			st.write(model(0,LLA,qA,pA,fA,random_qA,  'model_a', framesA))

			#except:
			#	st.write("Choose right parameters")

		if select_event == 'conformity + nonconformism':
			#try:		
			LLB = start_setup(MB, start_setupB)
			st.write(model(0,LLB,qB,pB, 0 ,random_qB,  'model_b', framesB))
			#except:
			#	st.write("Choose right parameters")


	if button_start:
		if select_event == 'conformity + independence':
			#try:		
			LLA = start_setup(MA, start_setupA)
			st.write(model(MCSA,LLA,qA,pA,fA,random_qA,  'model_a', framesA))

			#except:
			#	st.write("Choose right parameters")

		if select_event == 'conformity + nonconformism':
			#try:		
			LLB = start_setup(MB, start_setupB)
			st.write(model(MCSB,LLB,qB,pB, 0 ,random_qB,  'model_b', framesB))
			#except:
			#	st.write("Choose right parameters")
