from Command import Command
class TestCommand(Command):
    def __init__(self):
        super().__init__("test_command")

    async def run(self, params, message):
        await message.channel.send("test")