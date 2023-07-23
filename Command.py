class Command:
    def __init__(self, command_name, role_whitelist=None, roles_blacklist=None):
        # require certain fields
        if not command_name:
            raise NotImplementedError("please pass in command_name value.")

        self.command_name = command_name
        self.role_whitelist = role_whitelist
        self.roles_blacklist = roles_blacklist

    def check(self, command_name, message=None):
        if command_name != self.command_name:
            return False

        can_run = True # defaults to true if roles not specified

        if self.role_whitelist != None:
            can_run = False # if there is a whitelist default it to false

            for role in self.role_whitelist:
                if role in message.author.roles:
                    can_run = True

        if self.roles_blacklist != None:
            for role in self.roles_blacklist:
                if role in message.author.roles:
                    can_run = False

        return can_run


    async def run(self, params, message):
        raise NotImplementedError("please override the run method")