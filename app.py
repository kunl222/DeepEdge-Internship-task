import streamlit as st
import requests

st.set_page_config(page_title="Wikipedia Topic Explorer", layout="centered")

st.title("📚 Wikipedia Topic Explorer")
st.markdown("Enter a topic (e.g., 'deep learning') to scrape its Wikipedia article.")

topic = st.text_input("Topic", "")

if st.button("Scrape Wikipedia") and topic:
    try:
        response = requests.post(
            "http://localhost:5000/scrape",
            json={"query": topic}
        )
        if response.status_code == 200:
            data = response.json()
            st.success("Article Summary:")
            st.write(data["content"])
            st.markdown(f"[Read more on Wikipedia]({data['source_url']})")
        else:
            st.error("❌ Failed to fetch content from Wikipedia.")
    except Exception as e:
        st.error(f"❌ Request failed: {e}")



    # python -m streamlit run "d:/deepseek project/streamlit/streamlit_app/app.py"
