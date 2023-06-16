# %%
import pandas as pd
import numpy as np
import streamlit as st

# %%
#read csv
df = pd.read_csv('./Sangrur/result.csv')
df.head()
#show all columns
pd.set_option('display.max_columns', None)
df.head()
df_a = pd.read_csv('./Sangrur/result2.csv')
#show features
df2tempa = df[['features__attributes__objectid', 'features__attributes__schcd',
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
df2tempb = df_a[['features__attributes__objectid', 'features__attributes__schcd',
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
df2temp = pd.concat([df2tempa, df2tempb]).drop_duplicates()
#merge both df without 
# %%
# filter out district with name sangrur
# df2 = df2[df2['features__attributes__dtname'] == 'Sangrur']
# df2['LAT'] = df2['features__attributes__latitude']
# df2['LON'] = df2['features__attributes__longitude']
# df2

# %%
def filter_district(df, district):
    df = df[df['features__attributes__dtname'] == district]
    df['LAT'] = df['features__attributes__latitude']
    df['LON'] = df['features__attributes__longitude']
    return df

def filter_school_type(df, school_type):
    df = df[df['features__attributes__school_typ'] == school_type]
    df['LAT'] = df['features__attributes__latitude']
    df['LON'] = df['features__attributes__longitude']
    return df

# %%
# #use streamlit to show data
# st.title('Schools in Sangrur')
# st.write(df2)
# #show map of sangrur
# st.map(df2)
# map_type = st.selectbox('Select map type', ['stamen', 'carto', 'openstreetmap', 'esri', 'stamenterrain', 'stamentoner', 'stamenwatercolor', 'stamenterrain'])
# st.map(df2[['LAT', 'LON']], zoom=10, use_container_width=True, height=500, tooltip=df2['features__attributes__schname'], map_type=map_type)
# #show map of sangrur with markers and zoom

#show other details of the school when clicked on marker
#use folium to show map
import folium
from streamlit_folium import folium_static
#put bcg logo on top of the site
from PIL import Image
image = Image.open('./logo.png')

#create columns

#add a pill with text 
# st.markdown("<h4 style='text-align: left; color: black;'>School GIS Mapping</h4>", unsafe_allow_html=True)
#add bcg logo on top of the sidebar
image = Image.open('./logo.png')
st.image(image, width=100)
#add a footer with texts
st.sidebar.markdown("<h4 style='text-align: left; color: black;'>Developed by: BCG Social Impact</h4>", unsafe_allow_html=True)


def school_maps():
#add columns
    col1, col2 = st.columns([1, 1])

    district = col1.selectbox('Select District', df2temp['features__attributes__dtname'].unique())
    df2 = filter_district(df2temp, district)

    #select school type and have all as an option
    school_type = col2.selectbox('Select School Type', df2['features__attributes__school_typ'].unique())
    df2 = filter_school_type(df2, school_type)

    #add a button to reset the filters
    if st.button('Reset Filters'):
        df2 = df2temp
        df2['LAT'] = df2['features__attributes__latitude']
        df2['LON'] = df2['features__attributes__longitude']

    m = folium.Map(location=[df2['LAT'].mean(), df2['LON'].mean()], zoom_start=10)
    #let the map cover the whole screen
    folium.TileLayer('cartodbpositron').add_to(m)

    for i in range(0,len(df2)):
        mypopup = "School Name:{} \n Type:{} \n Management:{} \n Location:{} \n Pincode:{}".format(df2.iloc[i]['features__attributes__schname'], df2.iloc[i]['features__attributes__school_typ'], df2.iloc[i]['features__attributes__management'], df2.iloc[i]['features__attributes__sdtname'], df2.iloc[i]['features__attributes__pincode'])
        html = '''
        <h3>School Name:{}</h3>
        <p>Type:{}</p>
        <p>Management:{}</p>
        <p>Location:{}</p>
        <p>Pincode:{}</p>
        '''.format(df2.iloc[i]['features__attributes__schname'], df2.iloc[i]['features__attributes__school_typ'], df2.iloc[i]['features__attributes__management'], df2.iloc[i]['features__attributes__sdtname'], df2.iloc[i]['features__attributes__pincode'])
        iframe = folium.IFrame(html=html, width=200, height=200)
        folium.Marker(
            location=[df2.iloc[i]['LAT'], df2.iloc[i]['LON']],
            popup=folium.Popup(iframe, max_width=200),
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(m)
    folium_static(m)

page_to_show = {
    "School Maps": school_maps,
}
name_page = st.sidebar.selectbox("Go to", page_to_show.keys())
page_to_show[name_page]()




# %%
#run streamlit
#streamlit run Mapping.py



