import discord
from discord.ext import commands


from RoleCustomButtons import AddRemoveRoleButton
class ReactionRoleTestCog(commands.Cog):
    def __init__(self, yeet_bot):
        self.yeet_bot = yeet_bot

    # @commands.command(name="role_set_add_remove")
    # @commands.has_permissions() # https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions
    # async def role_set_add_remove(self, context: commands.Context, *args):
    #     role = None
    #     for roleID in args:
    #         roleID = int(roleID[3: len(roleID)-1])
    #         for guildRole in context.guild.roles:
    #             if guildRole.id == roleID:
    #                 role = guildRole
    #                 break
    #
    #         if role == None:
    #             await context.send("Please send a valid role")
    #
    #         await context.send(f"Add or Remove {role.name}.", view=AddRemoveRoleButton(role))
    @commands.command(name="button_test")
    @commands.has_permissions() # https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions
    async def role_set_choose(self, context: commands.Context, *args):
        roles = []
        for roleID in args:
            roleID = int(roleID[3: len(roleID)-1])
            for guildRole in context.guild.roles:
                if guildRole.id == roleID:
                    roles.append(guildRole)
                    break

        print("message sent")
        await context.send(f"role_set_choose", view=AddRemoveRoleButton(roles))


    # @commands.command(name="role_set_choose")
    # @commands.has_permissions() # https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions
    # async def role_set_add_remove(self, context: commands.Context, role1, role2):
    #     role = None
    #     for roleID in args:
    #         roleID = int(roleID[3 : len(roleID)-1])
    #         for guildRole in context.guild.roles:
    #             if guildRole.id == roleID:
    #                 role = guildRole
    #                 break
    #
    #         if role == None:
    #             await context.send("Please send a valid role")
    #
    #         await context.send(f"Add or Remove {role.name}.", view=RoleButton(role))

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        await payload.interaction.send_message(
            f"{payload.member} reacted with {payload.emoji}",
            ephemeral=True
        )
async def setup(yeet_bot):
    await yeet_bot.add_cog(ReactionRoleTestCog(yeet_bot))
