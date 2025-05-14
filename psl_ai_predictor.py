import streamlit as st
import openai
import random
import os

# Load your OpenAI API key
openai.api_key = st.secrets["openai_api_key"] if "openai_api_key" in st.secrets else os.getenv("OPENAI_API_KEY")

# PSL team data (hardcoded, can be replaced with dataset)
psl_teams = [
    "Lahore Qalandars",
    "Karachi Kings",
    "Islamabad United",
    "Peshawar Zalmi",
    "Multan Sultans",
    "Quetta Gladiators"
]

# Prompt Template for GPT
def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()

# Generate score prediction
def predict_scores(team1, team2):
    prompt = f"""
    Predict the scores of a Pakistan Super League (PSL) match between {team1} and {team2}.
    Give a realistic T20 score prediction for each team, including total runs and a few key batsmen and bowlers.
    """
    return ask_gpt(prompt)

# Predict probable squads
def predict_squads(team):
    prompt = f"""
    Predict the probable squad of {team} for the upcoming PSL tournament. Include 11 players, a captain, and key performers.
    """
    return ask_gpt(prompt)

# Predict tournament progression
def predict_tournament_outcome():
    prompt = """
    Based on past PSL patterns, predict which 4 teams are most likely to reach the playoffs, then the semi-finals, finals, and ultimately the winner of the tournament.
    Also predict the top run-scorer and top wicket-taker of the season with reasoning.
    """
    return ask_gpt(prompt)

# Streamlit UI
st.set_page_config(page_title="PSL AI Predictor", page_icon="🏏")

st.title("🏏 PSL AI Chatbot Predictor")
st.markdown("This AI predicts PSL match scores, squads, top players, and final outcomes anonymously.")

st.subheader("🔮 Match Score Predictor")
team1 = st.selectbox("Select Team 1", psl_teams)
team2 = st.selectbox("Select Team 2", [t for t in psl_teams if t != team1])
if st.button("Predict Match Score"):
    with st.spinner("Predicting match outcome..."):
        result = predict_scores(team1, team2)
        st.success("Prediction complete!")
        st.text(result)

st.subheader("📋 Predict Probable Squad")
selected_team = st.selectbox("Select a Team to Predict Squad", psl_teams)
if st.button("Predict Squad"):
    with st.spinner("Generating squad..."):
        squad = predict_squads(selected_team)
        st.success("Squad predicted!")
        st.text(squad)

st.subheader("🏆 Tournament Simulation")
if st.button("Run Full Tournament Prediction"):
    with st.spinner("Simulating PSL Tournament..."):
        outcome = predict_tournament_outcome()
        st.success("Prediction complete!")
        st.markdown(outcome)

st.markdown("---")
st.markdown("🤖 *Powered by GPT-4 and cricket logic. This is just a simulation tool, not gambling advice.*")
