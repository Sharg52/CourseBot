start = (", это бот для <b>прогнозов на матчи по Dota 2 🥳</b>\n"
         "Всего пользователей {BotUser.objects.count()}\n"
         "Вы можете позвать друзей по своей ссылке:\n"
         "[Ваша ссылка...](https://t.me/{(await bot.me).username}?start={user.id})\n\n"
         "Посмотрите матчи на сегодня: /matches")

help = ("Вы можете:\n"
        "1)Посмотреть команды для управления: /help\n\n"
        "2)Матчи на сегодня: /matches\n\n"
        "3)Посмотреть статистику: /statistics(не работает)\n\n"
        "4)Приглашённые друзей: /referrals\n\n"
        "5)Ваша ссылка для приглашений: /link")
link = ("Вы можете позвать друзей по своей ссылке:\n"
        "https://t.me/{(await bot.me).username}?start={BotUser.objects.get(tg_id=msg_or_clb.chat.id).id}")
