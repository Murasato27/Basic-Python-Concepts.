# Print Formatting -  

print('This is a string {}'.format('okay.'))
print(" The world is {2}, {0} and {1}".format("lean", "mean.", "cruel"))
print('The {f} {b} {q}'.format(f='fox', b='brown', q='quick'))

# Float Formatting - 

result = 100/777 
print('The result was {r}'.format(r=result))

# Value:Width:Precisionf. (Mainly dealing with 'Precision'), as the width value only adds white space.  

print('The result was {r:1.3f}'.format(r=result)) # Variable inserted to 3 decimal places. 	

#fstrings, alternative to the .format method. 	

name = 'Andrew'
print(f'Hello my name is {name}') #This works with multiple variables (strings, integers, floats.)
age = 18
weight = 100.5
print(f'{name} is {age} years old; and can deadlift {weight} kilograms')  