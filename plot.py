import streamlit as st
import pandas as pd
import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import plotly.figure_factory as ff
df1 = pd.DataFrame(np.random.randn(6, 4), columns=['A', 'B', 'C', 'D'])
# st.line_chart(df1)
# st.bar_chart(df1)
# st.area_chart(df1)
plt.scatter(df1['A'],df1['B'])
chart =alt.Chart(df1).mark_circle().encode(

   x='A' ,y='B',tooltip = ['A','B']
)
st.altair_chart(chart,use_container_width=True)

#we can create flowchart
st.graphviz_chart('''
    digraph {
        run -> intr
        intr -> runbl
        runbl -> run
        run -> kernel
       
    }
''')

#we can plot plotly chart



# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)

import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)


import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))