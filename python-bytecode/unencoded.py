#!/usr/bin/env python

import time

example_variable = ["Text of Choice 0", "This Text is Choice 1", "Oh my word, it's choice 2", "Wouldn't you know it, it's choice 3"]

def expand_variable(choice):
	
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
