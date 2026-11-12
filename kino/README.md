# Kino Telegram Bot

Telegram kino bot. Ushbu loyiha `pyTelegramBotAPI` (telebot) kutubxonasida yozilgan.

## Lokal ishga tushirish

1. `pip install -r requirements.txt`
2. `.env.example` nusxasini `.env` deb nomlang va `BOT_TOKEN` qiymatini kiriting.
3. Windows PowerShell'da muhit o'zgaruvchisini kiriting yoki Render Environment'dan foydalaning.
4. `python main.py`

Kod `.env` faylini avtomatik o'qimaydi. Lokal ishlatishda tokenni terminal orqali `BOT_TOKEN` muhit o'zgaruvchisi qilib bering.

## Render'ga joylash

1. Loyihani GitHub repository'ga yuboring.
2. Render'da **New → Blueprint** orqali repository'ni ulang (yoki **New → Background Worker** yarating).
3. `render.yaml` konfiguratsiyasi worker, build/start buyruqlari va doimiy diskni belgilaydi.
4. Render Environment bo'limida `BOT_TOKEN` ni BotFather'dan olingan yangi token bilan to'ldiring. `ADMINS` qiymati admin Telegram ID'lari vergul bilan ajratilgan ko'rinishda bo'ladi.
5. Deploy qiling va Logs bo'limida `Bot muvaffaqiyatli ishga tushdi` yozuvini tekshiring.

`render.yaml` dagi `starter` worker va 1 GB persistent disk pullik resurslardir. Bepul Web Service bot uchun to'g'ri tanlov emas: u uxlab qolishi mumkin, Background Worker esa uzluksiz polling uchun mo'ljallangan.

## Ma'lumotlar bazasi

`kino_bot.db` repoda faqat kino katalogi seed ma'lumotlari bilan saqlanadi; foydalanuvchilar jadvali seed arxivga kiritilmagan. Render diskiga birinchi ishga tushishda shu katalog ko'chiriladi. Keyingi o'zgarishlar `/var/data/kino_bot.db` da saqlanadi. Diskni o'chirmang, aks holda bazadagi yangilanishlar yo'qolishi mumkin.

## Xavfsizlik

Bot tokenini kodga yoki GitHub'ga joylamang. Agar token oldin kod ichida bo'lgan bo'lsa, BotFather'da `/revoke` qilib yangisini oling.
