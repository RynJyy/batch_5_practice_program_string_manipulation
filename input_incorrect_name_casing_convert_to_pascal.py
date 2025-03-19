#input incorrect name casing
name = input("\nEnter your name: ")
#convert into proper casing
proper_cased_name = name.title()
#convert into pascal casing
pascal_casing_name = proper_cased_name.replace(" ", "")
#print name
print (f"\n{pascal_casing_name}")