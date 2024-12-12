string=input("Enter the string to check whether the given string is palindrome or not")

rev_string=string[::-1]
if rev_string==string:
    print("Palindrome")
else:
    print("Not palindrome")
