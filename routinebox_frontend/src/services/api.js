import axios from 'axios';

// Cấu hình đường dẫn API gốc (Base URL)
// Sau này khi có Backend thật sẽ thay đổi thành http://localhost:8080/api hoặc domain thật
const API_BASE_URL = 'https://mock-api.routinebox.com/api'; 

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 10000, // Timeout sau 10s
});

// Interceptor: Tự động gắn Token vào mỗi request nếu người dùng đã đăng nhập [cite: 96]
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token'); // Lấy token từ bộ nhớ trình duyệt
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Interceptor: Xử lý lỗi trả về từ server
api.interceptors.response.use(
  (response) => response.data, // Trả về data trực tiếp cho gọn
  (error) => {
    if (error.response?.status === 401) {
      // Nếu hết hạn token (401), tự động logout
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export default api;