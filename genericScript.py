# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 09:55:37 2018

@author: Santi
"""
import os
from Crypto.Cipher import ARC2

cipher=ARC2.new('ELPbestAsignaturaEver')

if os.path.exists("executions"):
	fileexecutions = open("executions", 'rb')
	n=fileexecutions.read()
	fileexecutions.close()
	print(n) 
	n=cipher.decrypt(n)
	n=str(n).strip('b').strip("'").strip(' ')
	n=int(n)+1
else:
	n=1
numberExecutions=open("nexes.txt",'w')
numberExecutions.write(str(n))
numberExecutions.close()
tocipher=str(n)
i=1
proof=False
while not proof:
	if len(tocipher)<(8*i):
		tocipher=tocipher+" "
	elif len(tocipher)>(8*i):
		i=i+1
	else:
		proof=True

print(tocipher)
print(str(cipher.encrypt(tocipher)))
print(cipher.encrypt(tocipher))
print(cipher.decrypt(cipher.encrypt(tocipher)))
fileexecutions=open("executions", 'wb')
fileexecutions.write(cipher.encrypt(tocipher))
print(cipher.encrypt(tocipher))
print(cipher.encrypt(tocipher).decode("cp1252"))
fileexecutions.close()

filemax= open("max.txt", 'r')
n=filemax.read()
n=int(n)
filemax.close()

for i in range(n):
	stri=str(i)
	ruta="python scrapper" + stri + ".py >exit_" + stri + ".txt"
	retvalue=os.system(ruta)
	print ("Execution " + stri + ": " + str(retvalue))