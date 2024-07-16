import streamlit as st

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
# Top Two Columns
#######################

col1,= st.columns(1, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/earps_logo_main.png", width=230)
    st.write(
        "Named after the English Shotstopper, Mary Earps, **EARPS** Scouting & Rating Platform is designed to help scouts and analysts find & compare goalkeepers in the top 5 European leagues in Women's football."
    )

#######################
# Rating Explainer
#######################

st.write("\n")
st.markdown("<h2 style='color: #89dda5;'>How the ratings were calculated</h2>", unsafe_allow_html=True)
st.write(
    """
    Using data from FBREF, the following metrics were selected: \n
    - PSxG +/- per 90
    - Crosses Stopped % per 90
    - Def Actions Outside Penalty Area per 90 \n
    These metrics were then fed into an XGBoost model to indentify each variables importance (when trying to make a prediction with Goals Against per 90 as a target variable). The feature importance number was then used to weight
    each metric before being scaled 0-10 to create a rating number. Minutes played was also taken into consideration when calculating the final rating. \n
    """
)

#######################
# Tools Explainer
#######################

st.write("\n")
st.markdown("<h2 style='color: #89dda5;'>Tools on the platform</h2>", unsafe_allow_html=True)
st.write(
    """
    ##### Goalkeeper Database \n
    Use Streamlit's interactive dataframe tools to filter, edit & download the data from the complete database. \n
    ###### Seasons For Each League \n
    - England: 2018-19 to 2023-2024
    - Italy: 2020-21 to 2023-2024
    - France: 2021-22 to 2023-2024
    - Germany: 2022-23 to 2023-2024
    - Spain: 2022-23 to 2023-2024

    ##### Player Comparison Tool \n
    Find any two goalkeepers in the database and compare their average rating (and other metrics) for all the seasons they have played in side by side. \n

    ##### Top Goalkeepers per Season \n
    Visualisation of the top 20 rated goalkeepers per season. The visualisation can be expanded and downloaded. \n
    ----
    """
)

#######################
# About the Data & the Creator
#######################

st.markdown('''
            About the Data & the Creator
            - **Data**: <a href="https://fbref.com/en/" style="color: #89dda5;">FBREF</a>
            - **Created By**: <a href="https://www.linkedin.com/in/matthewrichardsdata/" style="color: #89dda5;">Matthew Richards</a>
            ''', unsafe_allow_html=True)