#Let's start basic: How do you comment your code? Its by adding a hashtag in the front of your sentence or word. Like this one. 

#print hello world
print("Hello World")

# Assign a value to a varibale. What is variable? Think of a variable as a storage for your assigned value that you can use throught the coding. For example: 
name = {"first name" : "Jay",
        "last name" : "Shah",
        "age" : 31,
        "spouse name" : "Heemali Patel"}
print(name)

# As you can see that the above variable has multiple values which are fortmatted using dictionary. Let's print first name and last name. 
print(name['first name'] + " " + name["last name"])

# Let's understand array. Array is the list of items in brackets. It can be an integer or a string. 
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[0]) #as you can see that [0] is the first value in the array. 
print(numbers[0:2]) #this should print 1,2