# add your code here
for (i) in range(1, 101):
    if i % 3 == 0:
        if i % 5 == 0:
            print("FIZZBUZZ")
        else:
            print("FIZZ")
    elif i % 5 == 0:
        print("BUZZ") 
    else:
