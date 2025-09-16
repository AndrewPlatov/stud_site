// document.addEventListener('DOMContentLoaded', () => {
// // window.addEventListener('load', () => {
//     const form = document.getElementById('question-form');
//     console.log('Js')
//     // Проверяем, есть ли форма на странице
//     if (!form) return;

//     form.addEventListener('submit', (e) => {
//         e.preventDefault(); // Предотвращаем отправку формы по умолчанию

//         // Получаем выбранные чекбоксы
//         const checkboxes = document.querySelectorAll('input[type="checkbox"][name="answers"]:checked');
//         const selectedAnswers = Array.from(checkboxes).map(cb => cb.value);

//         // Проверка: есть ли выбранные ответы
//         if (selectedAnswers.length === 0) {
//             alert('Пожалуйста, выберите хотя бы один ответ.');
//             return;
//         }

//         // Можно добавить подтверждение
//         if (confirm(`Вы выбрали ответы: ${selectedAnswers.join(', ')}. Отправить?`)) {
//             // Отправляем форму
//             form.submit();
//         }
//     });
// });

const questions = [
    // 1
    {
        question: "Укажите цифры, на месте которых должны стоять запятые." ,
        question: "Заядлые путешественники (1) ищущие (2) что посмотреть в России самого необычного и даже мистического (3) непременно должны спуститься в Кунгурскую пещеру. Сегодня это место (4) самое известное уральское чудо. Температура здесь не поднимается выше +8 ºC (5) поэтому (6) отправившиеся на досуге полюбоваться сталактитами и сталагмитами (7) уральцы (8) частенько дрожат здесь от холода (9) если забыли надеть перед спуском тёплую куртку и шапку.",
        type: "text-input", // вопрос с текстовым вводом
        correctAnswer: ["12359"] // Правильный ответ
    },
    // 2
    {
        text: "Укажите цифры, на месте которых должны стоять запятые." ,
        question: "Кремль (1) самая древняя часть столицы России (2) расположенная на берегу Москвы-реки. Именно здесь (3) на Боровицком холме (4) ещё в середине XII века князь Юрий Долгорукий основал свою усадьбу-крепость (5) впервые упомянутую в 1147 году. Примечательно (6) что стены и башни Кремля были воздвигнуты из красного кирпича (7) на месте прежних белокаменных в конце XV века (8) а колокольня Ивана Великого (9) самое высокое здание на Руси тех времён.",
        type: "text-input", // вопрос с текстовым вводом
        correctAnswer: ["12359"] // Правильный ответ
    },
    // 3
    {
        text: "Укажите цифры, на месте которых должны стоять запятые." ,
        question: "Только вечером в весеннем лесу начинаешь понимать (1) что такое настоящая тишина (2) ибо то (3) что мы обычно принимаем за неё (4) есть постоянный и привычный шум. Он как фон радиоволн и помех в наушниках (5) на который не обращаешь внимания (6) улавливая нужный сигнал. Тишина весеннего неодетого леса наполнена голосами птиц (7) шорохом подсыхающей листвы и (8) падающих с ветвей (9) кáпель.",
        type: "text-input", // вопрос с текстовым вводом
        correctAnswer: ["12359"] // Правильный ответ
    },
    // 4
    {
        text: "Укажите цифры, на месте которых должны стоять запятые." ,
        question: "Дерево (1) материал недолговечный (2) а время и пожары сделали своё дело. Именно из-за них (3) до наших дней не дошли многие выдающиеся сооружения (4) о которых мы знаем только из летописей. При этом центральные районы России (5) почти не сохранили памятники деревянного зодчества. И только некоторые области Поволжья (6) Урала (7) Сибири и Севера (8) донесли до нас образцы этого высокого искусства.",
        type: "text-input", // вопрос с текстовым вводом
        correctAnswer: ["12359"] // Правильный ответ
    },
    // 5
    {
        text: "Укажите цифры, на месте которых должны стоять запятые." ,
        question: "Для изучения русской деревянной архитектуры XVI–XVII веков (1) мы располагаем немногочисленными (2) но довольно разнообразными и з о б р а з и т ел ь н ы м и и с т оч н и ка м и (3) р и с у н ка м и и н о с т р а н н ы х путешественников (4) планами (5) отдельных городов и селений (6) которые составлялись при строительстве новых городов-крепостей (7) или при перестройке старых (8) а также для разбора самых сложных земельных тяжб.",
        type: "text-input", // вопрос с текстовым вводом
        correctAnswer: ["12359"] // Правильный ответ
    },
    // 6
    {
        text: "Укажите цифры, на месте которых должны стоять запятые." ,
        question: "Госудáрственная Третьякóвская галерéя (1) московский художественный музей (2) основанный в 1856 году купцом Павлом Третьяковым (3) происходившим из небогатого купеческого рода. Коллекционер хотел создать национальный музей (4) в котором (5) были бы представлены работы русских художников. Сегодня (6) экспозиция галереи насчитывает более 180000 предметов (7) и включает в себя картины (8) скульптуры и изделия из драгоценных металлов (9) созданные с XI по XX век.",
        type: "text-input", // вопрос с текстовым вводом
        correctAnswer: ["12359"] // Правильный ответ
    },
    // 7
    {
        text: "Укажите цифры, на месте которых должны стоять запятые." ,
        question: "Кремль (1) самая древняя часть столицы России (2) расположенная на берегу Москвы-реки. Именно здесь (3) на Боровицком холме (4) ещё в середине XII века князь Юрий Долгорукий основал свою усадьбу-крепость (5) впервые упомянутую в 1147 году. Примечательно (6) что стены и башни Кремля были воздвигнуты из красного кирпича (7) на месте прежних белокаменных в конце XV века (8) а колокольня Ивана Великого (9) самое высокое здание на Руси тех времён.",
        type: "text-input", // вопрос с текстовым вводом
        correctAnswer: ["12359"] // Правильный ответ
    },
    // 8
    {
        text: "Укажите цифры, на месте которых должны стоять запятые." ,
        question: "Кремль (1) самая древняя часть столицы России (2) расположенная на берегу Москвы-реки. Именно здесь (3) на Боровицком холме (4) ещё в середине XII века князь Юрий Долгорукий основал свою усадьбу-крепость (5) впервые упомянутую в 1147 году. Примечательно (6) что стены и башни Кремля были воздвигнуты из красного кирпича (7) на месте прежних белокаменных в конце XV века (8) а колокольня Ивана Великого (9) самое высокое здание на Руси тех времён.",
        type: "text-input", // вопрос с текстовым вводом
        correctAnswer: ["12359"] // Правильный ответ
    },
    // 9
    {
        text: "Укажите цифры, на месте которых должны стоять запятые." ,
        question: "Кремль (1) самая древняя часть столицы России (2) расположенная на берегу Москвы-реки. Именно здесь (3) на Боровицком холме (4) ещё в середине XII века князь Юрий Долгорукий основал свою усадьбу-крепость (5) впервые упомянутую в 1147 году. Примечательно (6) что стены и башни Кремля были воздвигнуты из красного кирпича (7) на месте прежних белокаменных в конце XV века (8) а колокольня Ивана Великого (9) самое высокое здание на Руси тех времён.",
        type: "text-input", // вопрос с текстовым вводом
        correctAnswer: ["12359"] // Правильный ответ
    },
    // 10
    {
        text: "Укажите цифры, на месте которых должны стоять запятые." ,
        question: "Кремль (1) самая древняя часть столицы России (2) расположенная на берегу Москвы-реки. Именно здесь (3) на Боровицком холме (4) ещё в середине XII века князь Юрий Долгорукий основал свою усадьбу-крепость (5) впервые упомянутую в 1147 году. Примечательно (6) что стены и башни Кремля были воздвигнуты из красного кирпича (7) на месте прежних белокаменных в конце XV века (8) а колокольня Ивана Великого (9) самое высокое здание на Руси тех времён.",
        type: "text-input", // вопрос с текстовым вводом
        correctAnswer: ["12359"] // Правильный ответ
    },
    // 11
    {
        text: "Укажите цифры, на месте которых должны стоять запятые." ,
        question: "Кремль (1) самая древняя часть столицы России (2) расположенная на берегу Москвы-реки. Именно здесь (3) на Боровицком холме (4) ещё в середине XII века князь Юрий Долгорукий основал свою усадьбу-крепость (5) впервые упомянутую в 1147 году. Примечательно (6) что стены и башни Кремля были воздвигнуты из красного кирпича (7) на месте прежних белокаменных в конце XV века (8) а колокольня Ивана Великого (9) самое высокое здание на Руси тех времён.",
        type: "text-input", // вопрос с текстовым вводом
        correctAnswer: ["12359"] // Правильный ответ
    },
    // 12
    {
        text: "Укажите цифры, на месте которых должны стоять запятые." ,
        question: "Кремль (1) самая древняя часть столицы России (2) расположенная на берегу Москвы-реки. Именно здесь (3) на Боровицком холме (4) ещё в середине XII века князь Юрий Долгорукий основал свою усадьбу-крепость (5) впервые упомянутую в 1147 году. Примечательно (6) что стены и башни Кремля были воздвигнуты из красного кирпича (7) на месте прежних белокаменных в конце XV века (8) а колокольня Ивана Великого (9) самое высокое здание на Руси тех времён.",
        type: "text-input", // вопрос с текстовым вводом
        correctAnswer: ["12359"] // Правильный ответ
    },
    // 13
    {
        text: "Укажите цифры, на месте которых должны стоять запятые." ,
        question: "Кремль (1) самая древняя часть столицы России (2) расположенная на берегу Москвы-реки. Именно здесь (3) на Боровицком холме (4) ещё в середине XII века князь Юрий Долгорукий основал свою усадьбу-крепость (5) впервые упомянутую в 1147 году. Примечательно (6) что стены и башни Кремля были воздвигнуты из красного кирпича (7) на месте прежних белокаменных в конце XV века (8) а колокольня Ивана Великого (9) самое высокое здание на Руси тех времён.",
        type: "text-input", // вопрос с текстовым вводом
        correctAnswer: ["12359"] // Правильный ответ
    },
    // 14
    {
        text: "Укажите цифры, на месте которых должны стоять запятые." ,
        question: "Кремль (1) самая древняя часть столицы России (2) расположенная на берегу Москвы-реки. Именно здесь (3) на Боровицком холме (4) ещё в середине XII века князь Юрий Долгорукий основал свою усадьбу-крепость (5) впервые упомянутую в 1147 году. Примечательно (6) что стены и башни Кремля были воздвигнуты из красного кирпича (7) на месте прежних белокаменных в конце XV века (8) а колокольня Ивана Великого (9) самое высокое здание на Руси тех времён.",
        type: "text-input", // вопрос с текстовым вводом
        correctAnswer: ["12359"] // Правильный ответ
    },
    // 15
    {
        text: "Укажите цифры, на месте которых должны стоять запятые." ,
        question: "Кремль (1) самая древняя часть столицы России (2) расположенная на берегу Москвы-реки. Именно здесь (3) на Боровицком холме (4) ещё в середине XII века князь Юрий Долгорукий основал свою усадьбу-крепость (5) впервые упомянутую в 1147 году. Примечательно (6) что стены и башни Кремля были воздвигнуты из красного кирпича (7) на месте прежних белокаменных в конце XV века (8) а колокольня Ивана Великого (9) самое высокое здание на Руси тех времён.",
        type: "text-input", // вопрос с текстовым вводом
        correctAnswer: ["12359"] // Правильный ответ
    },
];



