# Python Program to Count Vowels and Consonants and words

str1 = input("Please Enter Your Sentence : ")
vowels = 0
consonants = 0
for i in str1:
    if(ord(i) == 65 or ord(i) == 69 or ord(i) == 73
       or ord(i) == 79 or ord(i) == 85
       or ord(i) == 97 or ord(i) == 101 or ord(i) == 105
       or ord(i) == 111 or ord(i) == 117):
        vowels = vowels + 1
    elif((ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90)):
        consonants = consonants + 1

CountofWords = str1.split (" ")

print ("Number of Words :",len(CountofWords))
print("Total Number of Vowels = ", vowels)
print("Total Number of Consonants = ", consonants)
