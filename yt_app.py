import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.document_loaders import youtube
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.chains import RetrievalQA

# Load environment variables from .env
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

st.title("YouTube Assistant - GenAI + Gemini")

# User Inputs
youtube_url = st.text_input("Enter YouTube Video URL:")
question = st.text_area("Ask a question about the video:")

if st.button("Submit") and youtube_url and question:
    with st.spinner("Processing..."):
        try:
            # Step 1: Fetch transcript using LangChain's YoutubeLoader
            loader = youtube.YoutubeLoader.from_youtube_url(youtube_url, add_video_info=True)
            documents = loader.load()

            # Step 2: Split transcript into manageable chunks
            splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
            docs = splitter.split_documents(documents)

            # Step 3: Set up Gemini LLM and Embedding
            llm = ChatGoogleGenerativeAI(
                model="gemini-pro",
                google_api_key=GOOGLE_API_KEY,
                temperature=0.2
            )
            embedding = GoogleGenerativeAIEmbeddings(google_api_key=GOOGLE_API_KEY)

            # Step 4: Create vectorstore and RetrievalQA Chain
            vectordb = FAISS.from_documents(docs, embedding=embedding)
            retriever = vectordb.as_retriever()
            qa_chain = RetrievalQA.from_chain_type(
                llm=llm,
                chain_type="stuff",
                retriever=retriever
            )

            # Step 5: Run QA
            result = qa_chain({"query": question})

            # Output
            st.subheader("Answer:")
            st.write(result['result'])

            # (Optional) Show the fetched transcript
            with st.expander("Show video transcript"):
                for chunk in docs:
                    st.write(chunk.page_content)

        except Exception as e:
            st.error(f"Error: {e}")

st.markdown(
    "This assistant uses LangChain's YouTube transcript loader, Google's Gemini API, and answers your questions based on the video content."
)