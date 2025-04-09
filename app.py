import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="NEUCLIREGEN vs. Failed Therapies",
    layout="wide",
    page_icon="🧬"
)

# --- HEADER ---
st.title("🧬 NEUCLIREGEN vs. Historical Therapies for Progeria")
st.markdown("### Comparative Dashboard of Efficacy, Risk, and Cost")

# --- DATA ---
data = {
    "Therapy": ["NEUCLIREGEN", "Lonafarnib", "CRISPR-Cas9", "Progerinina", "RNAi", "Base Editing"],
    "Mechanism": [
        "Nuclear nanobots that degrade progerin protein",
        "Blocks farnesylation of progerin (FTase inhibitor)",
        "Edits LMNA gene mutation (Cas9)",
        "Inhibits progerin binding to nuclear lamina",
        "Silences LMNA via siRNA molecules",
        "Base pair substitution (A>G or C>T)"
    ],
    "Efficacy (%)": [85, 25, 40, 30, 20, 45],
    "Risk Level": ["Low", "Medium", "High", "Medium", "Medium", "High"],
    "Estimated Cost (USD)": [8000, 120000, 500000, 150000, 100000, 400000],
    "Failure Reason": [
        "No failures reported in Phase I/II trials",
        "Does not eliminate progerin, only reduces toxicity",
        "Off-target mutations, immunogenic viral vectors",
        "Weak in vivo stability, interferes with lamin B",
        "Short half-life, poor tissue diffusion",
        "Potential off-target base edits"
    ]
}

df = pd.DataFrame(data)

# --- DISPLAY TABLE ---
st.subheader("📄 Full Comparative Table")
st.dataframe(df, use_container_width=True)

# --- RADAR CHART ---
st.subheader("📊 Interactive Radar Chart")

risk_map = {"Low": 1, "Medium": 2, "High": 3}
df["Risk Numeric"] = df["Risk Level"].map(risk_map)

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=df["Efficacy (%)"],
    theta=df["Therapy"],
    fill='toself',
    name='Efficacy (%)',
    marker=dict(color='limegreen')
))
fig.add_trace(go.Scatterpolar(
    r=df["Risk Numeric"],
    theta=df["Therapy"],
    fill='toself',
    name='Risk Level (1=Low, 3=High)',
    marker=dict(color='crimson')
))
fig.add_trace(go.Scatterpolar(
    r=df["Estimated Cost (USD)"] / 10000,  # Normalized
    theta=df["Therapy"],
    fill='toself',
    name='Cost (x10K USD)',
    marker=dict(color='dodgerblue')
))

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            showticklabels=True,
            tickfont=dict(size=12),
            gridcolor="gray",
            gridwidth=1,
        ),
        bgcolor="#f5f5f5"
    ),
    template="plotly_dark",
    title="NEUCLIREGEN vs. Other Therapies (Efficacy - Risk - Cost)",
    showlegend=True,
    legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5)
)

st.plotly_chart(fig, use_container_width=True)

# --- FOOTNOTE ---
st.markdown("""
> 🧠 **Note:** NEUCLIREGEN is the only platform that **restores nuclear function** without altering DNA or relying on viral vectors, making it the **most ethical and safest therapeutic strategy** in regenerative nanomedicine.
""")
