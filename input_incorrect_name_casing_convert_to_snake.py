#input name
name = input("\nEnter your name: ")
#convert into lower case
lower_cased_name = name.lower()
#convert into snake case
snake_casing_name = lower_cased_name.replace(" ", "_")
#output name
print (f"\n{snake_casing_name}")