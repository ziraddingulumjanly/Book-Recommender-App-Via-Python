# 📚 Book Recommender System

This project is an interactive **Book Recommender System** built using **Python** and **Streamlit**, based on a collaborative filtering approach. It leverages real-world user ratings data to suggest books that are similar to a selected title, using **cosine similarity** between user rating vectors. The underlying dataset includes detailed metadata such as book titles, authors, publication years, publishers, and even cover image URLs, enabling both analytical and visual exploration.

The system filters out low-quality and sparse data to focus on meaningful ratings, ensuring high-quality recommendations. Once a user selects a book, the app returns a ranked list of the most similar titles along with their similarity scores. In addition to a summary table, it visually showcases each recommended book’s cover, author, publisher, and publication year — making the experience both informative and user-friendly.

Designed for both educational and practical use, this project demonstrates key concepts in recommendation systems, including data preprocessing, user-item matrix construction, similarity measurement, and interactive deployment. It’s ideal for anyone interested in building intelligent applications from real data, exploring collaborative filtering, or simply discovering new books.
Perfect! Here's a continuation of your `README.md` — now including a clear and concise **"How to Run"** section with instructions for cloning, installing, and running the app locally using Streamlit:

---

### 🛠️ How to Run the Project Locally

To run the Book Recommender System on your local machine:

1. **Clone the repository** or download it as a ZIP and extract it:

2. **Make sure you have the required Python packages installed**. If not, install them using:

```bash
pip install pandas numpy scikit-learn streamlit
```
3. **Run the Streamlit app**:

```bash
streamlit run app.py
```

4. A browser window will automatically open with the app interface, You can see demo images below.


![image](https://github.com/user-attachments/assets/300c693a-c7b7-4e57-9bc1-d07fcb171b8b)
![image](https://github.com/user-attachments/assets/86d93fa1-5374-4320-931e-360a8fdd3a1f)
