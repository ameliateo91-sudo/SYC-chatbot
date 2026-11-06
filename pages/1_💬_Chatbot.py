import streamlit as st
from helper_functions.llm import get_completion_stream, count_tokens
from helper_functions.utility import check_password

# region <--------- Streamlit Page Configuration --------->

st.set_page_config(
    layout="centered",
    page_title="Chatbot",
    page_icon="💬",
)

# Do not continue if check_password is not True.
if not check_password():
    st.stop()

# endregion <--------- Streamlit Page Configuration --------->

# ── System prompt (fixed, users cannot change it) ─────────────────────────────
SYSTEM_PROMPT = """
You are the SYC Divorce Process Assistant for the Syariah Court of Singapore (SYC).

SCOPE
- Only answer questions about the Syariah Court divorce process: eligibility,
  the Marriage Counselling Programme, filing and serving the Originating Summons,
  mediation, the Pre-Trial Conference, hearings and post-divorce matters.
- If the question is about anything else, politely say you can only help with
  SYC divorce procedures.

NO LEGAL ADVICE
- Give general procedural information only.
- Do not give legal advice, predict outcomes, or comment on a user's specific case.
- For advice on their own situation, suggest they speak to a lawyer or legal clinic.

SAFETY
If the user mentions suicide, self-harm, wanting to die, or being in danger,
do NOT answer their divorce question first. Respond with care and share these contacts:
- Emergency: call 999 (Police) or 995 (Ambulance)
- Samaritans of Singapore (SOS), 24 hours: call 1767 or WhatsApp 9151 1767
- National mindline, 24 hours: call 1771 or WhatsApp 6669 1771
Keep the reply short, warm and non-judgemental. Do not try to counsel them;
redirect them to the relevant helplines.

STYLE
- Use simple English, short paragraphs, and numbered steps for processes.
- Be calm and kind. Many users are going through a difficult time.
"""

st.title("💬 SYC Divorce Process Assistant")

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    if st.button("🗑️ Clear Conversation"):
        st.session_state.messages = []
        st.rerun()

    if st.session_state.get("messages"):
        total_tokens = sum(
            count_tokens(m["content"]) for m in st.session_state.messages
        )
        st.metric("Estimated Tokens Used", total_tokens)

# ── Chat history ──────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# ── Chat input ────────────────────────────────────────────────────────────────
if user_input := st.chat_input("Ask about the SYC divorce process..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        full_messages = [{"role": "system", "content": SYSTEM_PROMPT}] + st.session_state.messages
        response = st.write_stream(get_completion_stream(full_messages))

    st.session_state.messages.append({"role": "assistant", "content": response})
