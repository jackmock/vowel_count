## Sloth Bytes' Newsletter Challenge June 11, 2024 ##

# "How Many Vowels"
# Create a function that takes a string and returns the number (count) of vowels in the string.


# How I'd approach this:
# Get input from user -- we could store this as its own variable; which would allow us to return the original string along with the count.
#      **Doing that extra step is unnecessary for the scope of the prompt, but it would allow that extra flair if we *did* want to go that route.
# Convert input string to lowercase- this allows us to check only for lower-case versions of the vowels
# Convert string to list
# Create counter variable
# Iterate through list and check if each item is one of the 5 (not sure if we're meant to count 'y') vowels, incrementing counter variable for vowels
# Print counter variable

def main ():

    user_input = input('Please type string: ')
    working_var = user_input.lower()
    counter = 0
    for char in working_var:
        match char:
            case 'a' | 'e' | 'i' | 'o' | 'u':
                counter += 1
    print(f'\'{user_input}\' contains {counter} vowels')

main()