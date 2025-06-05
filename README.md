# 🤖 Crypto Trading Bot (Local Test Version)

บอทเทรดคริปโตที่สามารถใช้กลยุทธ์ต่าง ๆ และมีระบบ AI/ML วิเคราะห์แนวโน้ม พร้อมแดชบอร์ดสำหรับควบคุมและทดสอบ

## 📦 ฟีเจอร์
- กลยุทธ์: RSI, DCA, Grid Trading, MACD
- โมเดล AI/ML วิเคราะห์ทิศทางตลาด
- ระบบ Backtest และจำลองกลยุทธ์จากข้อมูลย้อนหลัง
- ระบบแจ้งเตือนผ่าน Discord
- ระบบ Login/Register และฐานข้อมูล SQLite
- แดชบอร์ดเว็บสำหรับควบคุมและทดสอบ

## 🚀 การเริ่มต้นใช้งาน

### 1. ติดตั้ง dependencies ของ Python
```bash
pip install -r requirements.txt
```

### 2. ตั้งค่าฐานข้อมูล
```bash
python -c "from db import init_db; init_db()"
```

### 3. ตั้งค่า API และ Webhook
```bash
cp .env.example .env
# แก้ไข .env ตามที่ต้องการ
```

### 4. รัน API Server
```bash
python api_server.py
```

### 5. รัน Web Dashboard
```bash
cd web-dashboard
npm install
npm run dev
#  open http://localhost:3000 in your browser.
```

## 📝 ข้อควรระวัง
- บอทนี้เป็นเวอร์ชันทดสอบ ไม่ควรใช้จริง
- ตั้งค่า API และ Webhook ให้ถูกต้อง
- ตรวจสอบข้อมูลที่ใช้ในระบบ Backtest ให้ถูกต้อง 

## 📂 Tech Stack
- Python + Flask
- React (JavaScript + Vite for frontend)
- SQLite for local DB
- CCXT
- Pandas
- Scikit-learn
- Discord Webhook
