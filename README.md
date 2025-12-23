# 💄 Smart Beauty Routine - E-commerce & Skincare Consultant

> **Hệ thống Thương mại điện tử Mỹ phẩm tích hợp Tư vấn Lộ trình Chăm sóc da thông minh.**

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-In%20Development-yellow)](https://github.com/username/repo)

## 📖 Giới thiệu (Introduction)

**Smart Beauty Routine** không chỉ là một website bán mỹ phẩm thông thường. Nó giải quyết nỗi đau lớn nhất của người dùng: **"Mua mỹ phẩm xong nhưng không biết dùng thứ tự nào cho đúng?"**.

Dự án này tích hợp thuật toán **Auto-Routine Builder**, tự động sắp xếp các sản phẩm người dùng chọn thành một quy trình chuẩn y khoa (Sáng/Tối) dựa trên thành phần và kết cấu sản phẩm.

### ✨ Tính năng nổi bật (Key Features)

* 🛍️ **E-commerce:** Tìm kiếm, lọc sản phẩm (theo loại da, vấn đề da), giỏ hàng, thanh toán.
* 🧠 **Smart Routine Builder (Core):**
    * Tự động sắp xếp thứ tự sử dụng (Ví dụ: Lỏng trước - Đặc sau, pH thấp trước - pH cao sau).
    * Phân chia quy trình Sáng (Morning) và Tối (Evening).
    * Cảnh báo xung đột thành phần (Ví dụ: Retinol + Vitamin C).
* 👤 **Skin Profile:** Lưu trữ hồ sơ da của người dùng để gợi ý sản phẩm phù hợp.
* 📦 **Quản lý đơn hàng:** Theo dõi trạng thái đơn hàng thời gian thực.

---

## 🛠️ Công nghệ sử dụng (Tech Stack)

*(Hãy bỏ chọn hoặc sửa lại các icon dưới đây theo đúng công nghệ bạn dùng)*

**Frontend:**
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)

**Backend:**
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

**Database:**
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)

**Tools:**
![Figma](https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)

---

## ⚙️ Cài đặt & Chạy dự án (Installation)

Làm theo các bước sau để chạy dự án trên máy local:

### 1. Clone dự án
```bash
git clone [https://github.com/username/smart-beauty-routine.git](https://github.com/username/smart-beauty-routine.git)
cd smart-beauty-routine

```

### 2. Cài đặt Backend

```bash
cd backend
npm install  # Hoặc composer install / pip install tùy ngôn ngữ
cp .env.example .env
# Cấu hình thông tin Database trong file .env

```

### 3. Cài đặt Frontend

```bash
cd frontend
npm install

```

### 4. Khởi tạo Database

Import file `database.sql` vào hệ quản trị CSDL của bạn hoặc chạy lệnh migration:

```bash
# Ví dụ với Node/Sequelize hoặc Laravel
npm run migrate
npm run seed  # Để tạo dữ liệu mẫu (Categories, Products)

```

### 5. Khởi chạy

* **Backend:** `npm start` (Port 5000)
* **Frontend:** `npm run dev` (Port 3000)

---

## 🗂️ Thiết kế Cơ sở dữ liệu (Database Schema)

Logic cốt lõi của tính năng **Routine Builder** nằm ở bảng `Categories`.

| Table Name | Description | Key Columns |
| --- | --- | --- |
| `users` | Lưu thông tin người dùng | `id`, `email`, `skin_type` |
| `products` | Sản phẩm mỹ phẩm | `id`, `name`, `category_id`, `price` |
| `categories` | **Chứa logic sắp xếp** | `id`, `name`, **`step_order`** (INT) |
| `routines` | Quy trình người dùng tạo | `id`, `user_id`, `name` |
| `routine_items` | Chi tiết quy trình | `product_id`, `usage_time` (Day/Night) |

**Quy ước `step_order`:**

* `10`: Tẩy trang
* `20`: Sữa rửa mặt
* `30`: Toner
* `40`: Serum/Treatment
* `50`: Kem dưỡng ẩm
* `60`: Kem chống nắng

---

## 🚀 Lộ trình phát triển (Roadmap)

* [x] Phân tích yêu cầu & Thiết kế Database
* [ ] Xây dựng API (Authentication, Product CRUD)
* [ ] Xây dựng Frontend (Homepage, Product List)
* [ ] **Phát triển tính năng Routine Builder** (Logic sắp xếp)
* [ ] Tích hợp Giỏ hàng & Thanh toán
* [ ] Deploy lên Server (Vercel/Heroku/AWS)

---

## 📸 Demo Screenshots

*(Dán ảnh chụp màn hình dự án vào đây sau khi bạn code xong giao diện)*

| Homepage | Routine Builder | Product Detail |
| --- | --- | --- |
|  |  |  |

---

## 🤝 Đóng góp (Contributing)

Mọi đóng góp đều được hoan nghênh. Vui lòng tạo Pull Request cho các tính năng mới hoặc sửa lỗi.

## 📄 License

Dự án này được cấp phép dưới [MIT License](https://www.google.com/search?q=LICENSE).
