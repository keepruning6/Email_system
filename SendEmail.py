# -*- coding:UTF-8 -*-
import smtplib
from email.mime.text import MIMEText    #导入文本
from email.mime.image import MIMEImage  #导入图片
from email.mime.multipart import MIMEMultipart #导入多类型
from email.header import Header 

sender ='20XXXXXX63@qq.com'
receivers= ['155XXXXXX7@qq.com']
mail_host='smtp.qq.com'
mail_user='205XXXXXXX63@qq.com'
mail_pass='XXXXXXXX'

message= MIMEMultipart('alternative')   #超文本类型使用
#message.attach(MIMEText('hello mail','plain','utf-8'))
message['From']= Header("wang",'utf-8')  #邮件头包括三部分发件人，收件人，邮件主题也就是from,to,subject
message['To']= Header("lin",'utf-8')
message['Subject']= Header('python test','utf-8')
html="""
<html>
  <head></head>
  <body>
    <p>图片：<br>
    <br><img src="cid:image1">
  </body>
</html>
"""
image=MIMEText(html,'html','utf-8')  #新建一个文本内容
message.attach(image)                
fp=open('1.jpg','rb')
msgImage=MIMEImage(fp.read())
fp.close()
msgImage.add_header('Content-ID','<image1>')
message.attach(msgImage)             #将图片装入邮件内容

#att1=MIMEText(open('./db/test.txt','rb').read(),'base64','utf-8')
#att1["Content-Type"]='application/octet-stream'
#att1["Content-Disposition"]='attachment;filename="test.txt"'
#message.attach(att1)

try:
	smtpObj=smtplib.SMTP()
	smtpObj.connect(mail_host,25)
	smtpObj.login(mail_user,mail_pass)
	smtpObj.sendmail(sender,receivers,message.as_string())
	print "success"
except smtp.SMTPException:
	print "Error"