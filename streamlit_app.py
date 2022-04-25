from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np


with st.echo(code_location='below'):

    #Clinical slider parameters
    g0 = st.slider("Rate of nutrient consumption", 1, 500, (20-100))
    g1 = st.slider("Nutrient supply degradation (ext. inhibitor)", 1, 10, 1-5)
    g2 = st.slider("External inhibitor degradation", 1, 10, 1-5)
    g3 = st.slider("Inhibitor generation by tumor", 1, 10, 1-5)
    g4 = st.slider("Inhibitor degradation by tumor", 1, 10, 1-5)
    g5 = st.slider("Rate of NP binding", 1, 10, 1-5)
    g6 = st.slider("Rate of NP degradation", 1, 10, 1-5)

    c1 = st.slider("Auger effect", 1, 10, 1-5)
    c2 = st.slider("Radiotherapy effect", 1, 10, 1-5)

    #Mathematical proportionality components
    s = 100
    ae = 0.2
    Phi_i = 1
    Phi_n = 0.6
    n_i = 1


    Point = namedtuple('Point', 'x y')
    data = []

    #Create drop down menu to select variables 
    options = st.multiselect(
     'Which variables would you like to select?',
     ['Rate of nutrient consumption', 'Nutrient supply degradation (ext. inhibitor)', 'External inhibitor degradation', 'Inhibitor generation by tumor'],
     ['Rate of NP binding', 'Rate of NP degradation'])

    #Limit to three variables 
    if options :
        if len(options) <= 3:
            st.write(options)
        else:
            st.warning("Please only select three variables")

    st.write('You selected:', options)
    
    def TumorModel(dRp, Rp, c1, g5, g6, s, g1, Phi_i, Phi_n, ae, n_i, c2):
        dRp = (Rp/3)[[(c1(g5+g6)-s*g1)/15][Rp*Rp]+(s*Phi_i)-(s*Phi_n)-[(s*2*ae)/Rp]-c1(n_i)-c2]
        return dRp

        """    for dRp in range(g0):
        TumorModel()
        x = dRp
        y = [VarSelector1]
        z = [VarSelector2]"""

    import plotly.graph_objects as go
    import plotly.figure_factory as ff
    
    fig = go.Figure(data=[go.surface(x = dRp, y = [VarSelector1], z = [VarSelector2])])
    st.plotly_chart

    """for curr_point_num in range(g0):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))
"""
    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
