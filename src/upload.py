import ftplib

# FTP connection information
ftp_server = ""
ftp_username = ""
ftp_password = ""
ftp_path = "/data/summary.txt"

# Local path to the file
file_path = "summary.txt"

# Establish connection to the FTP server
ftp_conn = ftplib.FTP(ftp_server)
ftp_conn.login(user=ftp_username, passwd=ftp_password)

# Upload the file
with open(file_path, 'rb') as file:
    ftp_conn.storbinary(f'STOR {ftp_path}', file)

print("Successfully uploaded summary.txt")

# Close the connection
ftp_conn.quit()
