from Command import Command
import JsonManager as jm
class GetJsonInfoCommand(Command):
    def __init__(self):
        super().__init__("get_json")

    async def run(self, params, message):
        member_info = jm.get_member_info(message.author, message.guild)
        print([str(saved_word) for saved_word in member_info["member_saved_words"]])
        await message.channel.send(f'''
        {message.author},
    your stored value is {member_info["member_value"]}.
    your saved words are: {", ".join(member_info["member_saved_words"])}
        ''')