#input statement 
statement = input("\nEnter a statement: ")
#count number of words
number_of_words = len(statement.split())
#print number of words
print (f"\nNumber of words in the statement: {number_of_words}")