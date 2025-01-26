function load_data() {
  fetch("/data")
    .then((response) => response.json())
    .then((data) => {

      for (index = 0; index < data.length; ++index) {
        let div = document.createElement("div");
        let img = document.createElement("img");
        let name = document.createElement("h1");
        let button = document.createElement("button")
        name.textContent = "Цена: "+data[index][1];
        img.src = "/static/img/" + data[index][3];

        img.alt = "Описание картинки";
        div.className +="plinkImages";
        name.className +="ImgTextBoxes";
        button.className+= "ButtonBuyBox";
        button.textContent = "Купить";
        
        let container = document.querySelector("#divContainer");
        div.appendChild(img);
        div.appendChild(name);
        div.append(button);
        
        container.appendChild(div);
      }
      
    })
    .catch((error) => console.error("Error:", error));
}

window.onload = function () {
  w = load_data();
};
