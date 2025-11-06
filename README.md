# COVID-19 Research Papers Dashboard

## Files
- papers.csv: Sample dataset of 100 fake research papers{couldn't access the real dataset} with titles, journals, and publication dates.
- app.py: Streamlit app that loads the data and displays charts and word clouds.

## Run the App
1. Open terminal in the project folder.
2. Install dependencies:
   pip install streamlit pandas matplotlib wordcloud
3. Start the app:
   streamlit run app.py
4. Open http://localhost:8501 in your browser.

## What it shows
- Number of papers published each year
- Top 5 journals
- Most common words in paper titles

## Key Code Features
- @st.cache_data: Speeds up loading by storing the dataset in memory
- pd.to_datetime(): Converts text dates to proper date format for year extraction
- df['year'].value_counts().sort_index().plot(): Counts papers by year and creates a bar chart
- WordCloud(): Generates a visual of most frequent words from paper titles

No login required. No external data. Works offline.