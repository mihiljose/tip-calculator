#If the bill was $150.00, split between 5 people, with 12% tip. 

bill_amt = float(input("What is the bill amount?"))
tip_percentage = float(input("How many percentage do you wish to tip?"))
no_of_pple = int(input("How many people are splitting the bill?"))

bill_with_tip = ((tip_percentage/100)*bill_amt )+ bill_amt
#Each person should pay (150.00 / 5) * 1.12 = 33.6
each_pay = bill_with_tip/no_of_pple
#Format the result to 2 decimal places = 33.60
formated_tip = round(each_pay,2)

print("each person should pay: "+str(formated_tip))
 