import discord
from discord.ext import commands
import logic  # import file logic.py
from config import TOKEN

intents = discord.Intents.default()
intents.message_content = True  
bot = commands.Bot(command_prefix="!", intents=intents)


# ================= BUTTON VIEW =================
class MenuView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="1️⃣ Cara Pembelian", style=discord.ButtonStyle.primary)
    async def pembelian(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(logic.get_pembelian(), ephemeral=True)

    @discord.ui.button(label="2️⃣ Status Pesanan", style=discord.ButtonStyle.success)
    async def status(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(logic.get_status(), ephemeral=True)

    @discord.ui.button(label="3️⃣ Batalkan Pesanan", style=discord.ButtonStyle.danger)
    async def batal(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(logic.get_batal(), ephemeral=True)

    @discord.ui.button(label="4️⃣ Pesanan Rusak", style=discord.ButtonStyle.secondary)
    async def rusak(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(logic.get_rusak(), ephemeral=True)

    @discord.ui.button(label="5️⃣ Dukungan Teknis", style=discord.ButtonStyle.danger)
    async def teknis(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(logic.get_teknis(), ephemeral=True)

    @discord.ui.button(label="6️⃣ Ubah Metode Pengiriman", style=discord.ButtonStyle.success)
    async def pengiriman(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(logic.get_pengiriman(), ephemeral=True)
        
@bot.command()
async def start(ctx):
    embed = discord.Embed(
        title="🛍️ Semua Bisa Kamu Beli",
        description=(
            "Selamat datang di toko kami!\n\n"
            "Ada yang bisa kami bantu?\n\n"
            "Silakan pilih salah satu menu di bawah ini 👇"
        ),
        color=0x3498db
    )

    await ctx.send(embed=embed, view=MenuView())
bot.run(TOKEN)