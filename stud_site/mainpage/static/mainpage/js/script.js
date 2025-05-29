document.addEventListener('DOMContentLoaded', () => {
// window.addEventListener('load', () => {
    const form = document.getElementById('question-form');
    console.log('Js')
    // Проверяем, есть ли форма на странице
    if (!form) return;

    form.addEventListener('submit', (e) => {
        e.preventDefault(); // Предотвращаем отправку формы по умолчанию

        // Получаем выбранные чекбоксы
        const checkboxes = document.querySelectorAll('input[type="checkbox"][name="answers"]:checked');
        const selectedAnswers = Array.from(checkboxes).map(cb => cb.value);

        // Проверка: есть ли выбранные ответы
        if (selectedAnswers.length === 0) {
            alert('Пожалуйста, выберите хотя бы один ответ.');
            return;
        }

        // Можно добавить подтверждение
        if (confirm(`Вы выбрали ответы: ${selectedAnswers.join(', ')}. Отправить?`)) {
            // Отправляем форму
            form.submit();
        }
    });
});