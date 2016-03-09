import random

def main():
	print("Magic 8 ball predict the future!")

	# Have the user enter a question
	question = input("Enter a Yes/No question: ")
	
	
	# Replay whith a random Yes/Maybe/No response
	
	rand_value = int(random.random() * 4)

	if rand_value == 0:
		print("Yes!")
	elif rand_value == 1:
		print("Signs point to yes!")
	elif rand_value == 2:
		print("Reply hazy. Ask again.")
	else:
		print("I don't think so!")

#init
if __name__ == "__main__":
	main()
