from llama_cpp import Llama
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import LlamaCpp
from langchain.vectorstores.faiss import FAISS

import logging
import sys


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, force=True)

embeddings = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-large")
index = FAISS.load_local('storage', embeddings)

llm = LlamaCpp(
    # model_path="./llama-2-7b-chat.ggmlv3.q8_0.bin",
    model_path="./llama-2-7b-chat.ggmlv3.q4_0.bin",
    # input={
    #     "max_tokens": 32,
    #     "stop": ["System:", "User:", "Assistant:", "\n"],
    # },
    verbose=True, n_ctx=2048,
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=index.as_retriever(search_kwargs={"k": 4}),
    verbose=True,
)

while True:
    input_text = input('> ')

    print("karaage_sensei:", qa_chain.run("日本語で答えてください。" + input_text))
