# usr/bin/env python
# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from Cryptodome.Cipher import AES # str不是16的倍数那就补足为16的倍数
from binascii import b2a_hex, a2b_hex
import easygui

key = 'this is a key123'
inv_key = 'This is an IV456'


class Encryption:                  #定义Encryption类
    def __init__(self):
        self.declare = "wud"       #初始化
        self.key = 'this is a key123'
        self.inv_key = 'This is an IV456'

    def Encry_file(self, path):   #加密文件函数
        """文件加密模块儿"""

        inv_path = path[::-1]     #解析出路径
        location = inv_path.index("\\")
        path_true = inv_path[location:][::-1]

        location_4 = inv_path.index(".")
        file_name = inv_path[location_4 + 1:location][::-1] + ".bin"  #重命名文件
        file_path = path_true + file_name
        obj = AES.new(key, AES.MODE_OFB, inv_key)                     #新建加密对象

        f = open(path, "rb")                                          #读取文件内容
        info = f.read()
        while len(info) % 16 != 0:
            info += '='

        ciphertext = b2a_hex(obj.encrypt(info))                       #返回的二进制十六进制表示                

        f_4 = open(file_path, "wb")                                   #定义新文件
        f_4.write(ciphertext)                                         #将十六进制的内容写入文件                       
        f_4.close()
        f.close()

        print "加密完成"
        return file_path                                              #返回文件路径

    def Decry_file(self, path):
        """文件解密模块儿"""
        obj = AES.new(key, AES.MODE_OFB, inv_key)                     #新建AES对象
        f = open(path, "rb")
        info = f.read()                                               #将文本内容写入info
        f.close()
        plain = obj.decrypt(a2b_hex(info))                            #调用解密函数返回给plain
        f_3 = open("1.jpg", "wb")                                     #打开一个1.jpg文件
        f_3.write(plain)                                              #将plain信息写入1.jpg
        f.close()
        print "解密完成",
        print "文件名", "1.jpg"

    def Encry_text(self, message):
        """加密文本"""
        obj = AES.new(key, AES.MODE_OFB, inv_key)
        while len(message) % 16 != 0:
            message += '='
        ciphertext = obj.encrypt(message)
        ciphertext = b2a_hex(ciphertext)
        return ciphertext
        # f = open("cipher.bin", "wb")
        # f.write(ciphertext)
        # f.close()
        #
        # f_4 = open("cipher.bin", "rb")
        # text = f_4.read()
        # obj_2 = AES.new(key, AES.MODE_OFB, inv_key)
        # plain_text = obj_2.decrypt(a2b_hex(text))
        # print plain_text

    def Decry_text(self, message):
        """解密文本"""
        obj = AES.new(key, AES.MODE_OFB, inv_key)
        plain_text = obj.decrypt(a2b_hex(message))
        print "密文:", message
        print "明文:", plain_text


if __name__ == '__main__':
    print "ah"

    # 解密文件
    file_name = "3.bin"
    Encryption().Decry_file(file_name)

    # 解密文本
    message = "c8f5a5969c72955566fda87620a99a8c"
    Encryption().Decry_text(message)
