import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="Researcher Profile | Nolu Didiza", layout="wide")

# -------------------------
# Sidebar navigation
# -------------------------
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "Publications", "STEM Data Explorer", "Contact"],
)


# -------------------------
# App sections
# -------------------------
if menu == "Researcher Profile":
    st.title("Researcher Profile")

    # Hero section
    col1, col2 = st.columns([2, 1], vertical_alignment="center")

    with col1:
        st.subheader("Nolutando Didiza")
        st.write(
            "Emerging interdisciplinary researcher in development studies and biotechnology, "
            "preparing for a PhD trajectory. Focused on how food systems intersect with gender, "
            "infrastructure, and social/spatial justice in African urban contexts."
        )

        st.markdown("### Research Interests")
        st.write(
            "Agroecology • Urban Food Systems • Gender & Care Work • Spatial Justice • "
            "Informal Economies • Food Infrastructure • Waste Valorisation"
        )

    with col2:
        st.image(
            "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg",
            caption="Public image (Pixabay)",
            use_container_width=True
        )

    st.divider()

    # Education
    st.header("Education")
    st.write("**Master of Development Studies (Ongoing)** — University of the Western Cape")
    st.caption("Coursework: Theories of Social Transformation; Migration & Development; Community Development; Research Methods")
    st.caption("Mini-thesis: Understanding the Biowaste Valorisation Model in South Africa: A Case Study of the RCL Foods Waste-to-Energy Plant in Breede Valley")

    st.write("**BA Honours in Development Studies (2022)** — University of the Western Cape")
    st.caption("Research paper: Critical Review of GM Soybeans and Food Security in Developing Countries")

    st.write("**BSc in Biotechnology (2017)** — University of the Western Cape")
    st.caption("Member: Golden Key International Honour Society")

    st.divider()

    # Experience
    st.header("Research Experience")

st.subheader("Research Assistant – AGRI-COOL Project")
st.caption("Horizon Europe–funded project | Socio-Economic Impact Assessment (Task 6.4)")

st.write(
    "I am currently working as a **Research Assistant on the AGRI-COOL project**, "
    "which focuses on advancing sustainable cooling and renewable energy solutions "
    "within agri-food systems, with particular attention to smallholder and emerging farmers."
)

st.markdown("### Research Background")

st.write(
    "Agricultural systems globally are under increasing pressure from climate change, "
    "rising energy costs, and growing demands for sustainable food production. In South Africa, "
    "these pressures are particularly acute for smallholder and emerging farmers, who often "
    "operate under conditions of energy insecurity, limited access to capital, and inadequate "
    "post-harvest infrastructure."
)

st.write(
    "Post-harvest losses linked to insufficient cold-chain capacity remain a major constraint "
    "to food security, income stability, and market participation among small-scale producers."
)

st.write(
    "In response to these challenges, renewable energy–based agricultural innovations such as "
    "**agrivoltaics**, which integrate solar energy generation with agricultural production, "
    "have gained increasing attention. These systems offer the potential to reduce energy costs, "
    "improve land-use efficiency, and enhance climate resilience."
)

st.write(
    "However, despite growing technical evidence of their benefits, adoption among smallholder "
    "farmers in the Global South remains limited. Emerging research suggests that this is driven "
    "not only by technical or economic barriers, but also by **social, behavioural, and institutional factors**, "
    "including perceived risk, limited access to trusted information, and weak extension systems."
)

st.write(
    "Within the AGRI-COOL project, my research contributes to **Task 6.4: Socio-Economic Impact Assessment**, "
    "examining the behavioural, social, and contextual dimensions influencing the adoption of "
    "agrivoltaic systems and solar-powered cold-chain technologies among smallholder and emerging "
    "farmers in the Western Cape, South Africa."
)


    st.divider()

    # Skills
    st.header("Skills & Tools")
    st.write("**Research:** Qualitative & Quantitative Research")
    st.write("**Software:** Atlas.ti, SPSS, Microsoft Office")
    st.write("**Languages:** English, isiXhosa (fluent); French (in progress)")

st.divider()
st.header("Achievements & Professional Development")

st.subheader("Data Analysis & Data Science Training")

st.write(
    "Successfully completed structured training in **Data Analysis and Data Science**, "
    "with a strong focus on applied skills for research and real-world problem solving."
)

st.markdown("**Key competencies developed include:**")
st.write(
    "- Python programming for data analysis\n"
    "- Data cleaning and preprocessing (Pandas, NumPy)\n"
    "- Exploratory Data Analysis (EDA)\n"
    "- Data visualisation (Matplotlib, Plotly, Streamlit)\n"
    "- Working with CSV files and real-world datasets\n"
    "- Building interactive dashboards using Streamlit\n"
    "- Version control and collaboration using GitHub"
)

st.write(
    "This training strengthened my ability to support empirical research, "
    "socio-economic analysis, and evidence-based decision-making in interdisciplinary projects."
)

    # Community engagement
    st.header("Community Engagement")
    st.write("- Volunteer tutor in maths and science for high school learners")
    st.write("- Advocate for language as a bridge to inclusion in African research spaces")
    st.write("- Committed to mentorship and platform-building for early-career African researchers")

elif menu == "Publications":
    st.title("Publications")
    st.sidebar.header("Upload and Filter")

    uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

    if uploaded_file is not None:
        publications = pd.read_csv(uploaded_file)
        st.subheader("Uploaded Publications")
        st.dataframe(publications, use_container_width=True)

        keyword = st.text_input("Filter by keyword", "")
        if keyword:
            mask = publications.apply(
                lambda row: keyword.lower() in " ".join(row.astype(str).str.lower().values),
                axis=1
            )
            st.write(f"Filtered results for: **{keyword}**")
            st.dataframe(publications[mask], use_container_width=True)
        else:
            st.info("Tip: Type a keyword above to filter (e.g., 'food', 'waste', 'gender').")

        if "Year" in publications.columns:
            st.subheader("Publication Trends")
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)
        else:
            st.warning("Your CSV does not have a 'Year' column. Add it to see trends.")
    else:
        st.info("Upload a CSV to display and explore your publications.")

elif menu == "Contact":
    st.title("Contact")
    st.write("**Email:** lutandod@gmail.com")
    st.write("**LinkedIn:** @nolutandodidiza")
    st.caption("Tip: Keep public pages free of home addresses and phone numbers.")
