import discord
from discord.ext import commands
# class AddRemoveRoleButton(discord.ui.View):
#     def __init__(self, role: discord.Role):
#         super().__init__(timeout=None)
#         self.role = role
#         self.add_role_button.label = f"Add Role {self.role.name}"
#         self.remove_role_button.label = f"Remove Role {self.role.name}"
#
#     @discord.ui.button(style=discord.ButtonStyle.blurple, custom_id="yeet_bot:role_button:add_role")
#     async def add_role_button(self, interaction: discord.Interaction, button: discord.ui.Button):
#         button.label = "test"
#         user = interaction.user
#         if self.role in interaction.user.roles:
#             await interaction.response.send_message(f"{user.name} already has {self.role.name}.", ephemeral=True)
#         else:
#             await user.add_roles(self.role)
#             await interaction.response.send_message(f"Gave {user.name} role {self.role.name}.", ephemeral=True)
#
#     @discord.ui.button(style=discord.ButtonStyle.red, custom_id="yeet_bot:role_button:remove_role")
#     async def remove_role_button(self, interaction: discord.Interaction, button: discord.ui.Button):
#         user = interaction.user
#         if self.role in interaction.user.roles:
#             await user.remove_roles(self.role)
#             await interaction.response.send_message(f"Removed role {self.role.name} from {user.name}.", ephemeral=True)
#         else:
#             await interaction.response.send_message(f"{user.name} does not have {self.role.name} already.", ephemeral=True)
class AddRemoveRoleButton(discord.ui.View):
    def __init__(self, roles):
        self.role = roles
        super().__init__(timeout=None)

        row = 0
        for role in roles:
            row += 1
            self.add_item(AddRoleButton(role, row=row))
            self.add_item(RemoveRoleButton(role, row=row))

class AddRoleButton(discord.ui.Button):
    def __init__(self, role, label=None, style=None, row=None):
        self.role = role

        label_ = f"Add Role {self.role.name}" if label is None else label
        style_ = discord.ButtonStyle.green if style is None else style

        super().__init__(label=label_, style=style_, row=row)

    async def callback(self, interaction: discord.Interaction):
        user = interaction.user
        if self.role in user.roles:
            await user.remove_roles(self.role)
            await interaction.response.send_message(f"Role {self.role.name} has already been added.", ephemeral=True)
        else:
            await user.add_roles(self.role)
            await interaction.response.send_message(f"Gave {user.name} role {self.role.name}.", ephemeral=True)
class RemoveRoleButton(discord.ui.Button):
    def __init__(self, role, label=None, style=None, row=None):
        self.role = role

        label_ = f"Remove Role {self.role.name}" if label is None else label
        style_ = discord.ButtonStyle.red if style is None else style

        super().__init__(label=label_, style=style_, row=row)

    async def callback(self, interaction: discord.Interaction):
        user = interaction.user
        if self.role in user.roles:
            await user.remove_roles(self.role)
            await interaction.response.send_message(f"Removed role {self.role.name} from {user.name}.", ephemeral=True)
        else:
            await interaction.response.send_message(f"Role {self.role.name} has aleady been removed.", ephemeral=True)