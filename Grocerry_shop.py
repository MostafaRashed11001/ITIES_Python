# ## hint: its a good point to use file as json	  
# System for grocerry shop
# apple[40] -bannaa[30] -cherry[70]
# user take 3 - 2 - 10
# shop      37  28  60
# Cost      3*15 -

# #Welcome to ITI Shop
	# 1- Owner
	# 2- user
	# 3- exit
	# Select Mode For customer press 1 , for owner press two , to exist press 0 :  

# - Customer
    # - To show our products 				press 1         ---> products & cost
    # - To Buy from our products 			press 2     	---> Able to buy
    # - to print the bill 					press 3
# - to exist press 0
# - ITI OWNER
    # - Add new products       press 1
    # - Show Products          press 2
    # - Add Cost			   press 3
    # - Change cost			   press 4
# - to exist press 0
print("----------Welcome in grocerry shop----------")
password_list = ["2022",'g2']
Products_dic={
		"Apple" :[40.0,25.0], #[Quantity(kg):Price(L.E)]
		"Bannaa":[30.0,20.0],
		"Cherry":[70.0,30.0]
}
Customer_Products_dic={
			"Customer_product":["Quantity"]
}
cost=0
#Main loop
while True:
	print ("Modes:")
	print ("'1'for Owner")
	print ("'2'for user")
	print ("'3'for exit")
	while True:
		try:
			mode =int(input ("Please input mode : "))
			break
		except:
			print ("Enter Valid Number")															#input mode 
	if mode == 1:																					#owner_mode
		password=input ("Please enter your password:") 												#input Password
		if password in password_list:																#check password
			while True:
				print ("----------Welcome ITI Owner----------")
				print ("Owner Modes:")
				print ("press '1' for Add new products")
				print ("press '2' for Show Products")
				print ("press '3' for Change Cost")
				print ("press '4' for Change Quantity")
				print ("press '0' to exist to main mode")
				while True:
					try:
						owner_mode=int (input("Please choose mode:"))
						break
					except:
						print ("Enter Valid Number")
				if   owner_mode ==1:																#Add new products	
					name_of_new_product=input("Enter name of new product:")							#input new product
					while True:
						try:
							Quantity_of_new_product=float(input("Enter Quantity:"))					#input Quantity_of_new_product
							break
						except:
							print ("Enter Valid Number")
					while True:
						try:
							Price_of_new_product=float(input("Enter Price:"))						#input Price_of_new_product
							break
						except:
							print ("Enter Valid Number")
					Products_dic[name_of_new_product]=[Quantity_of_new_product,Price_of_new_product]
					print("products now:")
					print(Products_dic)																#output new products
				elif owner_mode ==2:																#Show Products
					print("products now[Quantity(kg):Price(L.E)]:")
					print(Products_dic)
				elif owner_mode ==3:																#Change Cost
					while True:
						name_of_new_product=input("Enter name of product:")							#choose product owner need change cost
						if name_of_new_product in Products_dic:
							break
						else:
							print ("Chosse Product form this list:")
							print(Products_dic)
					while True:
						try:
							Price_of_new_product=float(input("Enter Price:"))						#input new Cost
							break
						except:
							print ("Enter Valid Number")
					Products_dic[name_of_new_product]=[Products_dic[name_of_new_product][0],Price_of_new_product]
					print("product now[Quantity(kg):Price(L.E)]:")
					print(Products_dic[name_of_new_product])										#output changeing in product
				elif owner_mode ==4:																#Change Quantity
					while True:
						name_of_new_product=input("Enter name of product:")							#choose product owner need change Quantity
						if name_of_new_product in Products_dic:
							break
						else:
							print ("Chosse Product form this list:")
							print(Products_dic)
					while True:
						try:
							Quantity_of_new_product=float(input("Enter Quantity:"))					#Change Quantity
							break
						except:
							print ("Enter Valid Number")
					Products_dic[name_of_new_product]=[Quantity_of_new_product,Products_dic[name_of_new_product][1]]
					print("product now:")
					print(Products_dic[name_of_new_product])										#output changeing in product
				elif owner_mode ==0:
					break																			#exist to main mode
				else:
					print ("Choose one of this modes")
		else:
			print("----------Wrong password----------")												#Wrong password condtion
			print("Choose '1' again to enter the password")
	elif mode == 2:																					#Customer_mode
		print("----------Welcome in ITI grocerry shop----------")
		while True:
				print ("Customer Modes:")
				print ("press '1' for show our products")
				print ("press '2' for Buy from our products")
				print ("press '3' for Cost")
				print ("press '0' to exist to main mode")
				while True:
					try:
						Customer_mode=int (input("Please choose mode:"))							#input Customer_mode
						break
					except:
						print ("Enter Valid Number")
				if   Customer_mode ==1:																#Customer_mode show our products
					print("products--> 'Name of product': [Quantity(kg):Price(L.E)] : ")
					print(Products_dic)
				elif Customer_mode ==2:
					while True:
						while True:
							name_of_Customer_product=input("Enter name of product:")				#choose product Customer need to buy it
							if name_of_Customer_product in Products_dic:
								break
							else:
								print ("The "+name_of_Customer_product+" is not available in our products:")
								print ("If you need chosse available product form this list:")
								print(Products_dic)
						while True:
							try:
								Quantity_of_Customer_product=float(input("Enter Quantity:"))		#input Quantity Customer need it
								break
							except:
								print ("Enter Valid Number")
						if Products_dic[name_of_Customer_product][0]>=Quantity_of_Customer_product:	#Chack Quantity& output cost
							Customer_Products_dic[name_of_Customer_product]=[Quantity_of_Customer_product]
							cost+=(Quantity_of_Customer_product*Products_dic[name_of_Customer_product][1])
							Products_dic[name_of_Customer_product][0]-=Quantity_of_Customer_product
							print("Price of last product:")
							print((Quantity_of_Customer_product*Products_dic[name_of_Customer_product][1]))
							print("your product:")
							print(Customer_Products_dic)
							print("Total cost ="+ str(cost))
							break
						else:
							print("Quantity you needed not available at this moment :")
							print("You can found this "+str(Products_dic[name_of_Customer_product][0])+"Quantity")
				elif Customer_mode ==3:
					if cost>0:																		#Cost_Mode
						print("you orderd '"+ str(len(Customer_Products_dic)) + "' products from our shop")
						print("your product:")
						print(Customer_Products_dic)
						print("Total cost ="+ str(cost))
					elif cost==0:
						print("you don't buy any thing")
						print("Choose '1'to show our products and '2' to Buy our products")
				elif Customer_mode ==0:
					Customer_Products_dic.clear()
					break																			#exist to main mode
				else:
					print ("Choose one of this modes:")
	elif mode == 3:
		break																						#exit from main program
	else:
		print("----------Wrong Mode----------")														#Wrong Mode
		print("Please choose from this modes:")