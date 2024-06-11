import ftplib

# FTP-Verbindungsinformationen
ftp_server = ""
ftp_username = ""
ftp_password = ""
ftp_path = "/data/summary.txt"

# Lokaler Pfad zur Datei
file_path = "summary.txt"

# Verbindung zum FTP-Server herstellen
ftp_conn = ftplib.FTP(ftp_server)
ftp_conn.login(user=ftp_username, passwd=ftp_password)

# Datei hochladen
with open(file_path, 'rb') as file:
    ftp_conn.storbinary(f'STOR {ftp_path}', file)

print("Successfully uploaded summary.txt")

# Verbindung schließen
ftp_conn.quit()