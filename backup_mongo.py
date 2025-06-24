import subprocess
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
# === CONFIGURATION ===
MONGO_URI = os.getenv("MONGO_URI")  
BACKUP_DIR = os.getenv("BACKUP_DIR")  # Directory to store backups

# === CREATE TIMESTAMPED FOLDER ===
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
backup_path = os.path.join(BACKUP_DIR, f"mongo-backup-{timestamp}")
os.makedirs(backup_path, exist_ok=True)

# === RUN MONGODUMP ===
dump_command = [
    "mongodump",
    f"--uri={MONGO_URI}",
    f"--out={backup_path}"
]

try:
    subprocess.run(dump_command, check=True)
    print(f"✅ Backup successful: {backup_path}")
except subprocess.CalledProcessError as e:
    print("❌ Backup failed:", e)
