# Dictonaries cannot be ordered or sorted. They are retireved by key names, as oppsoed to Lists that are retrieved via locaiton. 

# This is conventient for when you want to retireve a value, without knwoing its location. 

#The trade of for lists is that you cannot easily retrieve the value, whilst dictionaries cannot be ordered or sorted. 

my_dictionary = {'key1':'value1','key2':'value2'} 
print(my_dictionary)

# You can retrieve a value by printing a key in the above code. 

print(my_dictionary['key1'])

# A good analogy for this is prices in a store. You can use dictionaries to use a food item as a key, to retireve a certain value/price. 

store_prices = {'apple': 0.80, 'orange':1}
print(store_prices['apple']) 

# Thus clearly without needing any index location, I have retrieved the needed information via key value pairs. 

# Dictionaries are very flexible in what variables they can hold. 

second_dictionary = {'key3':123, 'key4':[4,5,6], 'key5':{'test_key':100}}
print(second_dictionary['key5'])

#You can also have dictionaries within dictionaries, you can naviage using[][], inputing your original dictionary, as well as entering your 2 keys as string. 
#Keys are always represented as strings.

print(second_dictionary['key5']['test_key'])

#You can also retrieve values from a list within a dictionary too. I will try and get a value of 5 from key4 using this method now. 	

print(second_dictionary['key4'][1])

# Adding new key values to a existing dictionary is also possible. 

print(second_dictionary) 
second_dictionary['key6'] = 'Adding an extra key!'
print(second_dictionary)

# You can now see an extra dictionary has been added. 

# Overwriting an exisiting dictionary too is doable. 

second_dictionary['key3'] = 'NEW VALUE' 

print(second_dictionary)

#if you want to see all the keys of a dictionary you can you use, e.g exisiting_dictionary.keys(), and for values; exisiting_values() 

print(second_dictionary.keys())
print(second_dictionary.values()) 
 
 # You can use exisiting_dictionary.items to see your keys and values together. 
 print(second_dictionary.items())