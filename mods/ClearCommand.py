import disnake
from disnake.ext import commands

class ClearCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description = "Удаление заданного количества сообщений (по умолчанию: 10)")
    @commands.contexts(guild = True, bot_dm = False)
    @commands.default_member_permissions(manage_messages = True)

    async def clear(self, inter, int: int = 10):
        await inter.channel.purge (limit = int)

        await inter.send("Чат очищен", ephemeral=True, delete_after = 1.0)

def setup(bot: commands.Bot):
    bot.add_cog(ClearCommand(bot))