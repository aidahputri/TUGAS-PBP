/** @type {import('tailwindcss').Config} */
module.exports = {
  // darkMode: 'class',
  content: [
    './**/templates/**/*.html',
    './**/templates/*.html'
  ],
  theme: {
    extend: {
      fontFamily: {
        poppins: ['Poppins', 'sans-serif'],
        ponzu: ['Ponzu']
      },
      colors: {
        'purple-1': '#553EAE',
        'purple-2': '#4B4358',
        'purple-3': '#7C48D5',
        'purple-4': '#8468F5',
        'purple-5': '#9E3EAE',
        'pink-1': '#C15C69',
        'pink-2': '#FDB8BA',
        'pink-3': '#EC74E7',
        'pink-4': '#FDB4B6',
        'pink-5': '#FEE0E0',
        'pink-6': '#ECCBD9',
        'gray-1': '#D9D9D9',
        'blue-1': '#97D2FB',
        'blue-2': '#83BCFF',
        'green-1': '#80FFE8',
        'yellow-1': '#E0DCBD',

      },
      backgroundImage: {
        'login' : 'url("/static/Bg/login-bg.png")',
        'register' : 'url("/static/Bg/register-bg.png")',
        'todolist' : 'url("/static/Bg/todolist-bg.png")',
      },

    },
  },
  plugins: [],
}
