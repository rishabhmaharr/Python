#Q: Create two tuples 1 packed and 1 unpacked, assign them values. Now change their assigned values and also access any three elements from these tuples individually and also count occurence of a specific value in the tuple. Also find the lengths of these tuples and concatenate them and repeat the joined tuple 19 times
 
packed_tuple = ("Rishabh", "Python", "Uttrakhand", "Berlin", "Germany", 4)
print("Packed Tuple:", packed_tuple)
unpacked_tuple = 76, 57, 21, 39, 10  
print("Unpacked Tuple:", unpacked_tuple)

# Access the elements from the tuples. tuples are immutable so we cannot change the values directly.Therefore we can create new tuple with new values
element1 = packed_tuple[0]  
element2 = unpacked_tuple[2]  
element3 = packed_tuple[4]  
print("Accessed Elements:", element1, element2, element3)

# Count the occurrence of a specific value
count_of_3_in_packed = packed_tuple.count(3)
print("Count of 3 in Packed Tuple:", count_of_3_in_packed)

count_of_57_in_unpacked = unpacked_tuple.count(57)
print("Count of 57 in Unpacked Tuple:", count_of_57_in_unpacked)

# Find the length of tuples
length_of_packed = len(packed_tuple)
print("Length of Packed Tuple:", length_of_packed)

length_of_unpacked = len(unpacked_tuple)
print("Length of Unpacked Tuple:", length_of_unpacked)

# Concatenate the tuples
concatenate_the_tuple = packed_tuple + unpacked_tuple
print("Concatenated Tuple:", concatenate_the_tuple)

# Repeating the concatenated tuple 19 times
repeated_tuple = concatenate_the_tuple * 19
print("Repeated Tuple:", repeated_tuple)



