# Fizz if number is divisible by 3, buzz if the number is divisible by 5 and fizz buzz if number is divisible by both 3 and 5
def fizzbuzz(max_number):
	for number in range (1, max_number):
		If number%3 == 0  and number%5 != 0:
			print(“fizz”)
		If number%5 == 0  and number%3 != 0:
			print(“buzz”)
		If number%5 == 0  and number%3 == 0:
			print(“fizzbuzz”)
	else:
			print(“something else”)

#You are going to write a program that calculates the average student height from a List of heights.
#e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
def calcutate_average_height_from_list (student_height_list):
sum_of_all_heights = 0
list_length = 0

	for item in student_height_list:
		sum_of_all_heights += (int)item
		list_length += 1
	
	return sum_of_all_heights/list_length


#You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:
#i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

def calculate_sum_of_even_numbers(start, end):
sum_of_all_even_numbers = 0
	for number in range(start, end):
		If number % 2 ==0 :
			sum_of_all_even_numbers += number
	return sum_of_all_numbers

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word_list = ["aardvark", "baboon", "camel"]
random_word = word_list[random.randint(0,len(word_list)-1)]



#You need to write a function that checks whether if the number passed into it is a prime number or not.
def is_prime(number):
    is_prime = True
    for x in range(1, number):
        if x!=1 and x!=number and number%x == 0:
            is_prime = False
    print(str(is_prime))
 
 
is_prime(2)
is_prime(4)
is_prime(100)
is_prime(3)
is_prime(199999999)



#Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text. 
#e.g.
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
def encrypt(text, shift):
    encrypted_text = ''
    for x in text:
        index_of_char_in_alphabet_list =  alphabet.index(x)
        changed_char = alphabet[index_of_char_in_alphabet_list + shift]
        encrypted_text += changed_char
    return encrypted_text




