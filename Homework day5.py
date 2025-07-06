# You have 2 strings "I am learning Python" & "Python is easier to learn as compared to Java"
#  you need to: 
#  1. Join these strings. 
# 2. Extract any 2 substrings out of the joined string without: 
#  a) Usage of Stop Value 
#  b) Usage of Start Value 
#  3. Check what happens if you set the step value as 9 
#  4. From the String "Python is easier to learn as compared to Java" find the -1 index value and note your answer. 
#  5. Convert each string into upper case. 
#  6. Replace "Python" with "Java" and vice versa in individual strings.

string1 = "I am learning Python"
string2 = "Python is easier to learn as compared to Java"

# Join these strings.
joined_string = string1 + " " + string2
print(joined_string)

# Extract any 2 substrings out of the joined string without:
# a) Usage of Stop Value
substring1 = joined_string[5:]
print(substring1)

# b) Usage of Start Value
substring2 = joined_string[:20]
print(substring2)

# Check what happens if you set the step value as 9 
step_string = joined_string[::9]
print(step_string)

# 4. From the String "Python is easier to learn as compared to Java" find the -1 index value and note your answer. 
print(string2[-1])

#  5. Convert each string into upper case. 
print(string1.upper())
print(string2.upper())







