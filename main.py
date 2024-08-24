import openai
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()


def get_movie_recommendations(genres, favorite_movies):
    # Retrieve the API key from environment variables
    api_key = os.getenv('OPEN_AI_APIKEY')
    openai.api_key = api_key

    prompt = input(
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


def get_user_preferences():
    genres = input("Lütfen favori film türlerinizi virgülle ayırarak girin (örn. Aksiyon, Komedi, Bilim Kurgu): ").split(",")
    favorite_movies = []
    for i in range(3):
        movie = input(f"En sevdiğiniz {i+1}. filmi girin: ")
        favorite_movies.append(movie)
    return genres, favorite_movies


def main():
    genres, favorite_movies = get_user_preferences()
    recommendations = get_movie_recommendations(genres, favorite_movies)
    print("\nFilm Önerileri:\n")
    print(recommendations)

if __name__ == "__main__":
    main()
