# Program Logic

fibonacci_list=[0,1]

count=eval((input("How much fibonacci numbers you want???\n")))

if count<=0:
    print("Please enter a positive integer starting with 1.")
    
elif count==1:
    print(f"Fibonacci numbers upto {count} is:")
    print(fibonacci_list[0])
    
elif count==2:
    print(f"Fibonacci numbers upto {count} is:")
    print(fibonacci_list[0],",",fibonacci_list[1])
    
else:
    for i in range(2,count):
        fibonacci_list.append(fibonacci_list[i-1]+fibonacci_list[i-2])

    print(f"Fibonacci numbers upto {count} is:")
    print(fibonacci_list)
