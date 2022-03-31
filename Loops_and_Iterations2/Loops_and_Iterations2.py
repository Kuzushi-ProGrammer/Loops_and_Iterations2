# (Re-write as definite loop after)                                                                 (DONE)

print('Enter five numbers, and I, Cortana, will calculate your results.')
       
numlist = [0]       # Didn't end up using as many variables as I thought

# ----------------------------------------------------------------------------------------------- #     Declaring stuff ^^^  Running stuff vvv
   
for x in range(100):                                            # Larger number than 5 to account for errors (no way someone is gonna make a mistake 100 times on a 5 input question)
    listnum = len(numlist)                                      # Assigns the value of the function len(numlist) to a variable
    numero = ('Enter a number ({}): ').format(listnum)          # Formats the output message to count what input you're on                    
    if len(numlist) <= 5:                                       # Checks if the amount of items in the list is equal to or less than 5
        print()                                                 # Extra empty line
        num = input(numero)                                     # Uses the formatted message to get input from user
        try: 
            if float(num):                                      # Executes if input *can* be converted to a float
                numlist.append(float(num))                      # Appends input (after converted to float) to number list
                print(numlist)
                
        except:                                                 # Execute if the input *cannot* be converted to a float
            print('Invalid Character - Please try again.')

    elif len(numlist) > 5:
        print('Calculating...')
        break


# ----------------------------------------------------------------------------------------------- # 
 
# numlistf = [float(x) for x in numlist]      # Converts list to float (Not actually important anymore as the input when it gets appended is converted directly)

sumlist = sum(numlist)                      # Gets sum of number list
count = len(numlist) - 1                        # Gets amount of numbers in number list (it was counting one too many for some reason)
average = sumlist / count                   # Divides sum by number count to get mean average

total = ('Total: {}').format(sumlist)           # Formatting for end text
numnum = ('Number Count: {}').format(count)
avg = ('Average: {}').format(average)

print()
print(total)
print(numnum)
print(avg)
print()

input('-Press Enter to Exit-')  # Prevents program from closing, put at end of code

