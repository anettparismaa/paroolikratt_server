async function postData(url = "", data = {}) {
  const response = await fetch(url, {
    method: "POST",
    cache: "no-cache",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
  return response.json();
}

async function checkPassword() {
  const password = document.getElementById("passwordInput").value;
  const resultHeading = document.getElementById("result-heading");
  const recLink = document.getElementById("reccomendation-link");
  const background = document.getElementById("results");

  document.body.classList.toggle("loading")
  document.getElementById("passwordInput").value = "";
  const response = await postData("https://localhost/submissions/", {
    content: password,
  });

  if (response.leaked) {
    background.setAttribute(
      "style",
      "background-image: linear-gradient(rgba(225, 237, 244, 1), rgba(245, 180, 0, 0.5), rgba(236, 87, 50, 1)"
    );
    resultHeading.innerText =
      "Oh häda! Parool leiti lekkinud paroolide andmebaasist!";
    recLink.innerText = "Vaata soovitusi tugeva parooli loomiseks!";
  } else {
    background.setAttribute(
      "style",
      "background-image: linear-gradient(rgba(225, 237, 244, 1), rgba(103, 204, 142, 1), rgba(4, 191, 191, 1))"
    );
    resultHeading.innerText = "Parooli ei leitud ühestki andmebaasist!";
    recLink.innerText = "Vaata soovitusi tugeva parooli loomiseks!";
  }

  if (response.dangerous) {
    background.setAttribute(
      "style",
      "background-image: linear-gradient(rgba(225, 237, 244, 1), rgba(245, 180, 0, 0.5), rgba(236, 87, 50, 1)"
    );
    resultHeading.innerText =
      "Oh häda! Parool leiti ebaturvaliste paroolide andmebaasist!";
    recLink.innerText = "Vaata soovitusi tugeva parooli loomiseks!";
  }
  document.body.classList.toggle("loading")
}

async function upperCase() {
  const capitalLetter = document.getElementById("capital-letter");
  const passphrase = document.getElementById("passpharse-button").textContent;
  try {
    if (capitalLetter.checked) {
      const response = await postData("http://localhost/uppercase/", {
        value: document.getElementById("passpharse-button").textContent,
        number: "true",
      });
      document.getElementById("passpharse-button").textContent =
        response.phrase_value;
    }

    if (!capitalLetter.checked) {
      document.getElementById("passpharse-button").textContent =
        passphrase.toLowerCase();
    }
  } catch (error) {
    console.error(error);
  }
}

async function copyText() {
  const passphrase = document.getElementById("passpharse-button").textContent;
  navigator.clipboard.writeText(passphrase);
}

async function regenerate() {
  const inputlenght = document.getElementById("input-lenght");
  const inputnr = document.getElementById("input-numbers");
  const response = await postData("http://localhost/generator/", {
    value: inputlenght.value,
    number: inputnr.value,
  });
  document.getElementById("passpharse-button").textContent =
    response.phrase_value;
  upperCase();
}

async function loadElements() {
  const inclength = document.getElementById("increment-lenght");
  const declenght = document.getElementById("decrement-lenght");
  const incnr = document.getElementById("increment-numbers");
  const decnr = document.getElementById("decrement-numbers");

  regenerate();

  inclength.addEventListener("click", () => {
    const inputlenght = document.getElementById("input-lenght");
    if (inputlenght.value < 10) {
      inputlenght.value++;
    }
  });

  declenght.addEventListener("click", () => {
    const inputnr = document.getElementById("input-numbers");
    const inputlenght = document.getElementById("input-lenght");

    if (inputnr.value > 1 && inputnr.value >= inputlenght.value) {
      inputnr.value--;
    }

    if (inputlenght.value > 1) {
      inputlenght.value--;
    }
  });

  incnr.addEventListener("click", () => {
    const inputnr = document.getElementById("input-numbers");
    const inputlenght = document.getElementById("input-lenght");
    if (inputnr.value < Math.min(10, inputlenght.value)) {
      inputnr.value++;
    }
  });

  decnr.addEventListener("click", () => {
    const inputnr = document.getElementById("input-numbers");
    if (inputnr.value > 0) {
      inputnr.value--;
    }
  });
}
