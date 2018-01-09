def c(str1):
	str2=str1[::-1]
	str3=''
	c=0

	if str1==str2:
		print("yes")
		return str1
	else:
		for x in range(0,len(str1)):
			if c ==0:
				for y in range(0,len(str2)):
					if(x==y):
						if str1[x]==str2[y]:
							str3=str3+str1[x]
					
						else:
							str1=str1.replace(str1[x],'')
							c=1
	if c <= len(str1):
		
	return c(str1)
str1=raw_input("enter string:")
c(str1)
print(str1)



