# OSalean Dashboard - Sales Management System

Website dashboard lengkap untuk manajemen penjualan dengan 5 halaman utama yang fully responsive dan interactive.

## 📁 Struktur Folder

```
osalean-dashboard/
├── index.html          # Dashboard - Sales Overview
├── analytics.html      # Analytics - Business Metrics
├── invoice.html        # Invoice Management
├── products.html       # Products Catalog
├── blog.html          # Blog & Insights
├── images/            # Folder gambar
│   ├── logo.png
│   ├── profile.png
│   ├── product1.png
│   ├── product2.png
│   ├── product3.png
│   ├── product4.png
│   ├── product5.png
│   ├── blog1.png
│   ├── blog2.png
│   └── blog3.png
└── README.md
```

## 🎨 Fitur Utama

### ✅ Responsive Design
- **Mobile First**: Navbar hamburger menu yang berfungsi dengan baik
- **Tidak ada horizontal scroll**: Semua elemen proporsional di mobile
- **Breakpoints**: Optimized untuk mobile, tablet, dan desktop

### ✅ Fitur Interaktif (JavaScript)

#### 1. **Mobile Navigation**
- Hamburger menu yang dapat dibuka/tutup
- Smooth animation
- Overlay background

#### 2. **Dashboard (index.html)**
- View toggle (Default/Weekly/Monthly)
- Export button
- Interactive charts
- Filter button

#### 3. **Analytics (analytics.html)**
- Period selector (Today/Week/Month/Year)
- Interactive metrics cards
- Real-time data visualization

#### 4. **Invoice (invoice.html)**
- Search functionality
- Status filter (All/Paid/Pending/Overdue)
- Send via WhatsApp button
- Download invoice
- View invoice details

#### 5. **Products (products.html)**
- Search products
- Category filter
- Grid/List view toggle
- Add to cart → WhatsApp
- Favorite & Quick view buttons

#### 6. **Blog (blog.html)**
- Search articles
- Category filter
- Read more → WhatsApp
- Featured article section

### ✅ Floating Buttons (Semua Halaman)

1. **WhatsApp Button**
   - Fixed position bottom right
   - Pulse animation
   - Link ke WhatsApp dengan pesan custom per halaman

2. **Scroll to Top Button**
   - Muncul setelah scroll 300px
   - Smooth scroll animation
   - Hover effect

## 🎯 Teknologi yang Digunakan

- **HTML5**: Semantic markup
- **Tailwind CSS**: Utility-first CSS framework
- **JavaScript Vanilla**: Tanpa library tambahan
- **Google Fonts**: Inter font family
- **Bootstrap Icons**: Icon set yang ringan dan modern

## 🚀 Cara Menggunakan

1. **Buka file HTML di browser**
   ```
   Klik kanan pada index.html → Open with → Browser pilihan Anda
   ```

2. **Testing Responsive**
   - Buka Developer Tools (F12)
   - Toggle device toolbar (Ctrl+Shift+M)
   - Test di berbagai ukuran layar

3. **Customize WhatsApp Number**
   - Cari `6281234567890` di semua file HTML
   - Ganti dengan nomor WhatsApp Anda

## 📱 Mobile Optimization

### Navbar Mobile
- ✅ Hamburger menu berfungsi sempurna
- ✅ Tidak ada glitch atau horizontal scroll
- ✅ Smooth open/close animation
- ✅ Overlay background saat menu terbuka

### Floating Buttons
- ✅ Posisi fixed yang tidak mengganggu konten
- ✅ Tidak menyebabkan horizontal scroll
- ✅ Responsive di semua ukuran layar

## 🎨 Color Scheme

- **Primary**: #13ec5b (Green)
- **Background Light**: #f6f8f6
- **Background Dark**: #102216
- **Navy Dark**: #0a192f

## 📝 Catatan Penting

### Frontend Only
Semua fitur menggunakan JavaScript frontend tanpa backend:
- Filter dan search bekerja di client-side
- Data bersifat static/demo
- WhatsApp integration untuk komunikasi

### Integrasi WhatsApp
Setiap fitur yang memerlukan action mengarah ke WhatsApp:
- Add to Cart → WhatsApp dengan detail produk
- Send Invoice → WhatsApp dengan detail invoice
- Read Article → WhatsApp untuk request artikel
- Contact → WhatsApp untuk pertanyaan

## 🔧 Customization

### Mengganti Logo
1. Replace file `images/logo.png`
2. Ukuran recommended: 512x512px

### Mengganti Profile Photo
1. Replace file `images/profile.png`
2. Ukuran recommended: 400x400px

### Menambah Produk
Edit file `products.html`:
```html
<div class="product-card ...">
  <!-- Copy struktur product card yang ada -->
</div>
```

### Menambah Blog Article
Edit file `blog.html`:
```html
<div class="blog-card ...">
  <!-- Copy struktur blog card yang ada -->
</div>
```

## 📊 Halaman-Halaman

### 1. Dashboard (index.html)
- Sales overview
- Metric cards (Total Sales, Purchase, User Growth, New Customers)
- Weekly satisfaction chart
- Orders by country
- Top selling products table

### 2. Analytics (analytics.html)
- Key metrics (Revenue, Conversion, AOV, Visitors)
- Revenue overview chart
- Traffic sources breakdown
- Top products performance
- Customer behavior insights

### 3. Invoice (invoice.html)
- Invoice statistics
- Search & filter invoices
- Invoice list table
- Actions: View, Download, Send via WhatsApp
- Pagination

### 4. Products (products.html)
- Product statistics
- Search & category filter
- Grid/List view toggle
- Product cards with images
- Add to cart functionality

### 5. Blog (blog.html)
- Featured article
- Search & category filter
- Blog grid layout
- Article cards with categories
- Load more functionality

## 🌐 Browser Support

- ✅ Chrome (Recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Mobile browsers

## 📞 Support

Untuk pertanyaan atau bantuan, hubungi via WhatsApp:
- Nomor: 6281234567890 (ganti dengan nomor Anda)

## 📄 License

© 2024 OSalean Management System. All rights reserved.

---

**Dibuat dengan ❤️ menggunakan Tailwind CSS dan JavaScript Vanilla**
