''' Claculator'''
#Varables
opration_list=['+','-','*','/','%','**','//']
opration_logical_list=['&','|','^','~','<<','>>']
opration=''
number_1=0
number_2=0
mode=0
resalt=0
print("----------Welcome my friend----------")
#Main loop
while True:
	print ("Please input '0' if you need Seintific")
	print ("Input '1' if you need logical")
	print ("Input '2' if you need convert")
	print ("Input '3' If you need exit")
	mode =int(input ("Please input mode : ")) #input mode 
	#Seintific
	if mode == 0:
		while True:
			try:
				number_1=float(input("Enter frist number ="))
				break
			except:
				print ("Enter Valid Number")
		while True:
			try:
				number_2=float(input("Enter sec number ="))
				break
			except:
				print ("Enter Valid Number")
		while True:
			opration=input("Enter opration['+','-','*','/','%','**','//']: ")
			if opration in opration_list:
				if opration == '+':
					resalt=number_1 + number_2
					print("The resalt =",resalt)
					break
				elif opration== '-':
					resalt=number_1 - number_2
					print("The resalt =",resalt)
					break
				elif opration== '*':
					resalt=number_1 * number_2
					print("The resalt =",resalt)
					break
				elif opration== '/':
					resalt=number_1 / number_2
					print("The resalt =",resalt)
					break
				elif opration== '**':
					resalt=number_1 ** number_2
					print("The resalt =",resalt)
					break
				elif opration== '//':
					resalt=number_1 // number_2
					print("The resalt =",resalt)
					break
				elif opration== '%':
					resalt=number_1 % number_2
					print("The resalt =",resalt)
					break
			else:
				print("Error opration")
	#logical
	elif mode ==1:
		while True:
			try:
				number_1=int(input("Enter frist number ="))
				break
			except:
				print ("Enter Valid Number")
		while True:
			opration=input("Enter opration['&','|','^','~','<<','>>']: ")
			if opration =='~':
				resalt= ~number_1
				print("The resalt =",resalt)
				break
			elif opration in opration_logical_list:
				while True:
					try:
						number_2=int(input("Enter sec number ="))
						break
					except:
						print ("Enter Valid Number")
				if opration == '&':
					resalt=number_1 & number_2
					print("The resalt =",resalt)
					break
				elif opration== '|':
					resalt=number_1 | number_2
					print("The resalt =",resalt)
					break
				elif opration== '^':
					resalt=number_1 ^ number_2
					print("The resalt =",resalt)
					break
				elif opration== '<<':
					resalt=number_1 << number_2
					print("The resalt =",resalt)
					break
				elif opration== '>>':
					resalt=number_1 >> number_2
					print("The resalt =",resalt)
					break
			else:
				print("Error opration")
	#convert to "binary,hexadecimal,Octal"
	elif mode==2:
		number_1=int(input("Enter dicmal number you need covert="))
		print ("Binary=",bin(number_1))
		print ("hexadecimal=",hex(number_1))
		print ("Octal=",oct(number_1))
	#Exit from program
	elif mode==3:
		print("----------Thanks my friend---------- ")
		break
	else:
		print ("Error mode")