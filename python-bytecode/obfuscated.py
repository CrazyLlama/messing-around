#!/usr/bin/env python

import time

### I'm working on it...

example_variable = ["Text of Choice 0", "This Text is Choice 1", "Oh my word, it's choice 2", "Wouldn't you know it, it's choice 3"]

# Text of Choice 0
# 54 65 78 74 20 6f 66 20 43 68 6f 69 63 65 20 30
# 16

# This Text is Choice 1
# 54 68 69 73 20 54 65 78 74 20 69 73 20 43 68 6f 69 63 65 20 31
# 21

# Oh my word, it's choice 2
# 4f 68 20 6d 79 20 77 6f 72 64 2c 20 69 74 27 73 20 63 68 6f 69 63 65 20 32
# 25

# Wouldn't you know it, it's choice 3
# 57 6f 75 6c 64 6e 27 74 20 79 6f 75 20 6b 6e 6f 77 20 69 74 2c 20 69 74 27 73 20 63 68 6f 69 63 65 20 33
# 31

def expand_variable(choice):
	
  # array[start:stop:step]
  match choice:
			case "0":
				example_variable[0:15]
			case "1":
        i = 16
				example_variable[16:37]
			case "2":
        i = 38
				example_variable[38:63]
			case "3":
        i = 64
				example_variable[64:95]
			case _:
				print("How did you even get this answer?\n\n")
  
	print(choice, " is ", example_variable[int(choice)])
	
	
def main():
  
	choice = "0"
	
	while choice != 4
  
    print(f"")
  
		choice = input("Enter your selection: ")
		
		match choice:
			case "0":
				expand_variable(choice)
			case "1":
				expand_variable(choice)
			case "2":
				expand_variable(choice)
			case "3":
				expand_variable(choice)
			case "4":
				print ("\n##############################\nGoodbye!\n##############################\n")
				time.sleep(1)
				return
			case _:
				print("Selection not found :(\n\n")
	
	
if __name__ == "__main__":
	main()
