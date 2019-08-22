#check BMI
weight=input('Please enter your wt in kg : ')
height_feet_and_inches=input('Please enter youe ht in feet and inches :eg 5feet9inch as 5.9 : ')
#feet and inches to meter
height_in_m=0.304* float(height_feet_and_inches)
#calculate BMI
bmi=float(weight)/float(height_in_m*height_in_m)

if bmi  <=18.5:
    print('You are Under weight as your bmi is {}'.format(bmi))
elif (bmi >=18.5) and (bmi <=24.9):
     print('Perfect!You have normal weight and your bmi is {}'.format(bmi))
elif (bmi >=25) and (bmi <=29.9):
     print('You are Overweight as your bmi is {}'.format(bmi))
elif bmi>=30:
     print('You are highly obese as your bmi is {}'.format(bmi))
else :
     print('Renter properly')