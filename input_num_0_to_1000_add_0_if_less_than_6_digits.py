#input num
num = input("\nEnter a number between 0 and 1000: ")
#if num is less than 6 digits add 0 to the left of the number to complete 6 digits
if len(num) < 6:
    num = '0' + num
    #output num
    print (f"\n{num}")
#print num if 6 digits
else:
    print (f"\n{num}")