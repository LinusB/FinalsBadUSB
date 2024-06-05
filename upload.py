import ftplib

# FTP-Verbindungsinformationen
ftp_server = "ftpupload.net"
ftp_username = "if0_36675030"
ftp_password = "ITsecurity2024"
ftp_path = "/data/importantdata.txt"

# Lokaler Pfad zur Datei
file_path = "importantdata.txt"

# Verbindung zum FTP-Server herstellen
ftp_conn = ftplib.FTP(ftp_server)
ftp_conn.login(user=ftp_username, passwd=ftp_password)

# Datei hochladen
with open(file_path, 'rb') as file:
    ftp_conn.storbinary(f'STOR {ftp_path}', file)

print("Successfully uploaded importantdata.txt")

# Verbindung schließen
ftp_conn.quit()
