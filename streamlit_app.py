from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px



with st.sidebar:

    #Clinical slider parameters
        g0 = st.slider("Rate of nutrient consumption", 1, 500, (20,100))
        g1 = st.slider("Nutrient supply degradation (ext. inhibitor)", 1, 10, (1,5))
        g2 = st.slider("External inhibitor degradation", 1, 10, (1,5))
        g3 = st.slider("Inhibitor generation by tumor", 1, 10, (1,5))
        g4 = st.slider("Inhibitor degradation by tumor", 1, 10, (1,5))
        g5 = st.slider("Rate of NP binding", 1, 10, (1,5))
        g6 = st.slider("Rate of NP degradation", 1, 10, (1,5))

        c1 = st.slider("Auger effect", 1, 10, (1,5))
        c2 = st.slider("Radiotherapy effect", 1, 10, (1,5))

    #Mathematical proportionality components
        s = 100
        ae = 0.2
        Phi_i = 1
        Phi_n = 0.6
        n_i = 1
        

with st.echo(code_location='below'):

    #Create drop down menu to select variables 
    options = st.multiselect(
        'Which variables would you like to select?',
        ['g0', 'g1', 'g2', 'g3'])
    if options :
        if len(options) <= 2:
            st.write()
            #list_options = []
            #list_options.append(options)
        #st.write('You selected:', options)
        else:
            st.warning("Please only select two variables")

    #Establishing user's first and second variables, to be used in 3D scatter plot
    var1 = options[0]
    var2 = options[1]

    def TumorModel(dRp, Rp, c1, g5, g6, s, g1, Phi_i, Phi_n, ae, n_i, c2):
        dRp = (Rp/3)[[(c1(g5+g6)-s*g1)/15][Rp*Rp]+(s*Phi_i)-(s*Phi_n)-[(s*2*ae)/Rp]-c1(n_i)-c2]
        return dRp


    fig = px.scatter_3d(x=g6, y=var1, z=var2, color="black", size="300", hover_name="dRp",
                  symbol="sphere", color_discrete_map = {"dRp": "teal", "var2": "pink", "var3":"orange"})
    st.write(fig)
    print(fig)

