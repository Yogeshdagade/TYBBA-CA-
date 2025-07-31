dict={'mon':1,'sun':2,'tue':3,}
print("The given dictonary:",dict)
check_key=input("Enter key to check:")
check_value= input("Enter value:")
if check_key in dict:
    print(check_key,"is present.")
    dict.pop(check_key)
    dict[check_key]=check_value
else:
    print(check_key,"is not present")
    dict[check_key]=check_value
    print("Updated dictionary: ",dict)
