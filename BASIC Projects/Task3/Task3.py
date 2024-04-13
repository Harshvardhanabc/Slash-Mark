import random
def generate_password(passwords_length):
    Lower_Alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    Upper_Alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    Num = ['1','2','3','4','5','6','7','8','9','0']
    Symbol = ['!','@','#','$','%','^','&','*','(',')','_','+','|','/','?','.','>','<',',','~']
    all_characters = Lower_Alpha + Upper_Alpha + Num + Symbol
    password = ''.join(random.sample(all_characters,passwords_length))
    return password

Number_of_passwords = int(input("How many passwords do you want to generate = "))
passwords_length = []
for i in range(1, Number_of_passwords + 1):
    Length_of_passwords = int(input("Enter length of password {0} = ".format(i)))
    if(Length_of_passwords>3):
        passwords_length.append(Length_of_passwords)

    else:
        print("Please enter length of password greater then 3 and this length is not save or generated password from this length.")


passwords = []
for i in range(len(passwords_length)):
    password_len = passwords_length[i]    
    password = generate_password(password_len)
    passwords.append(password)

for i in range(len(passwords)):
    extract = passwords[i]
    print("Password {0} : {1}".format(i+1,extract))

