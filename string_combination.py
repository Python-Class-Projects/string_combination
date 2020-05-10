'''
Write a program that asks the user to enter a word or phrase. The program will then repeatedly ask the user to enter combinations
of characters and it will report whether that combination of characters can be extracted from the origincal word or phrase. If
the search string can be found in the original string, then idicate that. If it cannot be found inside, then also indicate that
and print the new formulated string from the user's input.
'''

#Function that retrieves phrase combination and determines if the combination can be extracted from original.
def check_extraction(phrase,combination):
	list_phrase = [char for char in phrase] #will create a new list with the letters seperated from the phrase.
	list_combination = [char for char in combination] #will create a new list with the letters seperated from the combination.

	#Initializing variables before the loop to determine the shared letters from combination to phrase.
	shared_elements = [] 
	non_shared_elements = []
	for i in range(len(list_combination)):
		if list_combination[i] in list_phrase:
			shared_elements.append(list_combination[i])

		if list_combination[i] not in list_phrase:
			non_shared_elements.append(list_combination[i])

	combine_shared = "".join(shared_elements) #Joining the shared_elements to convert to a string to print.
	combine_non_shared = " ".join(non_shared_elements) #Joining the non_shared_elements to convert to a string to print.

	if len(combine_non_shared) == 0: #We know if combine_non_shared == 0, then all words from combination can be extracted.
		print("That combination can be extracted from the original.")

	else: #We let the user know that the combination can't be extracted because combine_non_shared is not empty.
		print(f"That combination cannot be extracted. There is no '{combine_non_shared}', for example.")



#Loop through game
play_again = "y"
while play_again == "y":
	phrase = input("Enter a word or phrase: ").lower() #Retrieving phrase data and storing to variable.
	print("You can now enter combinations of characters, and I'll tell you")
	print("if that combination can be found in the word you just entered.")
	combination = input("Enter character combination to find: ").lower() #Retrieving combination data and storing to variable.
	check_extraction(phrase,combination) #Calling function and sending phrase and combination to function.
	play_again = input("Again? ") #Asking user if he/she wants to play again. Will determine whether loop will continue.
	play_again = play_again.lower()

print("\nEND OF PROGRAM\n")