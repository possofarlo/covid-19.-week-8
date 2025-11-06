import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Set page title
st.title("COVID-19 Research Papers Dashboard")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("papers.csv")
    df['publish_time'] = pd.to_datetime(df['publish_time'])
    df['year'] = df['publish_time'].dt.year
    return df

df = load_data()

# Show data info
st.write(f"Total papers: {len(df)}")
st.write("### Sample Data")
st.dataframe(df.head())

# Plot papers by year
st.write("### Papers Published by Year")
fig, ax = plt.subplots()
df['year'].value_counts().sort_index().plot(kind='bar', ax=ax)
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
st.pyplot(fig)

# Top journals
st.write("### Top Journals")
top_journals = df['journal'].value_counts().head(5)
st.bar_chart(top_journals)

# Word cloud of titles
st.write("### Common Words in Paper Titles")
text = ' '.join(df['title'].astype(str))
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
st.pyplot(fig)