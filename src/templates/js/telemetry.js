const cteElement = document.getElementById("cte");
const speedElement = document.getElementById("speed");
const imageElement = document.getElementById("image");

const socket = new WebSocket("ws://localhost:8082/telemetry/ws");

socket.onopen = (event) => {
    console.log("WebSocket connection established:", event);

    // Вы можете отправить начальные запросы или данные здесь
};

socket.onmessage = async (event) => {
    const data = event.data;
    if (typeof data === 'string') {
        // Если данные являются строкой, это, возможно, JSON.
        // Обработайте их как JSON.
        const parsedData = JSON.parse(data);
        if (parsedData.cte !== undefined && parsedData.speed !== undefined) {
            cteElement.textContent = `Отклонение от траектории: ${parsedData.cte}`;
            speedElement.textContent = `Скорость: ${parsedData.speed}`;
        }
    } else if (data instanceof Blob) {
        // Если данные - это Blob, это изображение.
        // Отобразите изображение.
        const blob = new Blob([data], { type: 'image/jpeg' }); // Замените 'image/jpeg' на нужный MIME-тип изображения
        imageElement.src = URL.createObjectURL(blob);
    }
};

socket.onclose = (event) => {
    if (event.wasClean) {
        console.log(`Closed cleanly, code=${event.code}, reason=${event.reason}`);
    } else {
        console.error(`Connection died`);
    }
};

socket.onerror = (error) => {
    console.error(`WebSocket Error: ${error}`);
};
