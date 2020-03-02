secret_word = "hop"
print(" Hint= Beer shampoo is made up of Barley and ____")
guess = ""
guess_count = 0
guess_limit = 4
out_of_guesses = False
while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
    	guess = input(" Enter the secret word:-")
    	guess_count += 1
    else:
    	out_of_guesses = True
	
if out_of_guesses:
	print("Out of guess, You Lose!")
else:
    print("you win!")