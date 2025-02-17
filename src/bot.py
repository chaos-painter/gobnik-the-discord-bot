import discord
from discord.ext import commands
from discord import app_commands

import asyncio

from data import *
from utils import *



intents = discord.Intents.all()

class Client(commands.Bot):
  def __init__(self):
    super().__init__(command_prefix="!", intents=intents)

  async def setup_hook(self):
    guild = discord.Object(id=DEV_SERVER_ID)
    self.tree.copy_global_to(guild=guild)
    await self.tree.sync(guild=guild)
    print("Slash commands synced.")

  async def on_ready(self):
    print(f"Logged in as {self.user}")

  # async def on_message(self, message):
  #   print(f"{message.author}: {message.content}")


client = Client()
frames = load_text_frames()

# Badapple command
@client.tree.command(name='badapple', description="Plays Bad Apple")
async def play_badapple(interaction: discord.Interaction):
  await interaction.response.defer()
  for frame in frames:
    await interaction.followup.send(frame)
    asyncio.sleep(0.1)



# Image to ASCII command
@client.tree.command(name='ascii', description="Converts images from links to ascii.")
async def image_to_ascii(interaction: discord.Interaction, url: str, width: int, mode: str):
  image = download_image(url)
  if mode == "block":
    charset = ASCII_CHARS_BLOCK
  elif mode == "regular":
    charset = ASCII_CHARS
  prepare_image(image, new_width=width, charset=charset)

  await interaction.response.send_message(file=discord.File(f"{DATA_PATH}/ascii_image.txt"))


client.run(BOT_TOKEN)