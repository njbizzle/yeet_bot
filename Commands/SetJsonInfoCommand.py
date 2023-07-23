from Command import Command
import JsonManager as jm
class SetJsonInfoCommand(Command):
    def __init__(self):
        super().__init__("set_json_value")

    async def run(self, params, message):
        try:
            new_value = int(params[0])
            jm.set_member_value(message.author, message.guild, new_value)
            await message.channel.send(f"value to {new_value}.")
        except:
            await message.channel.send(f"please set to a number")
