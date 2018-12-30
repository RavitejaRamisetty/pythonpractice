fruits=["apple","orange","grape","banana"]             #arrays are that storing the multiple values in a single variable
print(fruits)


fruits[0]="pine apple"                                 #modifying the value of the array item by using the indx number
print(fruits)


x=len(fruits)                                          #len() method is used to find the length of the array
print(x)

vegetables=["cucumber","brinjal","potato"]
for y in vegetables:                                   #to print the array elements individually "for in" loop is used
   print(y)
for z in fruits:
   print(z)


vegetables.append("tomato")                            #append() method used to add an array element in last for the existing arrays
print(vegetables)


vegetables.pop(3)                                      #pop() method is used to remove the array elements
print(vegetables)
fruits.remove("banana")                                #remove() method also is used to remove the array elements 
print(fruits)


print(fruits.copy())                                   #copy() method returns the copy of the list


print(fruits.count("orange"))
print(fruits.count("apple"))
print(vegetables.count("potato"))                      #count() method returns the number of element with specified index
print(vegetables.count("brinjal"))


fruits.extend(vegetables)                              #extend() method is used to insert the list in another list
print(fruits)


fruits.sort()                                          #sort() method is used to sort the array elements
print(fruits)