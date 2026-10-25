import streamlit as st
from portfolio_visuals import render_visuals
def review_claim(claim: str, evidence: str) -> dict:
    if not evidence.strip():
        return {"claim": claim, "status": "UNVERIFIED â€” no evidence supplied", "evidence": [], "next_step": "Add reliable source excerpts or links and verify manually."}
    return {"claim": claim, "status": "EVIDENCE PROVIDED â€” not independently verified", "evidence": [evidence.strip()], "next_step": "Check source identity, date, context, and whether the evidence directly supports the claim."}

st.set_page_config(page_title="Fact Checker", page_icon="ðŸ”Ž")
render_visuals('10_research_fact_checker')
st.title("Research & Fact-Checking Assistant")
claim = st.text_input("Claim to examine")
evidence = st.text_area("Paste source excerpt(s)")
if st.button("Review claim"):
    if not claim.strip(): st.warning("Enter a claim.")
    else: st.json(review_claim(claim, evidence))

