import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("🚀 NUCLIREGEN: Timeline of Progeria Treatments (2003–2025)")

# Timeline Data
timeline_data = {
    "Year": [
        2003, 2006, 2010, 2013, 2015, 2017, 2020, 2021, 2023, 2025
    ],
    "Treatment": [
        "Genetic Discovery",
        "Lonafarnib Preclinical",
        "Lonafarnib Phase II",
        "CRISPR (in vitro)",
        "CRISPR (in vivo - mice)",
        "Progerinina Discovery",
        "Lonafarnib FDA Approval",
        "CRISPR Early Human Trials",
        "NUCLIREGEN Prototype",
        "NUCLIREGEN Clinical Breakthrough"
    ],
    "Details": [
        "🧬 Identification of LMNA gene mutation linked to progeria.",
        "🧪 Initial animal testing on farnesyltransferase inhibitors.",
        "📊 Limited success in extending lifespan in patients.",
        "🔬 Gene editing success in Petri dish models.",
        "🐭 Partial nuclear repair in progeric murine models.",
        "💊 Molecule discovered to bind and neutralize progerin.",
        "✅ FDA approval, life extension by ~2.5 years.",
        "⚠️ Trials show immune response, off-target editing.",
        "🤖 Nanobot prototype created to target progerin inside nucleus.",
        "🏆 Achieves accurate, safe rejuvenation in clinical trials."
    ]
}

df = pd.DataFrame(timeline_data)

# Plotly timeline
fig = px.timeline(
    df,
    x_start="Year",
    x_end=[year + 0.8 for year in df["Year"]],
    y="Treatment",
    color="Treatment",
    hover_name="Treatment",
    hover_data={"Details": True, "Year": False},
    title="🧭 Evolution of Progeria Treatments (2003–2025)",
    color_discrete_sequence=px.colors.qualitative.Set3
)

fig.update_yaxes(autorange="reversed")
fig.update_layout(
    height=700,
    font=dict(family="Roboto Mono", size=14, color="#333333"),
    title_font_size=24,
    plot_bgcolor="#F0F2F6",
    paper_bgcolor="#F0F2F6",
    margin=dict(l=30, r=30, t=60, b=30),
    hoverlabel=dict(bgcolor="white", font_size=13, font_family="Roboto Mono"),
    showlegend=False
)

# Display
st.plotly_chart(fig, use_container_width=True)
