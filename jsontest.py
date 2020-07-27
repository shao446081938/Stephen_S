import json
from textwrap import indent
dict1 = {"ZhangShu":1,"ShaoYanhua":2,"ZhangZhandong":3}
json1 = json.dumps(dict1)
jf1 = open("jsontestf1.json",'r',encoding='utf8')
jf2 = open("jsontestf2.json",'w',encoding='utf8')
json2 = json.load(jf1)
json.dump(dict1,jf2,ensure_ascii=False)
jf1.close
jf2.close

print(json2)