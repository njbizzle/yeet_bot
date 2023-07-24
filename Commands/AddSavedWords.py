from Command import Command
import JsonManager as jm
class AddSavedWords(Command):
    def __init__(self):
        super().__init__("add_words")

    async def run(self, params, message):
        jm.add_member_saved_words(message.author, message.guild, params)
        await message.channel.send(f"saved words: {', '.join(params)}")
