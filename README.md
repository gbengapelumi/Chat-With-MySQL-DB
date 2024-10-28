# Chat with MySQL

A conversational AI application built with Streamlit that enables users to interact with a MySQL database using natural language queries. This project uses LangChain, SQLDatabase, and the Groq model to translate user questions into SQL queries and provides natural language responses based on the data retrieved.

## Features

- Natural language querying for MySQL databases
- Generates SQL queries from user questions
- Uses LangChain's ChatGroq model for generating SQL and natural language responses
- Maintains conversational context through chat history

## Prerequisites

- Python 3.8+
- MySQL server (ensure you have access to a MySQL instance)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2. **Set up a virtual environment (recommended):**

    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure environment variables:**

    - Create a `.env` file in the root directory and set your OpenAI and Groq API keys (if required for your models):
    ```bash
    OPENAI_API_KEY=your_openai_api_key
    GROQ_API_KEY=your_groq_api_key
    ```

## Usage

1. **Run the application:**

    ```bash
    streamlit run app.py
    ```

2. **Set up MySQL connection:**
   - Enter your MySQL server details in the sidebar (host, port, user, password, and database name).
   - Click the **Connect** button to establish a connection to your database.

3. **Ask questions about your database:**
   - Type natural language questions in the chat input field. The app will generate an SQL query, retrieve the result from your database, and display a natural language response.

## Example

Here’s a simple example to get you started:

1. **Connect to a database:** Enter database details, e.g., `localhost`, `3306`, `root`, `password`, and `Chinook` as the database.
2. **Ask a question:** Type `Show the top 3 artists with the most tracks`.
3. **Receive a response:** The app will generate and execute an SQL query to fetch the answer and respond in natural language.

## Project Structure

- `app.py` - Main application file containing Streamlit and LangChain components.
- `requirements.txt` - List of all Python dependencies.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [LangChain](https://github.com/hwchase17/langchain) - For providing powerful tools for language model integration.
- [Streamlit](https://streamlit.io) - For making it easy to build interactive data applications.
