import { Link, NavLink } from 'react-router-dom';
import { ShoppingBag, User, Search, Menu } from 'lucide-react'; // Icon từ thư viện đã cài

const Header = () => {
  // Hàm helper để active link (tô đậm menu đang chọn)
  const navLinkClass = ({ isActive }) =>
    isActive
      ? "text-primary font-bold border-b-2 border-primary pb-1"
      : "text-dark hover:text-primary transition-colors";

  return (
    <header className="bg-white shadow-sm sticky top-0 z-50">
      <div className="container mx-auto px-4 h-16 flex items-center justify-between">
        {/* 1. Logo */}
        <Link to="/" className="text-2xl font-bold text-primary tracking-tight">
          RoutineBox
        </Link>

        {/* 2. Menu chính (Desktop) */}
        <nav className="hidden md:flex space-x-8">
          <NavLink to="/" className={navLinkClass}>Trang chủ</NavLink>
          <NavLink to="/shop" className={navLinkClass}>Sản phẩm</NavLink>
          {/* Tính năng Routine Builder [cite: 38] */}
          <NavLink to="/my-routine" className={navLinkClass}>Routine của tôi</NavLink>
          {/* Tính năng Skin Quiz  */}
          <NavLink to="/skin-quiz" className={navLinkClass}>Khảo sát da</NavLink>
        </nav>

        {/* 3. Icons Action */}
        <div className="flex items-center space-x-4">
          {/* Nút tìm kiếm [cite: 32] */}
          <button className="p-2 hover:bg-gray-100 rounded-full">
            <Search size={20} />
          </button>
          
          {/* Giỏ hàng  */}
          <Link to="/cart" className="p-2 hover:bg-gray-100 rounded-full relative">
            <ShoppingBag size={20} />
            <span className="absolute top-0 right-0 bg-primary text-white text-xs w-4 h-4 flex items-center justify-center rounded-full">
              0
            </span>
          </Link>

          {/* User Profile */}
          <Link to="/login" className="p-2 hover:bg-gray-100 rounded-full">
            <User size={20} />
          </Link>
          
          {/* Mobile Menu Button */}
          <button className="md:hidden p-2">
            <Menu size={24} />
          </button>
        </div>
      </div>
    </header>
  );
};

export default Header;