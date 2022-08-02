calculation_to_units = 24
name_of_unit = "minutes"
minutes = 60

def days_to_units(num_of_days):
   condition_check = num_of_days >0
   print(type(condition_check))
   print(condition_check)

   if condition_check > 0:
      return f" {condition_check} days are  {condition_check * calculation_to_units * minutes} {name_of_unit}"
   else:
      return "Entered Negative value - No Conversion "

user_input = input("Enter a Number of days and I will conver to hours----> \n")

my_var = days_to_units(float(user_input))
print(my_var)