let currentQuestionIndex = 0;
let score = 0;
let results = [];
let attempts = 2;
let timer;
let timeLeft = 15 * 60;

function loadQuestion() {
    const questionContainer = document.getElementById('question');
    const answersContainer = document.getElementById('answers');
    const userAnswerInput = document.getElementById('user-answer');

    const currentQuestion = questions[currentQuestionIndex];

    // Устанавливаем текст вопроса
    questionContainer.textContent = currentQuestion.question;

    // Очищаем предыдущие ответы
    while (answersContainer.firstChild) {
        answersContainer.removeChild(answersContainer.firstChild);
    }

    if (currentQuestion.type === 'multiple-choice') {
        userAnswerInput.style.display = 'none';

        currentQuestion.answers.forEach((answer) => {
            const button = document.createElement('button');
            button.textContent = answer;
            button.onclick = () => selectAnswer(button, answer);
            answersContainer.appendChild(button);
        });

    } else if (currentQuestion.type === 'text-input') {
        userAnswerInput.style.display = 'block';
        userAnswerInput.value = '';
    }
}

let selectedAnswers = [];

function selectAnswer(button, answer) {
    // Проверяем, был ли уже выбран этот ответ
    if (selectedAnswers.includes(answer)) {
        // Если да, то убираем его из выбранных
        selectedAnswers = selectedAnswers.filter(selected => selected !== answer);
        button.classList.remove('selected'); // Убираем выделение с кнопки
    } else {
        // Если нет, добавляем его в выбранные
        selectedAnswers.push(answer);
        button.classList.add('selected'); // Выделяем кнопку
    }
}

