# Film Recommendation System

This project is a film recommendation system that uses OpenAI's GPT-3.5-turbo model to suggest movies based on user preferences. The application is built with Python and Streamlit.

## Description

The application prompts users to input their favorite film genres and movies. Based on this input, it generates movie recommendations using the OpenAI API.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/GulumserEskiturk/film-recommendation-system.git
    cd film-recommendation-system
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project root and add your OpenAI API key:
    ```dotenv
    OPEN_AI_APIKEY=your_openai_api_key
    ```

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run main.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Enter your favorite film genres and movies to get recommendations.
