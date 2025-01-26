function load_data() {
  fetch("/data")
    .then((response) => response.json())
    .then((data) => {
      for (index = 0; index < data.length; ++index) {
        let div = document.createElement("div");
        let img = document.createElement("img");
        let id = document.createElement("h1");
        let name = document.createElement("h1");
        let amount = document.createElement("h1");
        let price = document.createElement("h1");
        let button = document.createElement("button");
        name.textContent = data[index][4];
        id.textContent = "ID: " + data[index][0];
        amount.textContent = "Осталось: " + data[index][2] + " шт.";
        price.textContent = "Цена: " + data[index][1] + " НейКоинов";
        img.src = "/static/img/" + data[index][3];
        img.alt = "Описание картинки";
        div.className += "plinkImages";
        name.className += "ImgTextBoxes";
        id.className += "ImgTextBoxes";
        amount.className += "ImgTextBoxes";
        price.className += "ImgTextBoxes";
        button.className += "ButtonBuyBox";
        button.textContent = "Купить";
        let container = document.querySelector("#divContainer");
        div.appendChild(img);
        div.appendChild(id);
        div.appendChild(name);
        div.appendChild(amount);
        div.appendChild(price);
        div.append(button);
        container.appendChild(div);
      }
    })
    .catch((error) => console.error("Error:", error));
}

window.onload = function () {
  let w = load_data();
  // converted = '603006669';
  // let replace = document.querySelector("#profileButton");
  // var href = replace.getAttribute("href");
  // console.log(converted);
  // replace.href =("./profile/" + '603006669');
};
function process(selectedItem) {
  const data = JSON.stringify({
    selectedItem,
  });
  $.ajax({
    url: "/shop",
    type: "POST",
    contentType: "application/json",
    data: data,
    success: function (data) {
      console.log(data);
    },
  });
}
let tg = window.Telegram.WebApp; //получаем объект webapp телеграма
tg.expand(); //расширяем на все окно
tg.MainButton.text = "Changed Text"; //изменяем текст кнопки
tg.MainButton.setText("Changed Text1"); //изменяем текст кнопки иначе
tg.MainButton.textColor = "#F55353"; //изменяем цвет текста кнопки
tg.MainButton.color = "#143F6B"; //изменяем цвет бэкграунда кнопки
tg.MainButton.setParams({ color: "#143F6B" }); //так изменяются все параметры
tg.sendData(tg.initDataUnsafe.user.id);

