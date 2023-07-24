import discord
from discord.ext import commands
import JsonManager as jm
class TestJsonCog(commands.Cog):
    def __init__(self, yeet_bot):
        self.yeet_bot = yeet_bot

    @commands.command(name='set_value')
    async def set_member_value(self, context, value=None):
        try:
            jm.set_member_value(context.author, context.guild, int(value))
            await context.send(f"value to {value}.")
        except:
            await context.send(f"please set to a number.")

    @commands.command(name='get_info')
    async def get_member_info(self, context):
        member_info = jm.get_member_info(context.author, context.guild)
        await context.send(
            f"{context.author},\n" +
            f"your stored value is {member_info['member_value']}.\n" +
            f"your saved words are: {(', '.join(member_info['member_saved_words']) if member_info['member_saved_words'] != [] else ' none')}."
        )

    @commands.command(name='add_words')
    async def add_member_saved_words(self, context, *args):
        jm.add_member_saved_words(context.author, context.guild, args)
        await context.send(f"saved words: {', '.join(args)}")

    @commands.command(name='delete_words')
    async def remove_member_saved_words(self, context, *args):
        member_info = jm.get_member_info(context.author, context.guild)

        saved_words_to_delete = []

        # if all are deleted
        if args[0] == "-all":
            saved_words_to_delete = member_info["member_saved_words"]
        else: # otherwise look for what words in params that can be deleted
            for saved_word in member_info["member_saved_words"]:
                if saved_word in args:
                    saved_words_to_delete.append(saved_word)

        jm.delete_member_saved_words(context.author, context.guild, saved_words_to_delete)
        await context.send(f"deleted words: {', '.join(saved_words_to_delete)}")
async def setup(yeet_bot):
    await yeet_bot.add_cog(TestJsonCog(yeet_bot))