import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Header from "./components/layout/Header"; // Import Header từ file vừa tạo

// --- Các Component tạm thời (Placeholder) ---
const Home = () => <div className="p-4">Trang chủ - Giới thiệu</div>;
const Shop = () => <div className="p-4">Danh sách sản phẩm (Filter Texture/Safety)</div>;
const SkinQuiz = () => <div className="p-4">Khảo sát da (Input: Dầu/Khô)</div>;
const RoutineBuilder = () => <div className="p-4">Xây dựng Routine (Sáng/Tối)</div>;
const Login = () => <div className="p-4">Đăng nhập</div>;

// --- Component Chính ---
function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-50 text-dark font-sans">
        {/* Header nằm trong Router để dùng được Link/NavLink */}
        <Header /> 

        <main className="container mx-auto px-4 py-6">
          <Routes>
            {/* Public Routes */}
            <Route path="/" element={<Home />} />
            <Route path="/shop" element={<Shop />} /> 
            <Route path="/login" element={<Login />} /> 

            {/* Protected Routes */}
            <Route path="/skin-quiz" element={<SkinQuiz />} />
            <Route path="/my-routine" element={<RoutineBuilder />} />
            
            {/* Admin Route */}
            <Route path="/admin/*" element={<div>Admin Dashboard</div>} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;