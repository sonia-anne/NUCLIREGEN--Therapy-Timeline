import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="NUCLIREGEN | Progeria Therapy Timeline", layout="wide")

st.title("🧬 NUCLIREGEN Dashboard")
st.markdown("## 📆 Timeline: 20 Years of Progeria Therapeutics (2003–2023)")

# Timeline Data
timeline_data = {
    "Year": [2003, 2006, 2010, 2013, 2015, 2017, 2020, 2021, 2023],
    "Treatment": [
        "Genetic Discovery",
        "Lonafarnib Preclinical",
        "Lonafarnib Phase II",
        "CRISPR (in vitro)",
        "CRISPR (mice)",
        "Progerinina Discovery",
        "Lonafarnib FDA Approval",
        "CRISPR Early Trials",
        "NUCLIREGEN Prototype"
    ],
    "Impact": [
        "LMNA mutation identified",
        "Farnesylation inhibition tested in mice",
        "Limited life extension observed",
        "Gene editing of LMNA in vitro",
        "Partial nuclear recovery in murine models",
        "Targeted degradation potential",
        "Official approval (2.5 years gain)",
        "Low editing precision, immune issues",
        "Nuclear repair, no genome alteration"
    ]
}

df_timeline = pd.DataFrame(timeline_data)

# Timeline Chart
fig = px.scatter(
    df_timeline,
    x="Year",
    y=["Therapy"] * len(df_timeline),
    size=[40]*len(df_timeline),
    color="Treatment",
    hover_name="Treatment",
    text="Impact",
    title="🧭 Evolution of Progeria Therapies (2003–2023)"
)

fig.update_traces(textposition="top center")
fig.update_layout(height=600)

st.plotly_chart(fig)

# Comparative Table
st.markdown("## 📊 Comparative Table: Failed Therapies vs. NUCLIREGEN")

failure_data = {
    "Name": ["Lonafarnib", "CRISPR", "Progerinina", "Gene Therapy", "Epigenetic Editing"],
    "Mechanism": [
        "Farnesylation inhibitor",
        "CRISPR-Cas9 gene editing",
        "Binds progerin-lamin A",
        "Viral DNA delivery",
        "Histone methylation modification"
    ],
    "Efficacy": ["Low", "Moderate", "Unknown", "Partial", "Variable"],
    "Risk": ["Mild", "High", "Unknown", "Very High", "Moderate"],
    "Cost": ["$100K/year", "$500K+", "N/A", "$1M+", "$80K+"],
    "Reason for Failure": [
        "Does not remove progerin",
        "Off-targets + immune reaction",
        "Low specificity/stability",
        "Immune rejection & oncogenic risk",
        "Inconsistent effects + reversal"
    ]
}

df_failures = pd.DataFrame(failure_data)

st.dataframe(df_failures, use_container_width=True)
