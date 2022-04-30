import altair as alt
import math
from nbformat import write
import pandas as pd
import streamlit as st
import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt





with st.sidebar:
    
    """ #Clinical slider parameters
    g0 = st.slider("Rate of nutrient consumption", 1, 500, (20,100))
    g1 = st.slider("Nutrient supply degradation (ext. inhibitor)", 1, 10, (1,5))
    g2 = st.slider("External inhibitor degradation", 1, 10, (1,5))
    g3 = st.slider("Inhibitor generation by tumor", 1, 10, (1,5))
    g4 = st.slider("Inhibitor degradation by tumor", 1, 10, (1,5))
    g5 = st.slider("Rate of NP binding", 1, 10, (1,5))
    g6 = st.slider("Rate of NP degradation", 1, 10, (1,5))
    """

    g0 = st.slider("Rate of nutrient consumption", 1, 500)
    g1 = st.slider("Nutrient supply degradation (ext. inhibitor)", 1, 10)
    g2 = st.slider("External inhibitor degradation", 1, 10)
    g3 = st.slider("Inhibitor generation by tumor", 1, 10)
    g4 = st.slider("Inhibitor degradation by tumor", 1, 10)
    g5 = st.slider("Rate of NP binding", 1, 10)
    g6 = st.slider("Rate of NP degradation", 1, 10)
    

    c1 = st.slider("Auger effect", 1, 10)
    c2 = st.slider("Radiotherapy effect", 1, 10)

    #Mathematical proportionality components
    s = 100
    ae = 0.2
    Phi_i = 1 
    Phi_n = 0.6
    n_i = 1
    Rp = 1

def model(Rp, var1, var2):
    s = 100
    ae = 0.2
    Phi_i = 1 
    Phi_n = 0.6
    n_i = 1
    Rp = 1
    dRp = (Rp/3)*(((
        c1
    *(g5+g6)-s*g1)*(0.0666666))*(Rp*Rp)+(s*Phi_i)-(s*Phi_n)-((s*2*ae)/Rp)-c1*(n_i)-c2)
    return dRp

    #Create drop down menu to select variables 
options = st.multiselect(
        'Which variables would you like to select?',
        ['g5', 'g6', 'c1', 'c2'])
st.write(options[0])
if options :
        if len(options) > 2:
            st.warning("Too many variables")
        elif len(options) < 2:
            st.warning("Too few variables")
            #list_options = []
            #list_options.append(options)
        #st.write('You selected:', options)
        else:
            var1 = options[0]
            var2 = options[1]
            model(Rp, var1, var2)


        
"""    Rp0 = [0,50,100]
    t = np.linspace(0,20,200)
    result = odeint(model, Rp0, t, args=(var2,))

    fig,ax = plt.subplots()
    ax.plot(t,result[:,0],label='R0=0')
    ax.plot(t,result[:,1],label='R0=0.3')
    ax.plot(t,result[:,2],label='R0=1')
    
    
    def TumorModel(Rp, c1, g5, g6, s, g1, Phi_i, Phi_n, ae, n_i, c2):
            dRp = (Rp/3)[[(c1(g5+g6)-s*g1)/15][Rp*Rp]+(s*Phi_i)-(s*Phi_n)-[(s*2*ae)/Rp]-c1(n_i)-c2]
            return dRp
    
    TumorModel(10, c1, g5, g6, s, g1, Phi_i, Phi_n, ae, n_i, c2)"""
