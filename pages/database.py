import streamlit as st
import pandas as pd

# Import Google Font
google_fonts_link = "<link href='https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap' rel='stylesheet'>"
st.markdown(google_fonts_link, unsafe_allow_html=True)

# CSS for custom styling
custom_css = """
<style>
    body {
        font-family: 'Inter', sans-serif;
    }
    .stDataFrame {
        margin: 0 auto;
    }
    .stMarkdown {
        text-align: center;
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
st.markdown(custom_css, unsafe_allow_html=True)

#######################
# Load Data
#######################

@st.cache_data
def load_data():
    return pd.read_csv('./rating_df.csv')

df = load_data()

# Page title using custom CSS
st.markdown("<h1 style='text-align: center; color: #FFF;'>Full Database of Goalkeepers</h1>", unsafe_allow_html=True)
st.write("\n\n")

#######################
# Columns for Filters & Dataframe
#######################

# Three columns hold the filtering widgets
col1, col2, col3 = st.columns(3, gap="small")

with col1:
    player_search = st.text_input("Search by Player")
    teams = st.multiselect("Select Teams", options=['All'] + list(df['Team'].unique()))
    seasons = st.multiselect("Select Season", options=['All'] + list(df['Season'].unique()))
    
with col2:
    min_age, max_age = int(df['Age'].min()), int(df['Age'].max())
    age = st.slider("Filter by Age", min_value=min_age, max_value=max_age, value=(min_age, max_age))
    
    min_minutes, max_minutes = int(df['Minutes'].min()), int(df['Minutes'].max())
    minutes = st.slider("Filter by Minutes", min_value=min_minutes, max_value=max_minutes, value=(min_minutes, max_minutes))
    
    min_rating, max_rating = float(df['Rating'].min()), float(df['Rating'].max())
    rating = st.slider("Rating", min_value=min_rating, max_value=max_rating, value=(min_rating, max_rating))

with col3:
    min_psxg, max_psxg = int(df['PSxG +/- per 90'].min()), float(df['PSxG +/- per 90'].max())
    psxg = st.slider("PSxG +/- per 90", min_value=min_psxg, max_value=max_psxg, value=(min_psxg, max_psxg))
    
    min_crosses, max_crosses = int(df['Crosses Stopped % per 90'].min()), float(df['Crosses Stopped % per 90'].max())
    crosses = st.slider("Crosses Stopped % per 90", min_value=min_crosses, max_value=max_crosses, value=(min_crosses, max_crosses))
    
    min_defa, max_defa = float(df['Def Actions Outside Penalty Area per 90'].min()), float(df['Def Actions Outside Penalty Area per 90'].max())
    defa = st.slider("Def Actions Outside Penalty Area per 90", min_value=min_defa, max_value=max_defa, value=(min_defa, max_defa))

# Filtering structure
filtered_df = df.copy()

if player_search:
    filtered_df = filtered_df[filtered_df['Player'].str.contains(player_search, case=False, na=False)]

if 'All' not in teams and teams:
    filtered_df = filtered_df[filtered_df['Team'].isin(teams)]

if 'All' not in seasons and seasons:
    filtered_df = filtered_df[filtered_df['Season'].isin(seasons)]

filtered_df = filtered_df[
    (filtered_df['Age'].between(age[0], age[1])) &
    (filtered_df['Minutes'].between(minutes[0], minutes[1])) &
    (filtered_df['Rating'].between(rating[0], rating[1]))
]

# Display the dataframe
st.dataframe(filtered_df)

# Shows the number of records displayed & explainer message
st.write(f"Showing {len(filtered_df)} out of {len(df)} records. These records can be downloaded as a CSV file. Hover over the dataframe.")
