import disnake
from disnake.ext import commands

class ByRole(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description = "Кик/бан пользователя по заданной роли")
    @commands.contexts(guild = True, bot_dm = False)
    @commands.default_member_permissions(ban_members = True)

    async def byrole(
            self,
            inter,
            role: disnake.Role,
            reason: str,
            toDo: str = commands.Param(name = "operator", choices = ["Бан", "Кик"])
            ):
        guild = inter.author.guild

        result = False

        for id in guild.members:
            member = id
            memberRole = id.roles
            for id in memberRole:
                if role.id == id.id:
                    match toDo:
                        case "Бан":
                            await member.ban(reason = reason)
                            await inter.send("Забанил", ephemeral = True, delete_after = 3.0)

                            result = True
                        case "Кик":
                            await member.kick(reason = reason)
                            await inter.send("Кикнул", ephemeral = True, delete_after = 3.0)

                            result = True

        if result == False:
            await inter.send("Никого не нашел", ephemeral = True, delete_after = 3.0)

def setup(bot: commands.Bot):
    bot.add_cog(ByRole(bot))