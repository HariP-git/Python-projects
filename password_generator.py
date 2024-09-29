#importing random 
import random;

print("------------------welcome to password generator !!!-------------------")

#declaring the values 

letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number=['1','2','3','4','5','6','7','8','9','0']
symbol=['!','#','@','$','^','&','*','(',')','{','}',';',':','[',']','~']

#getting how many character should be in password:

nr_letters=int(input("how many letters want to include in your password ?"))
nr_number=int(input("how many numbers want to include in your password ?"))
nr_symbol=int(input("how many symbol want to include in your password ?"))

password=[]

for char in range(1,nr_letters+1):
     password.append(random.choice(letter))
   

for no in range(1,nr_number+1):
     password.append(random.choice(number))

for sy in range(1,nr_symbol+1):
    password.append(random.choice(symbol))

#shuffling the password

random.shuffle(password)

password_list=""
for char in password:
     password_list+= char

#printing the output
     
print(f"your password is {password_list}")


                              


