import discord
from discord.ext import commands


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Checks the bot latency."""
        calculation = await ctx.send('Pinging...')
        clientping = (calculation.created_at - ctx.message.created_at).total_seconds() * 1000
        
        # editing the message to show the client latency and ping
        await calc.edit(embed=discord.Embed(description=f'Bot Latency: ``{round(self.bot.latency * 1000)}``ms\n Client Latency: ``{clientping}``'))


def setup(bot):
    """Load the Commands Cog"""
    bot.add_cog(Commands(bot))
