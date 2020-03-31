import discord
from discord.ext import commands


class Commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ping")
    async def _ping(self, ctx):
        """Ping the Bot"""
        calc = await ctx.send(embed=discord.Embed(description="Ping"))
        clientping = (calc.created_at - ctx.message.created_at).total_seconds() * 1000
        await calc.edit(embed=discord.Embed(
            description=f"Bot Latency ``{round(self.bot.latency * 1000)}``\nClient Latency ``{clientping}``\n",
            delete_after=10))


def setup(bot: commands.Bot):
    bot.add_cog(Commands(bot))
