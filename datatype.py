number = 67 #integer
second = 45.98 #float
greeting = "Hello there" #string
isPythonInteresting = True #boolean


#Data Structure - Multiple values stored in a single variable
cars = ["toyota", "nissan", "vw"] #special brackets for list - ordered and changeable
fruits =("banana", "apple", "mango") #Tuple - ordered nut unchangeable
countries = {"Kenya", "Tunisia", "Algeria"} #set - unordered and unchangeable
student = {
    "firstname" : "Jane",
    "age" : 25,
    "course" : "Web Development",
    "gender" : "female"
} #Dictionary - Key-value pair

print(cars)
print(fruits)
print(countries)
print(student)
print(student ["gender"])



print(number)
print(second)
print(isPythonInteresting)
print(cars)


#determining a datatype
print(type(countries))
print(type(student))

#Typecasting - converting from one data type to another
print(float(number))
print(int(second))