# import os
# import discord
# import aiohttp
# import json
# import openai
# from dotenv import load_dotenv

# load_dotenv()
# # Set up OpenAI API credentials
# openai.api_key = os.getenv("OPENAI_API_KEY")
# # Set up Discord bot client

# intents = discord.Intents.default()
# # intents.members = True

# client = discord.Client(intents=intents)

# # Define endpoint and parameters for Image API
# endpoint = "https://api.openai.com/v1/images/generations"
# model = "image-alpha-001"
# size = "512x512"

# async def generate_image(query):
#     async with aiohttp.ClientSession() as session:
#         # Set up headers and data for API request
#         headers = {
#             "Content-Type": "application/json",
#             "Authorization": f"Bearer {openai.api_key}",
#         }
#         data = {
#             "model": model,
#             "query": query,
#             "num_images": 1,
#             "size": size,
#         }

#         # Make the API request using the requests library
#         async with session.post(endpoint, headers=headers, data=json.dumps(data)) as response:
#             # Parse the response JSON and retrieve the generated image URL
#             result = await response.json()
#             generated_image_url = result["data"][0]["url"]
#             return generated_image_url

# @client.event
# async def on_ready():
#     print("Bot is ready.")

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
    
#     if message.content.startswith('!ping'):
#         await message.channel.send('Pong!')

#     if message.content.startswith("!generate_image"):
#         query = message.content.split("!generate_image ")[1]

#         # Use asyncio to generate image asynchronously
#         generated_image_url = await generate_image(query)

#         # Send the generated image URL as a message in the Discord channel
#         await message.channel.send(generated_image_url, "hi")

# client.run(os.getenv("DISCORD_BOT_TOKEN"))
