import subprocess
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# === CONFIGURATION ===
PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_DATABASE = os.getenv("PG_DATABASE")
BACKUP_DIR = os.getenv("BACKUP_DIR_POSTGRES")

# === CREATE TIMESTAMPED FOLDER ===
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
backup_folder = os.path.join(BACKUP_DIR, f"postgres-backup-{timestamp}")
os.makedirs(backup_folder, exist_ok=True)

backup_file = os.path.join(backup_folder, f"{PG_DATABASE}.dump")

# Set password environment variable for pg_dump
env = os.environ.copy()
env["PGPASSWORD"] = PG_PASSWORD

# === RUN PG_DUMP ===
dump_command = [
    "pg_dump",              # PostgreSQL backup utility

    "-h", PG_HOST,          # Hostname or IP address of PostgreSQL server
                            # Example: "localhost"

    "-p", PG_PORT,          # Port number on which PostgreSQL is running
                            # Default is 5432

    "-U", PG_USER,          # Database username used for authentication

    "-d", PG_DATABASE,      # Name of the database to backup

    "-F", "c",              # Output file format:
                            #   c = custom format (recommended)
                            #       - compressed
                            #       - required for pg_restore
                            #       - allows selective restore
                            #   p = plain SQL (text file)
                            #   t = tar format
                            #   d = directory format

    "-f", backup_file       # Output file path where backup will be stored
                            # Example: /backups/db.dump
]

try:
    subprocess.run(dump_command, check=True, env=env)
    print(f"✅ Backup successful: {backup_file}")
except subprocess.CalledProcessError as e:
    print("❌ Backup failed:", e)
