import streamlit as st
import pandas as pd

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
        color: #FF875B;
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

# Page title using custom CSS
st.markdown("<h1 style='text-align: center; color: #FFF;'>Player Average Rating & Metric Comparison</h1>", unsafe_allow_html=True)

#######################
# Select Boxes
#######################

# Columns for player selection
left, right = st.columns(2)

# Session state for player selections
if 'player1_selection' not in st.session_state:
    st.session_state['player1_selection'] = df['Player'].iloc[0]  # Default to first player if not set
if 'player2_selection' not in st.session_state:
    st.session_state['player2_selection'] = df['Player'].iloc[1]  # Default to second player if not set

with left:
    player1 = st.selectbox("Select Player 1", df['Player'].unique(), index=list(df['Player'].unique()).index(st.session_state['player1_selection']), key="player1_select")
    st.session_state['player1_selection'] = player1  # Update session state so select not lost when navigating between pages

with right:
    player2 = st.selectbox("Select Player 2", df['Player'].unique(), index=list(df['Player'].unique()).index(st.session_state['player2_selection']), key="player2_select")
    st.session_state['player2_selection'] = player2  # Update session state so select not lost when navigating between pages

#######################
# App Logic/Functionality
#######################

# Check if both players are selected
if player1 and player2:
    # Filter the DataFrame for the selected players
    player1_data = df[df['Player'] == player1]
    player2_data = df[df['Player'] == player2]

# For Player 1 current age & team
if not player1_data.empty:
    player1_2023_24_data = player1_data[player1_data['Season'] == "2023-24"]
    if not player1_2023_24_data.empty:
        player_age_2023_24_player1 = player1_2023_24_data['Age'].iloc[0]
        player_team_2023_24_player1 = player1_2023_24_data['Team'].iloc[0]
    else:
        player_age_2023_24_player1 = "Data not available"
        player_team_2023_24_player1 = "Data not available"
else:
    player_age_2023_24_player1 = "Data not available"
    player_team_2023_24_player1 = "Data not available"

# For Player 2 current age & team
if not player2_data.empty:
    player2_2023_24_data = player2_data[player2_data['Season'] == "2023-24"]
    if not player2_2023_24_data.empty:
        player_age_2023_24_player2 = player2_2023_24_data['Age'].iloc[0]
        player_team_2023_24_player2 = player2_2023_24_data['Team'].iloc[0]
    else:
        player_age_2023_24_player2 = "Data not available"
        player_team_2023_24_player2 = "Data not available"
else:
    player_age_2023_24_player2 = "Data not available"
    player_team_2023_24_player2 = "Data not available"

# Calculate the total number of Seasons for both players
def calculate_unique_seasons(player_data):
    if not player_data.empty:
        unique_seasons = player_data['Season'].nunique()
        return unique_seasons
    else:
        return "No data available"
    
total_seasons_player1 = calculate_unique_seasons(player1_data)
total_seasons_player2 = calculate_unique_seasons(player2_data)

# Calculate average minutes played per season for Player 1
if not player1_data.empty:
    avg_minutes_player1 = round(player1_data['Minutes'].sum() / total_seasons_player1)
else:
    avg_minutes_player1 = "Data not available"

# Calculate average minutes played per season for Player 2
if not player2_data.empty:
    avg_minutes_player2 = round(player2_data['Minutes'].sum() / total_seasons_player2)
else:
    avg_minutes_player2 = "Data not available"

# Calculate average metrics for Player 1
avg_rating_player1 = round(player1_data['Rating'].mean(), 2)
avg_psxg_player1 = round(player1_data['PSxG +/- per 90'].mean(), 2)
avg_crosses_stopped_player1 = round(player1_data['Crosses Stopped % per 90'].mean(), 2)
avg_def_actions_outside_pa_player1 = round(player1_data['Def Actions Outside Penalty Area per 90'].mean(), 2)
avg_goals_against_player1 = round(player1_data['Goals Against per 90'].mean(), 2)

# Calculate average metrics for Player 2
avg_psxg_player2 = round(player2_data['PSxG +/- per 90'].mean(), 2)
avg_crosses_stopped_player2 = round(player2_data['Crosses Stopped % per 90'].mean(), 2)
avg_def_actions_outside_pa_player2 = round(player2_data['Def Actions Outside Penalty Area per 90'].mean(), 2)
avg_goals_against_player2 = round(player2_data['Goals Against per 90'].mean(), 2)
avg_rating_player2 = round(player2_data['Rating'].mean(), 2)

#######################
# Player Data Columns
#######################

# Creating column layout
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

# Column 1: Display
with col1:
    st.markdown(f'<p class="big-font">Current Age<br><span class="metric">{player_age_2023_24_player1}</span></p>', unsafe_allow_html=True)
    st.markdown(f'<p class="big-font">Current Team<br><span class="metric">{player_team_2023_24_player1}</span></p>', unsafe_allow_html=True)
    st.markdown(f'<p class="big-font">Average Rating<br><span class="metric">{avg_rating_player1}</span></p>', unsafe_allow_html=True)
    st.markdown(f'<p class="big-font">Total Seasons of Data<br><span class="metric">{total_seasons_player1}</span></p>', unsafe_allow_html=True)
    st.markdown(f'<p class="big-font">Average Minutes per Season<br><span class="metric">{avg_minutes_player1}</span></p>', unsafe_allow_html=True)
    st.write("---")
    st.markdown(f'<p class="big-font">PSxG +/- per 90<br><span class="metric">{avg_psxg_player1}</span></p>', unsafe_allow_html=True)
    st.markdown(f'<p class="big-font">Crosses Stopped % per 90<br><span class="metric">{avg_crosses_stopped_player1}</span></p>', unsafe_allow_html=True)
    st.markdown(f'<p class="big-font">Def Actions Outside Penalty Area per 90<br><span class="metric">{avg_def_actions_outside_pa_player1}</span></p>', unsafe_allow_html=True)
    st.markdown(f'<p class="big-font">Goals Against per 90<br><span class="metric">{avg_goals_against_player1}</span></p>', unsafe_allow_html=True)

# Column 2: Display
with col2:
    st.markdown(f'<p class="big-font-2">Current Age<br><span class="metric">{player_age_2023_24_player2}</span></p>', unsafe_allow_html=True)
    st.markdown(f'<p class="big-font-2">Current Team<br><span class="metric">{player_team_2023_24_player2}</span></p>', unsafe_allow_html=True)
    st.markdown(f'<p class="big-font-2">Average Rating<br><span class="metric">{avg_rating_player2}</span></p>', unsafe_allow_html=True)
    st.markdown(f'<p class="big-font-2">Total Seasons of Data<br><span class="metric">{total_seasons_player2}</span></p>', unsafe_allow_html=True)
    st.markdown(f'<p class="big-font-2">Average Minutes per Season<br><span class="metric">{avg_minutes_player2}</span></p>', unsafe_allow_html=True)
    st.write("---")
    st.markdown(f'<p class="big-font-2">PSxG +/- per 90<br><span class="metric">{avg_psxg_player2}</span></p>', unsafe_allow_html=True)
    st.markdown(f'<p class="big-font-2">Crosses Stopped % per 90<br><span class="metric">{avg_crosses_stopped_player2}</span></p>', unsafe_allow_html=True)
    st.markdown(f'<p class="big-font-2">Def Actions Outside Penalty Area per 90<br><span class="metric">{avg_def_actions_outside_pa_player2}</span></p>', unsafe_allow_html=True)
    st.markdown(f'<p class="big-font-2">Goals Against per 90<br><span class="metric">{avg_goals_against_player2}</span></p>', unsafe_allow_html=True)
