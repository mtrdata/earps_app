import streamlit as st

# Set the page config to wide layout
st.set_page_config(layout="wide")

# Import Google Font
google_fonts_link = "<link href='https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap' rel='stylesheet'>"

# Inject the Google Fonts link into the Streamlit app
st.markdown(google_fonts_link, unsafe_allow_html=True)

# CSS for custom styling
custom_css = """
<style>
    body {
        font-family: 'Inter', sans-serif;
    }
    .big-font {
        font-size: 24px !important;
        color: #89dda5;
        text-align: center;
        font-weight: bold;
    }
    .big-font-2 {
        font-size: 24px !important;
        color: #89dde5;
        text-align: center;
        font-weight: bold;
    }
    .metric {
        font-size:40px !important;
        color: #FFF;
        text-align: center;
        font-weight: normal;
    }
    div.stSelectbox > div {
    text-align: center;
    font-size: 18px;
}
</style>
"""

# Inject custom CSS with st.markdown
st.markdown(custom_css, unsafe_allow_html=True)

#######################
# Page Set Up
#######################

about_page = st.Page(
    'pages/about.py',
    title='About Ratings & Application',
    icon=':material/info:',
    default=True,
)
database_page = st.Page(
    'pages/database.py',
    title='Goalkeeper Database',
    icon=':material/database:',
)
comparison_page = st.Page(
    'pages/head_to_head.py',
    title='Player Comparison Tool',
    icon=':material/search:',
)
top_10 = st.Page(
    'pages/top_10.py',
    title='Top Goalkeepers per Season',
    icon=':material/bar_chart:',
)


#######################
# Navigation Structure  
#######################
nav = st.navigation(
    {
        'Application Information': [about_page],
        'Tools': [database_page, comparison_page, top_10],
    }
)


#######################
# Page Assests
#######################
st.logo('assets/earps_logo.png')
st.sidebar.text('Made by Matthew Richards')


#######################
# Run Navigation
#######################
nav.run()