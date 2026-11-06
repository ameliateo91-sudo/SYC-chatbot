import streamlit as st

st.title("🔗 Useful Links")
st.write("Official Syariah Court guides and videos to help you through the divorce process.")

# ── Divorce Guide ─────────────────────────────────────────────────────────────
st.header("📘 SYC Divorce Guide")
st.write(
    "A broad overview of the divorce process and commonly asked questions. "
    "You can refer to it at any stage of your divorce."
)
col1, col2 = st.columns(2)
col1.link_button("English version", "https://file.go.gov.sg/sycdivorceguides-eng.pdf")
col2.link_button("Malay version", "https://file.go.gov.sg/sycdivorceguide-malay.pdf")

# ── Video guides ──────────────────────────────────────────────────────────────
st.header("🎥 Divorce Video Guides")
st.write("Step-by-step videos on using the SYC eServices.")

# (title, English link, Malay link)
VIDEOS = [
    ("Registration for Marriage Counselling Programme",
     "https://www.youtube.com/watch?v=Zh3K_TffO9Q",
     "https://www.youtube.com/watch?v=8P831UQp7YM"),
    ("Marriage Counselling Appointment Scheduling",
     "https://www.youtube.com/watch?v=mrXyaeOZmvI",
     "https://www.youtube.com/watch?v=mls8Mctmet8"),
    ("Filing of Originating Summons for Divorce",
     "https://www.youtube.com/watch?v=x1JFqUi4e80",
     "https://www.youtube.com/watch?v=4JK3fRw1KVk"),
    ("Service of Originating Summons",
     "https://www.youtube.com/watch?v=0L2mkk3fa_w",
     "https://www.youtube.com/watch?v=Azq1I4Y1Aio"),
    ("Filing of Memorandum of Defence",
     "https://www.youtube.com/watch?v=xsHB4mExbws",
     "https://www.youtube.com/watch?v=AA32_7Enl08"),
    ("Filing of Amended Court Documents",
     "https://www.youtube.com/watch?v=2WMJVBRCR1k",
     "https://www.youtube.com/watch?v=TxIG-kpXKBg"),
    ("Filing of Summons",
     "https://www.youtube.com/watch?v=CCjntHceV4U",
     "https://www.youtube.com/watch?v=VHCwV_nqioE"),
]

language = st.radio("Language", ["English", "Malay"], horizontal=True)

for number, (title, english_link, malay_link) in enumerate(VIDEOS, start=1):
    link = english_link if language == "English" else malay_link
    with st.expander(f"{number}. {title}"):
        st.video(link)
        st.markdown(f"[Open on YouTube]({link})")

# ── More ──────────────────────────────────────────────────────────────────────
st.header("📚 More guides")
st.markdown(
    "- [All SYC user guides and videos](https://syariahcourt.gov.sg/Resources/User-Guides-and-Videos)\n"
    "- [eBantu: guidance tool for filling in your Case Statement or Memorandum of Defence (Ministry of Law)]"
    "(https://lab.mlaw.gov.sg/resources/ebantu-syariah-court-originating-documents-guidance-tool/)"
)

st.header("📞 Contact the Syariah Court")
st.markdown(
    "**Address:** Family Link @ Lengkok Bahru, 8 Lengkok Bahru, #03-01, Singapore 159052  \n"
    "**Tel:** (65) 6354 8371  \n"
    "**Email:** MCCY_Syariah@mccy.gov.sg"
)