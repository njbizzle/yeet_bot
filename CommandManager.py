# command file imports
from Commands.TestCommand import TestCommand

from Commands.GetJsonInfoCommand import GetJsonInfoCommand
from Commands.SetJsonInfoCommand import SetJsonInfoCommand
from Commands.AddSavedWords import AddSavedWords
from Commands.DeleteSavedWords import DeleteSavedWords


class CommandManager:
    def __init__(self):
        # ----- ADD ALL COMMANDS HERE -----
        self.commands = [
            TestCommand(),

            GetJsonInfoCommand(),
            SetJsonInfoCommand(),
            AddSavedWords(),
            DeleteSavedWords()
        ]
        # ----- ^^^^^^^^^^^^^^^^^^^^^ -----
        self.command_prefix = "!"
    def add_command(self, command):
        self.commands.append(command)
    async def on_message(self, message):
        if message.content[0] != self.command_prefix:
            return

        command_message = message.content.split(" ")
        command_name = command_message[0][1:]

        for command in self.commands:
            if command.check(command_name, message):
                await command.run(command_message[1:], message)
