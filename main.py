import discord
from discord.ext import commands
import google.generativeai as genai

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

token = "MTE2NzUxMjk4OTAyOTY0MjM1MA.Gpmkrk.yVEbJXmpcWS3Ztl5pPR7FitdL3_ZlnVPOFYQz4"
Gkey = "AIzaSyAQvbKwm8_ehobg5V0vxnFuFHIR5YIPv2g"

bot = commands.Bot(command_prefix='/', intents=intents)

genai.configure(api_key=Gkey)

generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)



@bot.event
async def on_ready():
    print("We are ready broo")


@bot.event
async def on_message(message):
    if message.content.startswith('/working'):
        await message.channel.send("Yeah Good Afternoon !!")

    await bot.process_commands(message)


@bot.command()
async def gen(ctx, *args):
    message = ' '.join(args)
    await ctx.send("generating....")
    await ctx.send("here")

@bot.command()
async def talk(ctx, *args):
    message = ' '.join(args)
    convo = model.start_chat(history=[])
    convo.send_message(message)
    output = convo.last.text
    await ctx.send(output)

bot.run(token,root_logger=True)
