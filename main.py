import discord
from discord.commands import Option
import os
from dotenv import load_dotenv

bot = discord.Bot(intents=discord.Intents.all())

@bot.event
async def on_ready():
    channel = bot.get_channel(975050699446566953)

    await channel.send("**봇이 작동 중 입니다.** 👍")

    print("봇이 작동중입니다. 👍")

@bot.slash_command(description="Get youtube video thumbnail")
async def thumbnail(ctx, video_id: Option(str, "Enter a youtube video ID", required=True), choice: Option(str, "Select a kind", choices=["default", "hqdefault", "sddefault", "maxresdefault"], required=True, default=""), thumbnail_id: Option(str, "Enter a number", choices=["0", "1", "2", "3"], required=False, default="")):

    if thumbnail_id == "":
        if choice == "default":
            embed = discord.Embed()
            embed.set_image(url=f"https://img.youtube.com/vi/{video_id}/default.jpg")
            view = discord.ui.View()
            item = discord.ui.Button(style=discord.ButtonStyle.gray, label="Click to open URL!", url=f"https://img.youtube.com/vi/{video_id}/default.jpg")
            view.add_item(item=item)

            return await ctx.respond(embed = embed, view = view)

        elif choice == "hqdefault":
            embed = discord.Embed()
            embed.set_image(url=f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg")
            view = discord.ui.View()
            item = discord.ui.Button(style=discord.ButtonStyle.gray, label="Click to open URL!", url=f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg")
            view.add_item(item=item)

            return await ctx.respond(embed = embed, view = view)

        elif choice == "sddefault":
            embed = discord.Embed()
            embed.set_image(url=f"https://img.youtube.com/vi/{video_id}/sddefault.jpg")
            view = discord.ui.View()
            item = discord.ui.Button(style=discord.ButtonStyle.gray, label="Click to open URL!", url=f"https://img.youtube.com/vi/{video_id}/sddefault.jpg")
            view.add_item(item=item)

            return await ctx.respond(embed = embed, view = view)

        elif choice == "maxresdefault":
            embed = discord.Embed()
            embed.set_image(url=f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg")
            view = discord.ui.View()
            item = discord.ui.Button(style=discord.ButtonStyle.gray, label="Click to open URL!", url=f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg")
            view.add_item(item=item)

            return await ctx.respond(embed = embed, view = view)

    else:
        if thumbnail_id == "0":
            embed = discord.Embed()
            embed.set_image(url=f"https://img.youtube.com/vi/{video_id}/0.jpg")
            view = discord.ui.View()
            item = discord.ui.Button(style=discord.ButtonStyle.gray, label="Click to open URL!", url=f"https://img.youtube.com/vi/{video_id}/0.jpg")
            view.add_item(item=item)

            return await ctx.respond(embed = embed, view = view)

        elif thumbnail_id == "1":
            embed = discord.Embed()
            embed.set_image(url=f"https://img.youtube.com/vi/{video_id}/1.jpg")
            view = discord.ui.View()
            item = discord.ui.Button(style=discord.ButtonStyle.gray, label="Click to open URL!", url=f"https://img.youtube.com/vi/{video_id}/1.jpg")
            view.add_item(item=item)

            return await ctx.respond(embed = embed, view = view)

        elif thumbnail_id == "2":
            embed = discord.Embed()
            embed.set_image(url=f"https://img.youtube.com/vi/{video_id}/2.jpg")
            view = discord.ui.View()
            item = discord.ui.Button(style=discord.ButtonStyle.gray, label="Click to open URL!", url=f"https://img.youtube.com/vi/{video_id}/2.jpg")
            view.add_item(item=item)

            return await ctx.respond(embed = embed, view = view)

        elif thumbnail_id == "3":
            embed = discord.Embed()
            embed.set_image(url=f"https://img.youtube.com/vi/{video_id}/2.jpg")
            view = discord.ui.View()
            item = discord.ui.Button(style=discord.ButtonStyle.gray, label="Click to open URL!", url=f"https://img.youtube.com/vi/{video_id}/2.jpg")
            view.add_item(item=item)

            return await ctx.respond(embed = embed, view = view)

load_dotenv()
token = os.getenv("TOKEN")
bot.run(token=token)