document.getElementById('submit-answer').onclick = function() {
    const userAnswer = document.getElementById('user-answer').value.trim();

    const currentQuestion = questions[currentQuestionIndex];

    if (currentQuestion.type === 'text-input') {
         if (userAnswer === '') {
             alert("Пожалуйста, введите ваш ответ.");
             return; 
         }

         checkTextInputAnswer(userAnswer);

     } else if (currentQuestion.type === 'multiple-choice') {
         if (selectedAnswers.length === 0) { 
             alert("Пожалуйста, выберите хотя бы один вариант ответа.");
             return; 
         }

         checkMultipleChoiceAnswers();
     }
};

function checkTextInputAnswer(userAnswer) {
     const currentQuestion = questions[currentQuestionIndex];
     
     const isCorrect = currentQuestion.correctAnswer.includes(userAnswer.toLowerCase());

     results.push({
         question: currentQuestion.question,
         userAnswers: [userAnswer],
         correctAnswers: currentQuestion.correctAnswer,
         isCorrect
     });

     if (isCorrect) score++;

     nextQuestion();
}

function checkMultipleChoiceAnswers() {
     const currentQuestion = questions[currentQuestionIndex];
     
     const correctAnswersSet = new Set(currentQuestion.correctAnswer);
     const selectedAnswersSet = new Set(selectedAnswers);
     
     let isCorrect = true;
     
     if (selectedAnswersSet.size !== correctAnswersSet.size || ![...selectedAnswersSet].every(answer => correctAnswersSet.has(answer))) {
         isCorrect = false;
     }

     results.push({
         question: currentQuestion.question,
         userAnswers: [...selectedAnswers],
         correctAnswers: currentQuestion.correctAnswer,
         isCorrect
     });

     if (isCorrect) score++;

     selectedAnswers = [];
     nextQuestion();
}

