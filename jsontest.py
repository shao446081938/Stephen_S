#encoding: utf-8
'''
@File    :   jsontest.py
@Time    :   2020/07/28 10:11:20
@Author  :   Yanhua Shao
@Contact :   shaoyanhua@ihep.ac.cn
'''
# Start typing your code from here

import json
import pymysql


#要将json文件中的数据存入数据库，需要将json文件转换为dict格式再转入
def insert_json_toMySQL(json_file):
    load_dict = json.load(json_file)
  

if __name__ == "__main__":
    #链接MySQL数据库
    mydb1 = pymysql.connect(host='localhost',
                            user='root',
                            password='',
                            database='test_1',
                            charset='utf8')  #链接本地mysql数据库
    mycursor = mydb1.cursor()  #新建游标变量
    mycursor.execute(
        "CREATE TABLE IF NOT EXISTS stu_info(ID INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, SNAME VARCHAR(255), SEX VARCHAR(255), Age INT, Addr VARCHAR(255), Grade VARCHAR(255), PhoneNumber INT,Gold INT)"
    )  #创建表（如果不存在的话）
    json_file = open("jsontestf1.json", 'r', encoding='utf8')  #打开本地编写好的json文件
