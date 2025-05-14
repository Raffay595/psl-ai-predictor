import streamlit as st
from openai import OpenAI
import os

# Load the API key from Streamlit secrets or environment variable
api_key = st.secrets["openai_api_key"] if "openai_api_key" in st.secrets else os.getenv("OPENAI_API_KEY")

# Create the OpenAI client
client = OpenAI(api_key=api_key)

# PSL team data
psl_teams = [
    "Lahore Qalandars",
    "Karachi Kings",
    "Islamabad United",
    "Peshawar Zalmi",
    "Multan Sultans",
    "Quetta Gladiators"
]

# GPT interaction function
def ask_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

# Generate score prediction
def predict_scores(team1, team2):
    prompt = f"""
    Predict the scores of a Pakistan Super League (PSL) match between {team1} and {team2}.
    Provide realistic T20 score predictions for both teams, including key batsmen and bowlers.
    """
    return ask_gpt(prompt)

# Predict probable squad
def predict_squads(team):
    prompt = f"""
    Predict the probable playing XI squad of {team} for the upcoming PSL tournament.
    Include captain, wicketkeeper, top batsmen, bowlers, and all-rounders.
    """
    return ask_gpt(prompt)

# Predict tournament outcome
def predict_tournament_outcome():
    prompt = """
    Predict the 4 PSL teams most likely to reach playoffs, then semi-finals, finalists, and the winner.
    Also predict the top run-scorer and top wicket-taker of the tournament with reasoning.
    """
    return ask_gpt(prompt)

# Streamlit UI
st.set_page_config(page_title="PSL AI Predictor", page_icon="🏏")

st.title("🏏 PSL AI Chatbot Predictor")
st.markdown("This AI predicts PSL match scores, team squads, top performers, and tournament results anonymously using GPT-4.")

# Match Score Prediction
st.subheader("🔮 Match Score Predictor")
team1 = st.selectbox("Select Team 1", psl_teams)
team2 = st.selectbox("Select Team 2", [t for t in psl_teams if t != team1])

if st.button("Predict Match Score"):
    with st.spinner("Predicting match outcome..."):
        result = predict_scores(team1, team2)
        st.success("Prediction complete!")
        st.text(result)

# Squad Prediction
st.subheader("📋 Predict Probable Squad")
selected_team = st.selectbox("Select a Team to Predict Squad", psl_teams)

if st.button("Predict Squad"):
    with st.spinner("Generating squad..."):
        squad = predict_squads(selected_team)
        st.success("Squad predicted!")
        st.text(squad)

# Tournament Simulation
st.subheader("🏆 Tournament Simulation")
if st.button("Run Full Tournament Prediction"):
    with st.spinner("Simulating PSL Tournament..."):
        outcome = predict_tournament_outcome()
        st.success("Prediction complete!")
        st.markdown(outcome)

st.markdown("---")
