def addition():
    print("Performing Addition")
    a=0
    n=float(input("Enter A Number : "))
    ans = n
    while True:
        m=float(input("Enter Another Number (Press 0 to Execute) : "))
        ans+=m
        a+=1
        if m==0:
            break
    print('Answer :',ans)
    print('Addition is performed on {} numbers'.format(a))
def subtraction():
    print("Performing Subtraction")
    a=0
    n=float(input("Enter A Number : "))
    ans = n
    while True:
        m=float(input("Enter Another Number (Press 0 to Execute) : "))
        ans-=m
        a+=1
        if m==0:
            break
    print('Answer :',ans)
    print('Subtraction is performed on {} numbers'.format(a))
def multiplication():
    print("Performing Multiplication")
    a=0
    n=float(input("Enter A Number : "))
    ans = n
    while True:
        m=float(input("Enter Another Number (Press 0 to Execute) : "))
        a += 1
        if m==0:
            break
        else:
            ans*=m

    print('Answer :',ans)
    print('Multiplication is performed on {} numbers'.format(a))
def division():
    print("Performing Division")
    print("You can Divide 2 Numbers only")
    n = float(input("Enter Divident : "))
    m = float(input("Enter Divisor : "))
    print("\tIn Float Format")
    ans=n/m
    print(ans)
    print("\tIn Interger form")
    ans=n//m
    print(ans)
    if n%m==0:
        print("Remainder is : 0")
    else:
        print('Remainder is : {}'.format(n%m))
def average():
    print("Finding Average")
    a=0
    n = float(input("Enter A Number : "))
    ans=n
    while True:
        m = float(input("Enter Another Number (Press 0 to Execute) : "))
        ans=ans+m
        a+=1
        if m==0:
            break
    print('Answer : {}'.format(ans/a))
    print('Averaging is performed on {} numbers'.format(a))
def multi():
    print("Performing Multiple Division")
    a = 0
    n = float(input("Enter A Number : "))
    ans = n
    while True:
        m = float(input("Enter Another Number (Press 0 to Execute) : "))
        a += 1
        if m == 0:
            break
        else:
            ans /= m
    print('Answer :', ans)
    print('Division is performed on {} numbers'.format(a))
while True:
    print('')
    print("Press 'A' for Addition")
    print("Press 'S' for Subtraction")
    print("Press 'M' for Multipication")
    print("Press 'D' for Division")
    print("Press 'MD' for Multiple Division")
    print("Press 'AVG' for Averaging")
    print("Press 'Q' to Quit")
    x=input("Enter : ").upper()
    if x!='Q':
        if x=='A':
            addition()
        elif x=='S':
            subtraction()
        elif x=='M':
            multiplication()
        elif x=='D':
            division()
        elif x=='MD':
            multi()
        elif x=='AVG':
            average()
        else:
            print("Invalid Input")
    else:
        print("Thank You !!")
        break