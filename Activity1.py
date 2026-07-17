num_1= int(input("Plz Enter a Number: "))
num_2= int(input("Plz Enter another Number: "))
operation= input("Plz Enter The Operation: ")
try:
 if "+":
  add= num_1 + num_2
  print(add)

 elif "-":
  sub= num_1 - num_2
  print(sub)

 elif "/":
  div= num_1 / num_2
  print(div)

 elif "**":
  mul= num_1 ** num_2
  print(mul)

except ZeroDivisionError:

 print(num_1,operation,num_2,)