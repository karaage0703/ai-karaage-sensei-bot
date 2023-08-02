import logging
import sys

from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import LlamaCpp
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.faiss import FAISS
from langchain.llms import OpenAIChat


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, force=True)

# ドキュメントの読み込み
with open("analysis_normalized_tweet_1.txt", encoding="utf-8") as f:
    test_all = f.read()

with open("analysis_normalized_tweet_2.txt", encoding="utf-8") as f:
    test_all += f.read()

with open("blog_text.txt", encoding="utf-8") as f:
    test_all += f.read()

# チャンクの分割
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=514,
    chunk_overlap=20,
)
texts = text_splitter.split_text(test_all)

# チャンクの確認
print(len(texts))
for text in texts:
    print(text[:10].replace("\n", "\\n"), ":", len(text))

# インデックスの作成
index = FAISS.from_texts(
    texts=texts,
    embedding=HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-large"),
)

index.save_local("storage")
