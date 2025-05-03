# 📚 Wikipedia Topic Explorer

A simple web application that lets users explore concise summaries from Wikipedia by entering a topic of interest. This project uses a **Flask backend** to interact with the Wikipedia REST API and a **Streamlit frontend** for an intuitive user interface.

---

## 🚀 Features

- Fetches summaries of Wikipedia topics via the REST API.
- Clean and interactive UI with Streamlit.
- Error handling for empty or invalid queries.
- Displays both the content and source URL of the article.

---

## 📁 Project Structure

- `backend.pynb`: Flask backend server that queries the Wikipedia REST API.
- `app.py`: Streamlit frontend that sends requests to the backend.
- `README.md`: Project overview and usage instructions.

---

## 🖥️ How It Works

1. User enters a topic (e.g., "machine learning") in the Streamlit UI.
2. Streamlit sends a POST request to the Flask backend.
3. Flask queries `https://en.wikipedia.org/api/rest_v1/page/summary/<topic>`.
4. The API response is returned and displayed to the user.

---

## 🛠️ How to Run
### 1. Start the Backend
### 1. Start the Backend
```bash
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

