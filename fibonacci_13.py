#Ask the user for the number of Fibonacci numbers, they want to generate.

num = int(input("Enter n "))
#Initialise the list containing the Fibonacci sequence
fibonacci_sequence = [1]
#If-else condition as the pattern for Fibonacci sequence comes into play number 2 onwards

if num == 1:
    print(fibonacci_sequence)

else:
    #Else takes care of the situation when 2 numbers are to be generated or when more than 2 are to be generated.

    fibonacci_sequence.append(1)
    if num ==2:
        print(fibonacci_sequence)
    else:
        #We run a recursive loop to generate numbers.

        for i in range(num-2):
            fibonacci_sequence.append(fibonacci_sequence[-2]+fibonacci_sequence[-1])
        print(fibonacci_sequence)