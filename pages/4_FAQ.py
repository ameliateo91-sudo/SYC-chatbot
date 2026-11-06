import streamlit as st
from helper_functions.utility import check_password

st.set_page_config(layout="centered", page_title="FAQ", page_icon="❓")

# Do not continue if check_password is not True.
if not check_password():
    st.stop()

DIVORCE_GUIDE_ENGLISH = "https://file.go.gov.sg/sycdivorceguides-eng.pdf"
DIVORCE_GUIDE_MALAY = "https://file.go.gov.sg/sycdivorceguide-malay.pdf"

OVERVIEW = "https://syariahcourt.gov.sg/Divorce/Overview"
PRE_DIVORCE = "https://syariahcourt.gov.sg/Divorce/Process-Pre-Divorce"
POST_DIVORCE = "https://syariahcourt.gov.sg/Divorce/Process-Post-Divorce"
FEES = "https://cm.syariahcourt.gov.sg/Divorce/Fees"
APPEALS = "https://cm.syariahcourt.gov.sg/Divorce/Appeals"
RECONCILIATION = "https://cm.syariahcourt.gov.sg/Divorce/Reconciliation"

# ── FAQ content ───────────────────────────────────────────────────────────────
# Each category holds a list of (question, answer, source link).
# To add a question, copy one block ( "Question?", """Answer""", LINK ), and paste it below.
FAQS = {
    "Before filing": [
        (
            "Who can file for divorce at the Syariah Court?",
            """
You can apply if **you and your spouse are Muslims, or were married under Muslim law**.
At least one of you must also:
- be a Singapore citizen; **or**
- have lived in Singapore for at least **3 continuous years** before applying; **or**
- be domiciled in Singapore (treat Singapore as your permanent home).

If neither of you is a Singapore citizen, you must show proof of residence in Singapore
for the 3 years before applying, e.g. an employment pass, employment agreement or tenancy agreement.
""",
            PRE_DIVORCE,
        ),
        (
            "What do I need to do before I can file for divorce?",
            """
You must **register for and attend the Marriage Counselling Programme (MCP)** before filing.
If it applies to you, you must also attend the **Parenting Programme**.
Registration for the MCP is done online through the **SYC Portal**.
""",
            PRE_DIVORCE,
        ),
        (
            "What are the main stages of the divorce process?",
            """
1. **Pre-divorce:** Marriage Counselling Programme
2. **Divorce proceedings:** filing the Originating Summons → serving the Originating Summons →
   mediation → Pre-Trial Conference → hearing (or hearing with Hakam)
3. **Post-divorce:** variation applications (summons) and enforcement of Syariah Court orders
""",
            OVERVIEW,
        ),
    ],
    "Using the SYC Portal": [
        (
            "How do I submit my applications?",
            """
All applications, including MCP registration, must be filed through **eServices on the SYC Portal**.
Read the *General Navigation* user guide first (see the **Useful Links** page).
Check your account regularly for status updates and messages.
""",
            OVERVIEW,
        ),
        (
            "I'm a foreigner without Singpass. How do I log in?",
            """
Singapore citizens, Permanent Residents and foreigners **with** Singpass log in with Singpass.
Foreigners **without** Singpass must first apply for an **SYCPass** on the SYC Portal login page.
""",
            OVERVIEW,
        ),
        (
            "Can Syariah Court staff give me legal advice or help me draft documents?",
            """
No. The Court's information is general and is not legal advice, and staff cannot help draft documents.
Only a lawyer can advise you on the merits of your case.
""",
            OVERVIEW,
        ),
    ],
    "Fees": [
        (
            "How much does it cost to file for divorce?",
            """
The Court's estimate of the **maximum** court fees:
- **Plaintiff** (filing the Originating Summons): about **$87**
- **Defendant** (filing the Memorandum of Defence): about **$42**

Some items only apply in certain cases (e.g. parenting or matrimonial property plans).
The **registration of divorce** fee is **$100**. See the Fees page for the full list.
""",
            FEES,
        ),
        (
            "How do I pay?",
            """
All fees are paid through the **SYC Portal** by **PayNow** or **eNETS / credit card**.
Filing fees for rejected or returned documents are not refundable, but a returned document can be
resubmitted in the same filing transaction without paying again.
""",
            FEES,
        ),
    ],
    "After the divorce": [
        (
            "Where do I get my divorce certificate?",
            """
You can download it from the **SYC Portal** under **"Court File"**:
- divorces registered **before 18 November 2022**: under *Court Orders*
- divorces registered **after 1 December 2022**: under *Court Documents*

It becomes available after an administrative period that depends on your case.
If you have a lawyer, the certificate is made available to your lawyer instead.
""",
            POST_DIVORCE,
        ),
        (
            "Can I appeal a decision?",
            """
- **Against a Registrar's direction or order:** file within **14 days** through the SYC Portal.
  It is heard by a President of the Syariah Court.
- **Against a Syariah Court decision:** file within **30 days** with the **Appeal Board**, run by MUIS.

In both cases, serve a copy of the notice on every other party within 3 days of filing.
Get legal advice on the merits before deciding to appeal.
""",
            APPEALS,
        ),
        (
            "Talak was pronounced outside court, but we want to reconcile. What do we do?",
            """
Both of you must come to the **Syariah Court in person within 7 days** of the talak being pronounced.
The Court will decide whether the out-of-court divorce is valid. If it is registered, you then both
attend the **Registry of Muslim Marriages** in person to register the revocation (rujuk) or remarriage.

If either of you wants to go ahead with the divorce, the usual process applies instead
(including the Marriage Counselling Programme).
""",
            RECONCILIATION,
        ),
    ],
}

# ── Page ──────────────────────────────────────────────────────────────────────
st.title("❓ Frequently Asked Questions")
st.write("Common questions about the Syariah Court divorce process.")

col1, col2 = st.columns(2)
col1.link_button("📘 Divorce Guide (English)", DIVORCE_GUIDE_ENGLISH)
col2.link_button("📗 Divorce Guide (Malay)", DIVORCE_GUIDE_MALAY)

search = st.text_input("🔍 Search the FAQs", placeholder="e.g. fees, certificate, Singpass")

found_any = False
for category, questions in FAQS.items():
    # keep only the questions that match the search (or all of them if search is empty)
    matches = [
        (q, a, link) for q, a, link in questions
        if search.lower() in q.lower() or search.lower() in a.lower()
    ]
    if not matches:
        continue
    found_any = True
    st.subheader(category)
    for question, answer, link in matches:
        with st.expander(question):
            st.markdown(answer)
            st.caption(f"Source: [Syariah Court website]({link})")

if not found_any:
    st.info("No FAQs match your search. Try another word, or ask the Chatbot.")

st.divider()
st.caption(
    "This page gives general information only and is not legal advice. "
    "For full details, refer to the SYC Divorce Guide or contact the Syariah Court "
    "at (65) 6354 8371 or MCCY_Syariah@mccy.gov.sg."
)