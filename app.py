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
# Dummy STEM datasets (keep from lecture)
# -------------------------
physics_data = pd.DataFrame({
    "Experiment": ["Alpha Decay", "Beta Decay", "Gamma Ray Analysis", "Quark Study", "Higgs Boson"],
    "Energy (MeV)": [4.2, 1.5, 2.9, 3.4, 7.1],
    "Date": pd.date_range(start="2024-01-01", periods=5),
})

astronomy_data = pd.DataFrame({
    "Celestial Object": ["Mars", "Venus", "Jupiter", "Saturn", "Moon"],
    "Brightness (Magnitude)": [-2.0, -4.6, -1.8, 0.2, -12.7],
    "Observation Date": pd.date_range(start="2024-01-01", periods=5),
})

weather_data = pd.DataFrame({
    "City": ["Cape Town", "London", "New York", "Tokyo", "Sydney"],
    "Temperature (°C)": [25, 10, -3, 15, 30],
    "Humidity (%)": [65, 70, 55, 80, 50],
    "Recorded Date": pd.date_range(start="2024-01-01", periods=5),
})

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
    st.header("Professional Experience")
    st.write("**Administrative Assistant (2017–Present)** — DSI-NRF Centre of Excellence in Food Security, University of the Western Cape")
    st.write("- Support logistics, travel, and coordination of collaborative research activities")
    st.write("- Assist in annual reporting, database management, and academic event organization")
    st.write("- Facilitate engagement between researchers, students, and external partners")
    st.write("- Involved in documentation and dissemination of food systems knowledge and learning exchanges")

    st.divider()

    # Skills
    st.header("Skills & Tools")
    st.write("**Research:** Qualitative & Quantitative Research")
    st.write("**Software:** Atlas.ti, SPSS, Microsoft Office")
    st.write("**Languages:** English, isiXhosa (fluent); French (in progress)")

    st.divider()

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

elif menu == "STEM Data Explorer":
    st.title("STEM Data Explorer")
    st.sidebar.header("Data Selection")

    data_option = st.sidebar.selectbox(
        "Choose a dataset to explore",
        ["Physics Experiments", "Astronomy Observations", "Weather Data"]
    )

    if data_option == "Physics Experiments":
        st.write("### Physics Experiment Data")
        energy_filter = st.slider("Filter by Energy (MeV)", 0.0, 10.0, (0.0, 10.0))
        filtered = physics_data[physics_data["Energy (MeV)"].between(*energy_filter)]
        st.dataframe(filtered, use_container_width=True)

    elif data_option == "Astronomy Observations":
        st.write("### Astronomy Observation Data")
        brightness_filter = st.slider("Filter by Brightness (Magnitude)", -15.0, 5.0, (-15.0, 5.0))
        filtered = astronomy_data[astronomy_data["Brightness (Magnitude)"].between(*brightness_filter)]
        st.dataframe(filtered, use_container_width=True)

    else:
        st.write("### Weather Data")
        temp_filter = st.slider("Filter by Temperature (°C)", -10.0, 40.0, (-10.0, 40.0))
        humidity_filter = st.slider("Filter by Humidity (%)", 0, 100, (0, 100))
        filtered = weather_data[
            weather_data["Temperature (°C)"].between(*temp_filter) &
            weather_data["Humidity (%)"].between(*humidity_filter)
        ]
        st.dataframe(filtered, use_container_width=True)

elif menu == "Contact":
    st.title("Contact")
    st.write("**Email:** lutandod@gmail.com")
    st.write("**LinkedIn:** @nolutandodidiza")
    st.caption("Tip: Keep public pages free of home addresses and phone numbers.")
