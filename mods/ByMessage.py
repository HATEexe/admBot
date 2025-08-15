import disnake
from disnake.ext import commands

messageList = {}

class ByMessage(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description = "Кик/бан пользователя, если у него меньше заданного числа сообщений")
    @commands.contexts(guild = True, bot_dm = False)
    @commands.default_member_permissions(ban_members = True)

    async def bymessage(
            self,
            inter,
            int: int,
            role: disnake.Role,
            toDo: str = commands.Param(name = "operator", choices = ["Бан", "Кик"])
        ):
        await inter.response.defer(with_message = True, ephemeral = True)

        counter = 0
        guild = inter.author.guild

        for channels in guild.channels:
            if channels.type == disnake.ChannelType.text:
                seekTo = guild.get_channel(channels.id)

                async for message in seekTo.history(limit = None):
                    user = guild.get_member(message.author.id)
                    if user != None:
                        for id in user.roles:
                            if id.id == role.id and message.author.bot == False and message.author.id != guild.owner_id:
                                counter = counter + 1
                                messageList[message.author.id] = counter

        if messageList == {}:
            await inter.edit_original_response("Никого не нашел", delete_after = 3.0)
            return

        match toDo:
            case "Бан":
                i = 0
                length = len(messageList)
                keyList = list(messageList.keys())

                while i < length:
                    memberToCheck = keyList[i]
                    memberMessage = messageList.get(memberToCheck)

                    if memberMessage < int:
                        member = guild.get_member(memberToCheck)

                        await member.ban(reason = f"Менее {int} сообщений")
                        await inter.edit_original_response(f"Забанил {member.mention}", delete_after = 3.0)

                    i = i + 1

            case "Кик":
                i = 0
                length = len(messageList)
                keyList = list(messageList.keys())

                while i < length:
                    memberToCheck = keyList[i]
                    memberMessage = messageList.get(memberToCheck)

                    if memberMessage < int:
                        member = guild.get_member(memberToCheck)

                        await member.kick(reason = f"Менее {int} сообщений")
                        await inter.edit_original_response(f"Кикнул {member.mention}", delete_after = 3.0)

                    i = i + 1

def setup(bot: commands.Bot):
    bot.add_cog(ByMessage(bot))