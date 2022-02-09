from ftplib import FTP
import getpass

username = getpass.getuser()
filepath = "change to file path you want to ftp"
print(filepath)

ftp = FTP('change this to ip address of server')
ftp.login(user='change to username',passwd='change to password')
with open(filepath, 'rb') as f:
     ftp.storbinary('STOR %s' % 'change to folder on server you want file to go to', f)
ftp.quit()