export default function Features() {
    return (
      <section className="p-4 sm:p-8 flex flex-col items-center">
        {/* Фото */}
        <div className="w-full max-w-md sm:max-w-4xl">
          <img
            src="photo.png"
            alt="Features"
            className="w-full h-auto rounded-lg shadow-md"
          />
        </div>
  
        {/* Текст о компании */}
        <div className="mt-6">
          <p className="text-green-600 font-bold text-sm">О компании</p>
          <h2 className="text-2xl font-bold text-gray-800 mt-2">
            Огромный опыт на сельскохозяйственных культурах
          </h2>
          <p className="text-gray-600 mt-4">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
            minim veniam, quis nostrud exercitation ullamco laboris.
          </p>
          <p className="text-gray-600 mt-4">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua.
          </p>
        </div>
  
        {/* Список */}
        <ul className="mt-6 space-y-6 max-w-md sm:max-w-4xl text-sm sm:text-base">
          <li className="text-center">
            <span className="text-green-600 font-bold text-3xl sm:text-4xl block">
              600
            </span>
            <p className="text-gray-600 mt-2">Lorem ipsum dolor sit amet.</p>
          </li>
          <li className="text-center">
            <span className="text-green-600 font-bold text-3xl sm:text-4xl block">
              600
            </span>
            <p className="text-gray-600 mt-2">Lorem ipsum dolor sit amet.</p>
          </li>
          <li className="text-center">
            <span className="text-green-600 font-bold text-3xl sm:text-4xl block">
              600
            </span>
            <p className="text-gray-600 mt-2">Lorem ipsum dolor sit amet.</p>
          </li>
        </ul>
  
        {/* Кнопка "Связаться с нами" */}
        <div className="mt-8">
          <button className="px-6 py-3 bg-green-600 text-white font-bold rounded-lg shadow-md hover:bg-green-700 transition duration-300">
            Связаться с нами
          </button>
        </div>
  
        {/* Заголовок "Наши Услуги" */}
        <div className="text-center mt-16">
          <h2 className="text-2xl font-bold text-gray-800 mt-2">
            Наши <span className="text-green-600">Услуги</span>
          </h2>
          <p className="text-gray-600 mt-4 max-w-2xl mx-auto">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua.
          </p>
        </div>
  
        {/* Блок "Сопровождение" */}
        <div className="mt-12 bg-gray-100 p-6 rounded-lg shadow-md text-center max-w-md">
          {/* Иконка */}
          <div className="flex justify-center items-center mb-4">
            <img
              src="body.png"
              alt="Icon"
              className="h-12 w-12"
            />
          </div>
          
          {/* Заголовок и текст */}
          <h3 className="text-lg font-bold text-gray-800 mb-2">Сопровождение</h3>
          <p className="text-gray-600 text-sm">
            Официально представляем интересы Вашей компании, избавляя от
            необходимости личного участия в рабочих процессах. Мы готовы взять на
            себя координацию вопросов.
          </p>
          
          {/* Кнопка */}
          <div className="mt-6 flex justify-center">
            <button className="bg-green-600 text-white rounded-full w-12 h-12 flex items-center justify-center hover:bg-green-700">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-6 w-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M9 5l7 7-7 7"
                />
              </svg>
            </button>
          </div>
        </div>

         {/* Блок "Сопровождение" */}
         <div className="mt-12 bg-gray-100 p-6 rounded-lg shadow-md text-center max-w-md">
          {/* Иконка */}
          <div className="flex justify-center items-center mb-4">
            <img
              src="body.png"
              alt="Icon"
              className="h-12 w-12"
            />
          </div>
          
          {/* Заголовок и текст */}
          <h3 className="text-lg font-bold text-gray-800 mb-2">Сопровождение</h3>
          <p className="text-gray-600 text-sm">
            Официально представляем интересы Вашей компании, избавляя от
            необходимости личного участия в рабочих процессах. Мы готовы взять на
            себя координацию вопросов.
          </p>
          
          {/* Кнопка */}
          <div className="mt-6 flex justify-center">
            <button className="bg-green-600 text-white rounded-full w-12 h-12 flex items-center justify-center hover:bg-green-700">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-6 w-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M9 5l7 7-7 7"
                />
              </svg>
            </button>
          </div>
        </div>

         {/* Блок "Сопровождение" */}
         <div className="mt-12 bg-gray-100 p-6 rounded-lg shadow-md text-center max-w-md">
          {/* Иконка */}
          <div className="flex justify-center items-center mb-4">
            <img
              src="body.png"
              alt="Icon"
              className="h-12 w-12"
            />
          </div>
          
          {/* Заголовок и текст */}
          <h3 className="text-lg font-bold text-gray-800 mb-2">Сопровождение</h3>
          <p className="text-gray-600 text-sm">
            Официально представляем интересы Вашей компании, избавляя от
            необходимости личного участия в рабочих процессах. Мы готовы взять на
            себя координацию вопросов.
          </p>
          
          {/* Кнопка */}
          <div className="mt-6 flex justify-center">
            <button className="bg-green-600 text-white rounded-full w-12 h-12 flex items-center justify-center hover:bg-green-700">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-6 w-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M9 5l7 7-7 7"
                />
              </svg>
            </button>
          </div>
        </div>

         {/* Блок "Сопровождение" */}
         <div className="mt-12 bg-gray-100 p-6 rounded-lg shadow-md text-center max-w-md">
          {/* Иконка */}
          <div className="flex justify-center items-center mb-4">
            <img
              src="body.png"
              alt="Icon"
              className="h-12 w-12"
            />
          </div>
          
          {/* Заголовок и текст */}
          <h3 className="text-lg font-bold text-gray-800 mb-2">Сопровождение</h3>
          <p className="text-gray-600 text-sm">
            Официально представляем интересы Вашей компании, избавляя от
            необходимости личного участия в рабочих процессах. Мы готовы взять на
            себя координацию вопросов.
          </p>
          
          {/* Кнопка */}
          <div className="mt-6 flex justify-center">
            <button className="bg-green-600 text-white rounded-full w-12 h-12 flex items-center justify-center hover:bg-green-700">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-6 w-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M9 5l7 7-7 7"
                />
              </svg>
            </button>
          </div>
        </div>
      </section>
    );
  }
  