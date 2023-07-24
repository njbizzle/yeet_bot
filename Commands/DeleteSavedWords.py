from Command import Command
import JsonManager as jm
class DeleteSavedWords(Command):
    def __init__(self):
        super().__init__("delete_words")

    async def run(self, params, message):
        member_info = jm.get_member_info(message.author, message.guild)

        saved_words_to_delete = []

        # if all are deleted
        if params[0] == "-all":
            saved_words_to_delete = member_info["member_saved_words"]
        else: # otherwise look for what words in params that can be deleted
            for saved_word in member_info["member_saved_words"]:
                if saved_word in params:
                    saved_words_to_delete.append(saved_word)

        jm.delete_member_saved_words(message.author, message.guild, saved_words_to_delete)
        await message.channel.send(f"deleted words: {', '.join(saved_words_to_delete)}")
