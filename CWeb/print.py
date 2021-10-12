import re

x = 'From: Using the : character'
y = re.findall('^F.+:',x)
print(y)

x = 'From stekmd.msdofn@jsdc.sdc.d Sat DM 5522 11:25'
y = re.findall('\S+@\S+',x)
print(y)

y = re.findall('^From .*@([^ ]*)',x) #extrae todos caracteres hasta un esapcio
#Los corchetes son un NOT
print(y)

x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)#para usar caracteres que usan las expresiones regualares se usa "\"
print(y)

x = '<a href="http://py4e-data.dr-chuck.net/known_by_Ogheneruno.html">Ogheneruno</a>'
y = re.findall('>(\S+)</', x)
print(y)


x = 'http://py4e-data.dr-chuck.net/known_by_Ogheneruno.html'
y = re.findall('y_(\S+)\.h', x)
print(y)
