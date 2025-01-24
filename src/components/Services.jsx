

export default function ContactForm() {
    return (
      <section className="p-8 bg-gray-100">
        <h2 className="text-2xl font-bold text-center text-green-700">Получить консультацию</h2>
        <form className="mt-6 max-w-md mx-auto space-y-4">
          <input type="text" placeholder="Ваше имя" className="w-full p-2 border rounded" />
          <input type="text" placeholder="Ваш телефон" className="w-full p-2 border rounded" />
          <select className="w-full p-2 border rounded">
            <option>Выберите услугу</option>
            <option>Консультация</option>
          </select>
          <button className="w-full bg-green-600 text-white p-2 rounded">Отправить</button>
        </form>
        

      </section>
      
    );
  }
  