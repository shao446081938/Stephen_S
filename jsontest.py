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
def insert_json_toMySQL(json_file, mycursor,mydb):
    load_dict = json.load(json_file)
    #print(type(load_dict))  #测试读取的数据类型

    for value in load_dict.values():  #测试从json中读取的词典键值对的保存形式
        for value2 in value:
            print(value2['id'], value2['name'], value2['sex'], value2['age'],
                  value2['addr'], value2['grade'], value2['phone'],
                  value2['gold'])
            SQL_INSERT_DATA = "INSERT INTO stu_info(ID,SNAME,SEX,Age,Addr,Grade,Phonenumber,Gold)VALUES(%d,'%s','%s',%d,'%s','%s','%s',%d)" % (
                value2['id'], value2['name'], value2['sex'], value2['age'],
                value2['addr'], value2['grade'], value2['phone'],
                value2['gold'])
            mycursor.execute(SQL_INSERT_DATA)
            mydb.commit()



if __name__ == "__main__":
    #链接MySQL数据库
    mydb1 = pymysql.connect(host='localhost',
                            user='root',
                            password='root',
                            port=3306,
                            database='test_1',
                            charset='utf8')  #链接本地mysql数据库
    mycursor = mydb1.cursor()  #新建游标变量
    #mycursor.execute("DROP TABLE IF EXIST stu_info")  #测试用，删除原有表
    SQL_CREATE_TABLE = "CREATE TABLE IF NOT EXISTS stu_info(ID INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, SNAME VARCHAR(255), SEX VARCHAR(255), Age INT, Addr VARCHAR(255), Grade VARCHAR(255), PhoneNumber VARCHAR(255),Gold INT)"
    mycursor.execute(SQL_CREATE_TABLE)  #创建表（如果不存在的话）
    json_file = open("/home/stephens/文档/test/Stephen_S/jsontestf1.json", 'r', encoding='utf8')  #打开本地编写好的json文件
    insert_json_toMySQL(json_file, mycursor,mydb1)
