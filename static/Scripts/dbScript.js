let tg = window.Telegram.WebApp;

// tg.initDataUnsafe.user.id // уникальный идентификатор пользователя
// tg.initDataUnsafe.user.isBot // бот ли пользователь (true/false)
// tg.initDataUnsafe.user.first_name // имя пользователя
// tg.initDataUnsafe.user.last_name // "фамилия" пользователя
// tg.initDataUnsafe.user.username // username пользователя
// tg.initDataUnsafe.user.language_code // код языка пользователя

document.getElementById(idBox).innerHTML = tg.initDataUnsafe.user.id;
