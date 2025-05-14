import streamlit as st
import openai
import os

# Load API key
api_key = st.secrets["openai_api_key"] if "openai_api_key" in st.secrets else os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

psl_teams = [
    "Lahore Qalandars", "Karachi Kings", "Islamabad United",
    "Peshawar Zalmi", "Multan Sultans", "Quetta Gladiators"
]

def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

def predict_scores(team1, team2):
    prompt = f"""
    Predict the scores of a Pakistan Super League (PSL) match between {team1} and {team2}.
    Provide realistic T20 score predictions for both teams, including key batsmen and bowlers.
    """
    return ask_gpt(prompt)

def predict_squads(team):
    prompt = f"""
    Predict the probable playing XI squad of {team} for the upcoming PSL tournament.
    Include captain, wicketkeeper, top batsmen, bowlers, and all-rounders.
    """
    return ask_gpt(prompt)

def predict_tournament_outcome():
    prompt = """
    Predict the 4 PSL teams most likely to reach playoffs, then semi-finals, finalists, and the winner.
    Also predict the top run-scorer and top wicket-taker of the tournament with reasoning.
    """
    return ask_gpt(prompt)

st.set_page_config(page_title="PSL AI Predictor", page_icon="🏏")
st.title("🏏 PSL AI Chatbot Predictor")
st.markdown("This AI predicts PSL match scores, team squads, top performers, and tournament results anonymously using GPT-4.")

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
