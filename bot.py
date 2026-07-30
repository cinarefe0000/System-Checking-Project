import discord
from discord.ext import commands
import psutil
import datetime

# Botun erişim izinleri
intents = discord.Intents.default()
intents.message_content = True  # Sohbet mesajlarını okuyabilmek için şarttır

#ünlem ile başlayacak
bot = commands.Bot(command_prefix="!", intents=intents)
@bot.event
async def on_ready():
    print(f"{bot.user} olarak giriş yapıldı! Bot aktif.")


# !sistem yazınca bu komut çalışacak
@bot.command()
async def sistem(ctx):
    # 1. Parametre: cpu
    cpu_kullanim = psutil.cpu_percent(interval=1)

    # 2. Parametre: Kullanılan ram
    ram_kullanim = psutil.virtual_memory().percent

    # 3. Parametre: C: diskindeki boş alan
    disk_bos = psutil.disk_usage("/").free // (1024**3)

    # 4. YENİ PARAMETRE: Sistemin Açılış Zamanı
    # psutil.boot_time() bilgisayarın açıldığı anın zaman damgasını verir yazıyor internette
    # datetime ile bunu okunabilir tarih/saat formatına çevirdim
    acilis_zamani_raw = psutil.boot_time()
    acilis_zamani = datetime.datetime.fromtimestamp(acilis_zamani_raw).strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    # Sohbet ekranına gönderilecek mesaj olacak
    mesaj = (
        f"📊 **Sistem Durumu Raporu**\n"
        f"• **CPU Kullanımı:** %{cpu_kullanim}\n"
        f"• **RAM Kullanımı:** %{ram_kullanim}\n"
        f"• **Boş Disk Alanı:** {disk_bos} GB\n"
        f"• **Sistem Açılış Tarihi (Yeni Özellik):** {acilis_zamani}"
    )

    # discorda gönder
    await ctx.send(mesaj)
bot.run("TOKEN")