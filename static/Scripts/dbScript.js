

// tg.initDataUnsafe.user.id // уникальный идентификатор пользователя
// tg.initDataUnsafe.user.isBot // бот ли пользователь (true/false)
// tg.initDataUnsafe.user.first_name // имя пользователя
// tg.initDataUnsafe.user.last_name // "фамилия" пользователя
// tg.initDataUnsafe.user.username // username пользователя
// tg.initDataUnsafe.user.language_code // код языка пользователя
let tg = window.Telegram.WebApp;
document.getElementById('idBox').innerHTML = Telegram.WebApp.initDataUnsafe.userId;;
document.write(Telegram.WebApp.initDataUnsafe.userId);
