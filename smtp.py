#coding: utf-8  
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '20****3@qq.com'
receiver = '142*****47@qq.com'
subject = 'python email test'
smtpserver = 'smtp.qq.com'
username = '205****3@qq.com'
password = '****'       #登录码

msg = MIMEText( 'Hello Python', 'text', 'utf-8' )
msg['Subject'] = Header( subject, 'utf-8' )

smtp = smtplib.SMTP()
smtp.connect( smtpserver )
smtp.login( username, password )
smtp.sendmail( sender, receiver, msg.as_string() )
smtp.quit()