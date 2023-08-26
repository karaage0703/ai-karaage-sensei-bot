from transformers import AutoTokenizer
from auto_gptq import AutoGPTQForCausalLM
import logging
import sys

import discord
from discord import app_commands

import configparser

config = configparser.ConfigParser()
config.read('.config')

DISCORD_TOKEN = config.get('discord_key', 'key')

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, force=True)

quantized_model_dir = "dahara1/weblab-10b-instruction-sft-GPTQ"
model_basename = "gptq_model-4bit-128g"

tokenizer = AutoTokenizer.from_pretrained(quantized_model_dir)

model = AutoGPTQForCausalLM.from_quantized(
        quantized_model_dir,
        model_basename=model_basename,
        use_safetensors=True,
        device="cuda:0")


@client.event
async def on_ready():
    print("bot ready")
    await tree.sync()

@tree.command(name="ask",description="AIからあげ先生への質問を入力してください。")
async def test_command(interaction: discord.Interaction, text:str="test"):
    await interaction.response.defer(thinking=True)
    tokens = tokenizer(text, return_tensors="pt").to("cuda:0").input_ids
    output = model.generate(input_ids=tokens, max_new_tokens=100, do_sample=True, temperature=0.8)
    response = tokenizer.decode(output[0])
    await interaction.followup.send(text + 'の質問の回答は' + response)

client.run(DISCORD_TOKEN)
