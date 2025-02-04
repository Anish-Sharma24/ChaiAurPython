# Here we will learn about how Python do memory management
# ---------------------------------------------- IMPORTANT FROM INTERVIEW PERSPECTIVE ---------------------------------------------------------------------------
# In python variable do not have any datatype only value have the datatype. Means the value we assign in memory has the datatype.
# Understanding different memory management
a = 10
b = 20
print("Showing the initially assigned value in these two variables are ","a =",a,"b =",b)
a = a+b
print ("Showing the value of a after value change",a)
print ("------------------------- Now we will understand how memory optimization is for LIST datatype -------------------------")

mylistone = [1,2,3,4,5] # referencing an list object in the memory
mylisttwo = mylistone # referencing same object in the memory with different variable
print(mylistone, mylisttwo) # this shows both veriable referencing the same list value
mylisttwo = [1,2,3,4,5] # now I assigned the same value as mylistone
print ("mylistone value",mylistone,"&","mylisttwo value",mylisttwo) # showing the same value then what is the difference?
# Now we are going to understand the difference
mylistone[1] = 22 # new value assigned at 1th position
print("mylistone value is", mylistone, "and mylisttwo value is", mylisttwo) # see the value has changed because in python when you assign new value it creates a new object in the memory everytime.
print("----------------------------------------------------------------------------------------------------------------")
L1 = [1,2,3,4,5]
L2 = L1 # referencing the same memory object or space
print('value of L1 is',L1,'value of L2 is',L2)
L1[3] = 44 # now L1 value is changed. Now it would be interesting to see what would be the L2's value.
print("L1 value now",L1)
print("L2 value now",L2)
# See both the values are same because both are pointing at the same memory object. Now it's clear that assigning the same value and referencing the same memory object are not same.