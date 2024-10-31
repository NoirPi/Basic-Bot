import twitchio
from twitchio.ext import commands
from datetime import datetime



class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def _ping(self, ctx):
        """Ping the Bot"""
        clientping = (datetime.now() - ctx.message.created_at).total_seconds() * 1000
        calc = await ctx.send("Bot Latency ``{round(self.bot.latency * 1000)}``\nClient Latency ``{clientping}``\n")


def setup(bot):
    bot.add_cog(Commands(bot))
