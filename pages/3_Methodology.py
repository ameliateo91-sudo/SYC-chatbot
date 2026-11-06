import streamlit as st

st.title("Methodology")

# ---------- 1. Overview ----------
st.header("Overview")
st.write("""
The SYC Divorce Process Assistant uses OpenAI's gpt-4o-mini model to answer
questions about the Syariah Court divorce process. It is trained on approved content from the Syariah Court website, and is designed to provide accurate and relevant information while adhering to strict guardrails to ensure safety and compliance.
""")

# ---------- 2. Scope ----------
st.header("Scope")
st.write("This chatbot covers the **Syariah Court divorce process only**:")
st.markdown("""
1. Eligibility to file for divorce at the Syariah Court
2. Marriage Counselling Programme
3. Filing the Originating Summons
4. Serving the Originating Summons
5. Mediation
6. Pre-Trial Conference
7. Hearing
""")

st.write("**Out of scope**: the chatbot will politely decline and redirect:")
st.markdown("""
- Legal advice or questions about the merits of a specific case
- Other Syariah Court services (e.g. inheritance certificates)
- Civil court divorce matters
- Questions unrelated to divorce
""")

# ---------- 3. Data source ----------
st.header("Data source")
st.markdown("""
- Approved content from the Syariah Court of Singapore website
- Content is split into small chunks so the chatbot can find the relevant part quickly
""")

# ---------- 4. Flowchart ----------
st.header("How the chatbot works")
st.graphviz_chart("""
digraph {
    node [shape=box, style=rounded]
    Q [label="User asks a question"]
    C [label="Is it about the SYC divorce process?", shape=diamond]
    N [label="Polite reply: I can only help with SYC divorce procedures"]
    R [label="Find relevant SYC content"]
    L [label="LLM answers using that content only"]
    A [label="Show answer + sources"]
    Q -> C
    C -> N [label="No"]
    C -> R [label="Yes"]
    R -> L -> A
}
""")

# ---------- 5. Guardrails ----------
st.header("Guardrails")
st.markdown("""
- Answers only from approved SYC content
- Does not give legal advice; redirects to a lawyer or legal clinic if asked 
- Shows emergency contacts if a user mentions being in danger 
- Uses delimiters to protect against prompt injection
- Password-protected, with a disclaimer on every page
""")