# -*- coding: UTF-8 -*-
def getText():
	txt=open("D:\\git\\ShakespeareSonnets.txt","r").read()   #根据具体路径修改
	txt=txt.lower()   #小写
	return txt

ss=getText()
words=ss.split()   #有空格就分割
counts={}
for word in words:   #统计放入词典
	counts[word]=counts.get(word,0)+1
items=list(counts.items())   #转换为列表
items.sort(key=lambda x:x[1],reverse=True)   #键值比较，降序
for i in range(100):   #打印前一百
	word, count=items[i]
	print ("{0:<10}{1:>5}".format(word, count))
