# -*- coding: UTF-8 -*-
def getText():
	txt=open("D:\\git\\ShakespeareSonnets.txt","r").read()   #���ݾ���·���޸�
	txt=txt.lower()   #Сд
	return txt

ss=getText()
words=ss.split()   #�пո�ͷָ�
counts={}
for word in words:   #ͳ�Ʒ���ʵ�
	counts[word]=counts.get(word,0)+1
items=list(counts.items())   #ת��Ϊ�б�
items.sort(key=lambda x:x[1],reverse=True)   #��ֵ�Ƚϣ�����
for i in range(100):   #��ӡǰһ��
	word, count=items[i]
	print ("{0:<10}{1:>5}".format(word, count))
