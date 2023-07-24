import discord
from discord.ext import commands
class RoleButton(discord.ui.View):
    def __init__(self, role: discord.Role):
        super().__init__(timeout=None)
        self.role = role

    @discord.ui.button(label=f"Remove/Add Role", style=discord.ButtonStyle.blurple)
    async def role_button_click(self, interaction: discord.Interaction, button: discord.ui.Button):
        user = interaction.user
        if self.role in interaction.user.roles:
            await user.remove_roles(self.role)
            await interaction.response.send_message(f"Removed role {self.role.name} from {user.name}.", ephemeral=True)
        else:
            await user.add_roles(self.role)
            await interaction.response.send_message(f"Gave {user.name} role {self.role.name}.", ephemeral=True)
class ReactionRoleTestCog(commands.Cog):
    def __init__(self, yeet_bot):
        self.yeet_bot = yeet_bot

    @commands.command("set_roles")
    async def set_roles(self, context: commands.Context):
        roleNames = ["role 1", "role 2", "role 3"]
        await context.send("Message lol", view=RoleButton(discord.utils.get(context.guild.roles,name=roleNames[0])))

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        await payload.interaction.send_message(
            f"{payload.member} reacted with {payload.emoji}",
            ephemeral=True
        )
async def setup(yeet_bot):
    await yeet_bot.add_cog(ReactionRoleTestCog(yeet_bot))
