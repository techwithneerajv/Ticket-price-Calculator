height = int(input("What is your height ?"))
if height >= 120:
	print("You are eligible for the ride")
	age = int(input("What is your age ?"))
	if age <=12:
		print("Pay $5.")
	elif age <=18:
		print("Pay $7")
	else:
		print("Pay $12")
else:
	print("Thankyou! You are not eligible for the ride.")
