DIVORCE_GUIDE_ENGLISH = "https://file.go.gov.sg/sycdivorceguides-eng.pdf"
DIVORCE_GUIDE_MALAY = "https://file.go.gov.sg/sycdivorceguide-malay.pdf"

# ── FAQ content ───────────────────────────────────────────────────────────────
# 👉 Replace the questions and answers below with the ones from the SYC Divorce Guide.
#    Each category holds a list of (question, answer) pairs.
#    To add a question, copy one line like ("Question?", "Answer."), and paste it below.
FAQS = {
    "Before filing": [
        ("Who can file for divorce at the Syariah Court?",
         "[PASTE ANSWER FROM DIVORCE GUIDE]"),
        ("What is the Marriage Counselling Programme (MCP)?",
         "[PASTE ANSWER FROM DIVORCE GUIDE]"),
    ],
    "Filing and serving": [
        ("How do I file the Originating Summons?",
         "[PASTE ANSWER FROM DIVORCE GUIDE]"),
        ("How do I serve the Originating Summons on my spouse?",
         "[PASTE ANSWER FROM DIVORCE GUIDE]"),
    ],
    "During the proceedings": [
        ("What happens at mediation?",
         "[PASTE ANSWER FROM DIVORCE GUIDE]"),
        ("What is a Pre-Trial Conference?",
         "[PASTE ANSWER FROM DIVORCE GUIDE]"),
    ],
    "After the divorce": [
        ("What do I need to do after the divorce is granted?",
         "[PASTE ANSWER FROM DIVORCE GUIDE]"),
    ],
}

# ── Page ──────────────────────────────────────────────────────────────────────
st.title("❓ Frequently Asked Questions")
st.write(
    "Common questions about the Syariah Court divorce process, taken from the "
    "**SYC Divorce Guide**."
)

col1, col2 = st.columns(2)
col1.link_button("📘 Divorce Guide (English)", DIVORCE_GUIDE_ENGLISH)
col2.link_button("📗 Divorce Guide (Malay)", DIVORCE_GUIDE_MALAY)

search = st.text_input("🔍 Search the FAQs", placeholder="e.g. mediation, documents, fees")

found_any = False
for category, questions in FAQS.items():
    # keep only the questions that match the search (or all of them if search is empty)
    matches = [
        (q, a) for q, a in questions
        if search.lower() in q.lower() or search.lower() in a.lower()
    ]
    if not matches:
        continue
    found_any = True
    st.subheader(category)
    for question, answer in matches:
        with st.expander(question):
            st.write(answer)

if not found_any:
    st.info("No FAQs match your search. Try another word, or ask the Chatbot.")

st.divider()
st.caption(
    "This page gives general information only and is not legal advice. "
    "For the full details, refer to the SYC Divorce Guide."
)