from llama_cpp import Llama
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import LlamaCpp
from langchain.vectorstores.faiss import FAISS

import logging
import sys

import discord
from discord import app_commands

import configparser

config = configparser.ConfigParser()
config.read('.config')

DISCORD_TOKEN = config.get('discord_key', 'key')

intents = discord.Intents.default()#適当に。
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

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

@client.event
async def on_ready():
    print("bot ready")
    await tree.sync()

@tree.command(name="ask",description="AIからあげ先生への質問を入力してください。")
async def test_command(interaction: discord.Interaction, text:str="test"):
    await interaction.response.defer(thinking=True)
    response = qa_chain.run("日本語で答えてください。" + text)
    await interaction.followup.send(text + 'の質問の回答は' + response)

client.run(DISCORD_TOKEN)
