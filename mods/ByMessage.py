import disnake
from disnake.ext import commands

class ByMessage(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description = "Кик/бан пользователя по заданному количеству сообщений")
    @commands.contexts(guild = True, bot_dm = False)
    @commands.default_member_permissions(ban_members = True)

    async def bymessage(
            self,
            inter,
            member: disnake.User,
            int: int,
            toDo: str = commands.Param(name = "operator", choices = ["Бан", "Кик"])
        ):
        counter = 0
        guild = inter.author.guild

        for channels in guild.channels:
            if channels.type == disnake.ChannelType.text:
                seekTo = guild.get_channel(channels.id)
                async for message in seekTo.history(limit = None):
                    if message.author == member:
                        counter += 1

        match toDo:
            case "Бан":
                if counter < int:
                    await member.ban(reason = f"Менее {int} сообщений")
                    await inter.send("Забанил", ephemeral=True, delete_after = 3.0)
                elif counter >= int:
                    await inter.send("Не забанил", ephemeral=True, delete_after = 3.0)

            case "Кик":
                if counter < int:
                    await member.kick(reason = f"Менее {int} сообщений")
                    await inter.send("Кикнул", ephemeral=True, delete_after = 3.0)
                elif counter >= int:
                    await inter.send("Не кикнул", ephemeral=True, delete_after = 3.0)

def setup(bot: commands.Bot):
    bot.add_cog(ByMessage(bot))