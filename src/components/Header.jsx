export default function Header() {
    return (
      <header className="flex justify-between items-center p-4 bg-white shadow">
        <img src="logo.png" alt="Logo" className="h-10" />
        <button>
          <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
          </svg>
        </button>
      </header>
    );
  }
  