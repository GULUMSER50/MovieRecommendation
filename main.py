import openai
from dotenv import load_dotenv
import os
import streamlit as st

# Load environment variables from the .env file
load_dotenv()

def get_movie_recommendations(genres, favorite_movies):
    # Retrieve the API key from environment variables
    api_key = os.getenv('OPEN_AI_APIKEY')
    openai.api_key = api_key

    prompt = (
        f"Bu kullanıcının favori film türleri: {', '.join(genres)}.\n"
        f"Ve en sevdiği 3 film: {', '.join(favorite_movies)}."
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200
    )

    return response['choices'][0]['message']['content'].strip()

def main():
    st.title("Film Öneri Sistemi")

    genres = st.text_input("Lütfen favori film türlerinizi virgülle ayırarak girin (örn. Aksiyon, Komedi, Bilim Kurgu):")
    favorite_movies = []
    for i in range(3):
        movie = st.text_input(f"En sevdiğiniz {i+1}. filmi girin:")

        if movie:
            favorite_movies.append(movie)

    if st.button("Öneri Al"):
        if genres and len(favorite_movies) == 3:
            genres_list = genres.split(",")
            recommendations = get_movie_recommendations(genres_list, favorite_movies)
            st.write("\nFilm Önerileri:\n")
            st.write(recommendations)
        else:
            st.write("Lütfen tüm alanları doldurun.")

if __name__ == "__main__":
    main()