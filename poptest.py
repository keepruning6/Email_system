# -- coding: utf-8 --
import smtplib
import poplib
import cStringIO
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header

mail_host = "smtp.qq.com"
host = "pop.qq.com"
mail_user = "20***3@qq.com"
mail_pass = "l***a"    #登录码
sender = '20****63@qq.com'
receivers =['15****7@qq.com']

'''message = MIMEMultipart()
message['From'] = Header("helllp",'utf-8')   #发件人信息
message['To'] =Header("test",'utf-8')        #收件人信息
subject = 'python test'
message.attach(MIMEText('aaaa','plain','utf-8')) #正文信息
#att1=MIMEText(open('3.txt','rb').read(),'base64','utf-8')
att1 = MIMEApplication(open("3.txt", 'rb').read())
att1.add_header('Content-Disposition', 'attachment', filename="3.txt")
#att1["Content-Type"] = 'application/octet-stream'
#att1["Content-Disposition"] = 'attachment;filename="3.txt"'
message.attach(att1)
try:
	smtpObj =smtplib.SMTP()
	smtpObj.connect(mail_host)
	smtpObj.login(mail_user,mail_pass)
	smtpObj.sendmail(sender,receivers,message.as_string())
	print ("success")
except smtplib.SMTPException:
	print ("false")
'''
pp=poplib.POP3(host)
#pp.set_debuglevel(1)
pp.user(mail_user)
pp.pass_(mail_pass)
ret=pp.stat()
print ret
num = len(pp.list()[1])
print 'num of messages', num

for i in range(1,num):
    #m = M.retr(i+1)
    m = pp.retr(i)

    buf = cStringIO.StringIO()
    buf.seek(0)
    msg = email.message_from_file(buf)
    print '?'
    for par in msg.walk():
    	print '111'
        #if not par.is_multipart():
        name = par.get_filename()

        if name:
            print 'name',name
            print '222'
            data = par.get_payload(decode=True)
            try:
                f = open(dstdir, 'wb') #注意一定要用wb来打开文件，因为附件一般都是二进制文件
                print 'save attfile succeed'
            except:
                print 'open  file name error'
            f.write(data)
            f.close()
            pp.dele(i)
        else:
        #不是附件，是文本内容
            body = par.get_payload(decode=True) # 解码出文本内容，直接输出来就可以了。
            #print 'body:',body
            pass
            #print 'body:',body       #中文没有处理好，所有没有输出了。
        #print '+'*60 # 用来区别各个部分的输出
    else:
        continue
pp.quit()
print 'exit'
#for i in range(1,ret[0]+1):
#	mlist=pp.top(1,0)
#	print 'line:',len(mlist[1])
#ret =pp.list()
#print ret
#down= pp.retr(1)
#print 'lines:',len(down)
#for line in down[1]:
#	print line
#pp.quit()