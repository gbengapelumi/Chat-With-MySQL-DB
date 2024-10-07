from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.utilities import SQLDatabase
import urllib.parse
import streamlit as st


def init_database(
    user: str, password: str, host: str, port: str, database: str
) -> SQLDatabase:
    password_encoded = urllib.parse.quote_plus(password)  # Encode special characters
    db_uri = (
        f"mysql+mysqlconnector://{user}:{password_encoded}@{host}:{port}/{database}"
    )
    return SQLDatabase.from_uri(db_uri)


if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(
            content="Hello!, I am a SQL assistant. Ask me anything about your database"
        ),
    ]


load_dotenv()

st.set_page_config(page_title="Chat with MySQL", page_icon=":speech_balloon")

st.title("Chat with MySQL")

with st.sidebar:
    st.subheader("Settings")
    st.write(
        "This is a simple chat application using MySQL. Connect to the database and start chatting."
    )

    st.text_input("Host", value="localhost", key="Host")
    st.text_input("Port", value="3306", key="Port")
    st.text_input("User", value="root", key="User")
    st.text_input("Password", type="password", value="Gbenga@99", key="Password")
    st.text_input("Database", value="Chinook", key="Database")

    if st.button("Connect"):
        with st.spinner("Connecting to database"):
            db = init_database(
                st.session_state["User"],
                st.session_state["Password"],
                st.session_state["Host"],
                st.session_state["Port"],
                st.session_state["Database"],
            )
            st.session_state.db = db
            st.success("Connected to Database!")

for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.markdown(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)

st.text_input("Type a message...")
