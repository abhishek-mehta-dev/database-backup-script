

# 🗃️ MongoDB Backup Script

A simple Python script to automate **MongoDB backups** using `mongodump`, with support for `.env` configuration and timestamped output folders.

---

## 🔧 Features

- ✅ Automated backup of MongoDB databases using `mongodump`
- 🕒 Timestamped backup folders
- 📁 Custom backup directory via environment variables
- 🔒 Keeps your sensitive credentials secure using `.env`
- 🐍 Lightweight and easy to schedule via cron or task scheduler

---

## 📦 Requirements

- Python 3.6+
- [mongodump](https://www.mongodb.com/docs/database-tools/mongodump/) installed and available in your system's PATH
- `python-dotenv` module for reading `.env` files

### 📥 Install Python dependency

```bash
pip install python-dotenv
````

---

## 📁 Clone this repository

```bash
git clone https://github.com/your-username/mongo-backup-script.git
cd mongo-backup-script
```

---

## 🛠️ Create a `.env` file in the root directory with the following content:

```env
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/dbname
BACKUP_DIR=/path/to/store/backups
```

---

## ▶️ Run the script

```bash
python backup.py
```

---

## ✅ Sample Output

```bash
✅ Backup successful: /path/to/store/backups/mongo-backup-YYYY-MM-DD_HH-MM-SS
```

---

## 📝 Notes

* Make sure `mongodump` is installed and accessible in your system PATH.
* The script will create a timestamped directory inside the provided `BACKUP_DIR`.
* For regular backups, consider scheduling the script using `cron` (Linux/macOS) or Task Scheduler (Windows).
* This script does **not** delete old backups — you can add your own logic or a cron job to handle cleanup.

---