function calculateGrade(score) {
   if (score === questions.length) return 5; // Все ответы правильные
   if (score >= questions.length * 0.8) return 4; // От 80% правильных ответов
   if (score >= questions.length * 0.6) return 3; // От 60% правильных ответов
   if (score >= questions.length * 0.4) return 2; // От 40% правильных ответов
   return 1; // Менее 40%
}

function nextQuestion() {
   currentQuestionIndex++;
   
   if (currentQuestionIndex < questions.length) {
       loadQuestion();
   } else {
       showFinalResult();
   }
}

function showFinalResult() {
   clearInterval(timer);

   const questionContainer = document.getElementById('question-container');
   const resultContainer = document.getElementById('result');
    
   while(resultContainer.firstChild){
      resultContainer.removeChild(resultContainer.firstChild); 
   }

   questionContainer.style.display = 'none';
    
   const titleElement = document.createElement('h2');
   titleElement.textContent = 'Тест завершен!';
   
   const scoreElement = document.createElement('p');
   scoreElement.textContent = `Ваш результат: ${score} из ${questions.length}.`;
   
   const gradeElement = document.createElement('p');
   gradeElement.textContent = `Ваша оценка: ${calculateGrade(score)}`;
   
   resultContainer.appendChild(titleElement);
   resultContainer.appendChild(scoreElement);
   resultContainer.appendChild(gradeElement);

   results.forEach((result, index) => {

       const blockClass=result.isCorrect?'correct':'incorrect';
       
       const blockDiv=document.createElement('div');
       blockDiv.className=`question-block ${blockClass}`;
       
       const questionHeader=document.createElement('h3');
       questionHeader.textContent=`Вопрос ${index + 1}:`;
       
       const questionText=document.createElement('p');
       questionText.textContent=`Вопрос: ${result.question}`;
       
       const userText=document.createElement('p');
       userText.textContent=`Ваш ответ: ${result.userAnswers.join(', ')}`;
       
       const correctText=document.createElement('p');
       correctText.textContent=`Правильный ответ: ${result.correctAnswers.join(', ')}`;
       
       const correctnessText=document.createElement('p');
       correctnessText.textContent=`${result.isCorrect ? 'Правильно' : 'Неправильно'}`;
       
       blockDiv.appendChild(questionHeader);
       blockDiv.appendChild(questionText);
       blockDiv.appendChild(userText);
       blockDiv.appendChild(correctText);
       blockDiv.appendChild(correctnessText);

       resultContainer.appendChild(blockDiv);
       
       resultContainer.appendChild(document.createElement('hr'));
   });
    
   attempts--;
    
   if(attempts > 0){
       const retryButton=document.createElement('button');
       retryButton.textContent=`Попробовать еще раз (${attempts} попытки осталось)`;
       retryButton.onclick=restartTest;
       
       resultContainer.appendChild(retryButton);
   } else{
       resultContainer.appendChild(document.createTextNode("Вы исчерпали все попытки."));
   }
}

function restartTest() { 
   currentQuestionIndex=0;
   score=0;
   results=[];
   selectedAnswers=[];
   
   loadTimer(); 
   
   loadQuestion(); 

}

function startTimer() { 
   timer=setInterval(() => { 
       timeLeft--; 

       let minutes=Math.floor(timeLeft/60); 
       let seconds=timeLeft%60; 

       document.getElementById("timer").textContent=`Осталось времени:${minutes}:${seconds<10?"0":""}${seconds}`; 

       if(timeLeft<=0){ 
           clearInterval(timer); 
           alert("Время вышло!"); 
           showFinalResult(); 
       } 

   },1000); 
}

function loadTimer(){
   startTimer(); 
   
   let minutes=Math.floor(timeLeft/60); 
   let seconds=timeLeft%60; 

   document.getElementById("timer").textContent=`Осталось времени:${minutes}:${seconds<10?"0":""}${seconds}`; 
}

loadTimer(); 

loadQuestion();