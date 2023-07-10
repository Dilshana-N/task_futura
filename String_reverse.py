a = input("Enter the string : ")
rev = ""
for i in range(len(a),0,-1):
    rev = rev + a[i-1]
print("Reverse of your string :",rev)