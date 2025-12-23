/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // Khai báo màu theo SRS
        primary: '#E91E63', 
        secondary: '#F8BBD0',
        dark: '#212121',
      }
    },
  },
  plugins: [],
}