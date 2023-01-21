# *****
# ****
# ***
# **
# *
#---------------------------------------------------------------------#
# size =int(input("input size of drawing:"))
# for number_rows in range(size):
	# for number_colums in range(size-number_rows):
		# print("*",end= ' ')
	# print("")
#---------------------------------------------------------------------#
'''       *
        * * *
      * * * * *
    * * * * * * *
  * * * * * * * * *
* * * * * * * * * * *
  * * * * * * * * *
    * * * * * * *
      * * * * *
        * * *
          *          '''
#---------------------------------------------------------------------#
# size =int(input("input size of drawing:"))
# for number_rows in range(size):
	# for number_space_colums in range(size-number_rows):
		# print(" ",end= ' ')
	# for number_Asterisk_colums in range(number_rows):
		# print("*",end= ' ')
	# for number_space_colums in range(number_rows+1):
		# print("*",end= ' ')
	# print("")
# for number_rows in range(size,-1,-1):
	# for number_space_colums in range(size-number_rows):
		# print(" ",end= ' ')
	# for number_Asterisk_colums in range(number_rows+1):
		# print("*",end= ' ')
	# for number_space_colums in range(number_rows):
		# print("*",end= ' ')
	# print("")
#----------------------------------------------------------------------#
# import os
# import time
# # take a size from user and number of repetitions
# size =int(input("input size of drawing:"))+1
# total_size=int(size *5.5)
# #Drawing by Asterisk
# for number_of_row in range(total_size):
	# if number_of_row<(size*2):
		# print("")
	# elif number_of_row>int(size*3.5):
		# print("")
	# elif number_of_row == (int (total_size/2)+1):
		# for number_colums in range(size*2):
			# print("*",end= ' ')
	# else:
		# for number_rows in range(size):
			# for number_colums in range(size-number_rows):
				# print("*",end= ' ')
		# print("")
#----------------------------------------------------------------------#
import os
import time
flag=0
#Drawing by Asterisk
os.system("cls")
while True:
	#Frist in Row
	for number_of_row in range(10):
		if number_of_row<=(3):
			print("")
		elif number_of_row>=7:
			print("")
		elif number_of_row ==5:
			for number_colums in range(6):
				if number_colums==0:
					print("")
				print("*",end= ' ')
				if number_colums==5:
					print("")
		else:
			for number_colums_1 in range(2):
				if (number_colums_1>0):
					print(" ",end= ' ')
					print("*",end= ' ')
	time.sleep(0.2)
	os.system("cls")
	#---------------------------------------------------------------#
	#Frist in colum
	for number_of_row in range(12):
		if number_of_row>=6:
			for number_colums in range(6):
				if flag==1 and number_colums==4:
					print ("* * *",end= ' ')
					flag=0
					break
				elif number_colums==5:
					print("*",end= ' ')
				elif number_colums<=5:
					print(" ",end=' ')
			if number_of_row==9:
				flag=1
			print("")
		else:
			print("")
			continue
	time.sleep(0.2)
	os.system("cls")
	#---------------------------------------------------------------#
	#Drawing by Asterisk
	#Scond in Row
	for number_of_row in range(10):
		if number_of_row<=(3):
			print("")
		elif number_of_row>=7:
			print("")
		elif number_of_row ==5:
			for number_colums in range(6*2):
				if number_colums>=6:
					print("*",end= ' ')
				elif number_colums<6:
					print(" ",end= ' ')
				elif number_colums==11:
					print("")
		else:
			if number_of_row==6:
				print("")
			for number_colums_1 in range(10):
				print(" ",end= ' ')
				if (number_colums_1>8):
					print("*",end= ' ')	
			print("")
	time.sleep(0.2)
	os.system("cls")
	#----------------------------------------------------------#
	#Scond in colum
	for number_of_row in range(6):
		for number_colums in range(6):
			if flag==1 and number_colums==4:
				print ("* * *",end= ' ')
				flag=0
				break
			elif number_colums==5:
				print("*",end= ' ')
			elif number_colums<=5:
				print(" ",end=' ')
		if number_of_row==0:
			flag=1
		print("")	
	time.sleep(0.2)
	os.system("cls")
	#-------------------------------------------------#
	