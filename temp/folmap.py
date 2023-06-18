# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# %%
#read csv
df = pd.read_csv('./Sangrur/result.csv')
df.head()
#show all columns
pd.set_option('display.max_columns', None)
df.head()
#show features
print(df.columns)
df2 = df[['features__attributes__objectid', 'features__attributes__schcd',
       'features__attributes__schname', 'features__attributes__schcat',
       'features__attributes__school_cat', 'features__attributes__schtype',
       'features__attributes__school_typ', 'features__attributes__schmgt',
       'features__attributes__management', 'features__attributes__rururb',
       'features__attributes__location', 'features__attributes__pincode',
       'features__attributes__dtname', 'features__attributes__udise_stco',
       'features__attributes__stname', 'features__attributes__vilname',
       'features__attributes__longitude', 'features__attributes__latitude',
       'features__attributes__stcode11', 'features__attributes__dtcode11',
       'features__attributes__sdtcode11', 'features__attributes__sdtname',
       'features__geometry__x', 'features__geometry__y']]

# %%
df2
# filter out district with name sangrur
df2 = df2[df2['features__attributes__dtname'] == 'Sangrur']
df2['LAT'] = df2['features__attributes__latitude']
df2['LON'] = df2['features__attributes__longitude']

# %%
# #use streamlit to show data
# st.title('Schools in Sangrur')
# st.write(df2)
# #show map of sangrur
# st.map(df2)
# map_type = st.selectbox('Select map type', ['stamen', 'carto', 'openstreetmap', 'esri', 'stamenterrain', 'stamentoner', 'stamenwatercolor', 'stamenterrain'])
# st.map(df2[['LAT', 'LON']], zoom=10, use_container_width=True, height=500, tooltip=df2['features__attributes__schname'], map_type=map_type)
# #show map of sangrur with markers and zoom

#use folium to show map
import folium
from streamlit_folium import folium_static
m = folium.Map(location=[df2['LAT'].mean(), df2['LON'].mean()], zoom_start=10)
for i in range(0,len(df2)):
    folium.Marker(
        location=[df2.iloc[i]['LAT'], df2.iloc[i]['LON']],
        popup=df2.iloc[i]['features__attributes__schname'],
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)
folium_static(m)

#run streamlit app



# %%
#run streamlit
#streamlit run Mapping.py



