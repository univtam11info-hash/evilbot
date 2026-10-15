import discord
from discord.ext import commands
import os

# إعداد الصلاحيات الأساسية
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# فئة الأزرار التفاعلية للتحقق
class VerificationView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="🛡️ Blue Team & Reversers", 
        style=discord.ButtonStyle.danger, 
        custom_id="blue_team_btn"
    )
    async def blue_team_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        role = discord.utils.get(interaction.guild.roles, name="blue team")
        if role:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                "⚡ **تم اختيار مسار المتقدمين!**\nيرجى التواصل مع الأدمن لإثبات الخبرة أو تقديم المشاريع الحقيقية لتعيينك رسمياً في مشاريع الفريق.", 
                ephemeral=True
            )

    @discord.ui.button(
        label="👤 Beginner & Member", 
        style=discord.ButtonStyle.primary, 
        custom_id="member_btn"
    )
    async def member_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        role = discord.utils.get(interaction.guild.roles, name="members")
        if role:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                "🌱 **مرحباً بك معنا!**\nتم إعطاؤك رتبة الأعضاء، وستتعلم معنا من الصفر لبناء فريق موحد وقوي.", 
                ephemeral=True
            )

@bot.event
async def on_ready():
    # تسجيل الأزرار لتظل تعمل حتى بعد إعادة تشغيل البوت
    bot.add_view(VerificationView())
    print(f"[+] Bot Online: {bot.user.name} | Ready for Evil Reversers")

# أمر لإرسال لوحة التقييم في القناة
@bot.command()
@commands.has_permissions(administrator=True)
async def setup_rules(ctx):
    embed = discord.Embed(
        title="🔐 نظام تحديد الرتب | Evil Reversers",
        description=(
            "أهلاً بك في المقر الرئيسي! اختر رتبتك بناءً على مستواك وخبرتك بالتحديد:\n\n"
            "🔴 **🛡️ Blue Team & Reversers:**\n"
            "> إذا عندك خبرة وتقدر تعاونا بمشاريع حقيقية (يتطلب منك إثباتها للأدمن).\n\n"
            "🔵 **👤 Beginner & Member:**\n"
            "> إذا حاب تتعلم معانا من الصفر ونكون فريق واحد موحد."
        ),
        color=discord.Color.red()
    )
    embed.set_footer(text="Evil Reversers System • اختر بالضغط على الزر المناسب أسفله")
    
    await ctx.send(embed=embed, view=VerificationView())

# قراءة التوكن من متغيرة البيئة للتأمين
TOKEN = os.getenv("DISCORD_TOKEN")
if __name__ == "__main__":
    bot.run(TOKEN)