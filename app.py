import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scraper import generate_roll_numbers, get_all_cgpas_parallel, export_to_csv

st.title("📊 CGPA Scraper & Visualizer")

st.sidebar.header("Enter Class Details")
year = st.sidebar.text_input("Admission Year (e.g. 23)")
degree = st.sidebar.text_input("Degree (e.g. B)")
branch = st.sidebar.text_input("Branch Code (e.g. ME)")
start_roll = st.sidebar.number_input("Start Roll No", 1, 999)
end_roll = st.sidebar.number_input("End Roll No", 1, 999)
workers = st.sidebar.slider("Parallel Threads", 1, 20, 5)

if st.sidebar.button("Fetch Results"):
    with st.spinner("Scraping CGPAs..."):
        rolls = generate_roll_numbers(year, degree, branch, start_roll, end_roll)
        results = get_all_cgpas_parallel(rolls, year, max_workers=workers)
        df = pd.DataFrame(list(results.items()), columns=["Roll Number", "CGPA"])
        df = df.dropna()
        df['CGPA'] = pd.to_numeric(df['CGPA'], errors='coerce')
        df = df.dropna()

        # Save CSV
        df.to_csv("cgpa_results.csv", index=False)

        st.success("✅ Scraping Done!")

        st.header("Summary Statistics")
        st.write(df['CGPA'].describe())

        st.header("📈 CGPA Distribution")
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.histplot(df['CGPA'], bins=20, kde=True, ax=ax, color='skyblue')
        st.pyplot(fig)
        st.header("🏆 Top 10 Performers")
        top_df = df.sort_values(by="CGPA", ascending=False).head(10)
        st.table(top_df)


        st.download_button("Download CSV", data=df.to_csv(index=False), file_name="cgpa_results.csv")

