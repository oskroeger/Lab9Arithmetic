# Owen Kroeger
# My Own Work

def arithmetic():
    
    first_term = int(input("Enter the first term in the sequence: "))
    difference = int(input("Enter the common difference: "))
    num_terms = int(input("Enter the number of terms to generate: "))

    for i in range(num_terms):
        print(first_term)
        first_term += difference


arithmetic()