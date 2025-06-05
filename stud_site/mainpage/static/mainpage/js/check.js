console.log('Работает!');

document.getElementById('checkButton').addEventListener('click', () => {
    const url_addr = document.getElementById('addressInput').value.trim();

    fetch(url_addr)
        .then(response => {
            console.log(
                'Ура! Сервер ответил на ', url_addr,
                response.status,
                response
            );
            if (response.status === 404) {
                        
                console.error(`ошибка! Адреса ${url_addr} не существует!`);
                return null;
            } else {
                return response.text();
            }
        })
        .then(data => {
            if (data !== null) {
                console.log(data);
            }
        })
        .catch(error => {
            console.error(`Ошибка при запросе к ${url_addr}:`, error);
        });
});
