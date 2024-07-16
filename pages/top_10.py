import streamlit as st
import pandas as pd
import altair as alt

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

# Load data
df = pd.read_csv('./rating_df.csv')

#######################
# Player Selection Column
#######################

st.markdown("<h1 style='text-align: center; color: #FFF;'>Best Goalkeepers by Season</h1>", unsafe_allow_html=True)
st.write("\n")
st.write("\n")

season_list = sorted(list(df['Season'].unique()), reverse=True)
selected_season = st.selectbox('Select a Season', season_list)
df_selected_season = df[df['Season'] == selected_season]
df_selected_season_sorted = df_selected_season.sort_values(by='Rating', ascending=False)

#######################
# Bar Chart
#######################

# Bar chart function used in the dashboard
# Select Rating for each season
top_20_players = df_selected_season_sorted.head(20)

# Bar Chart
def top_20():
    return alt.Chart(top_20_players).mark_bar().encode(
        x=alt.X('Rating:Q', 
                title='',
                axis=alt.Axis(format='d', labelFontSize=14)), 
        y=alt.Y('Player:N', sort='-x', title='',
                axis=alt.Axis(labelFontSize=14)), 
        color=alt.Color('Rating:Q', scale=alt.Scale(range=["#FF875B", "#89dda5"])),
        tooltip=['Player', 'Rating']
    ).properties(
        title=f'Top 20 Players by Rating in {selected_season} - Expand to see more',
        width='container'
    )

top_20_chart = top_20()

st.altair_chart(top_20_chart, use_container_width=True)
st.write(
    """
    Note: There is minimal data for the season 2018 through till 2021 as the data was not available for all players in the dataset.
    """
)

