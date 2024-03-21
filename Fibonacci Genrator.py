def generate_fibonacci(n):
    """
      Generates the first 'n' terms of the Fibonacci sequence.
    """
    fib_sequence = [0, 1] # Initialize with the first two terms
    
    while len(fib_sequence) < n:
        
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
        
    return fib_sequence

def main():
    
    try:
        
        num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
        if num_terms <= 0:
            
            print("Please enter a positive integer.")
            return
        
        fibonacci_result = generate_fibonacci(num_terms)
        print(f"The first {num_terms} terms of the Fibonacci sequence:")
        print(fibonacci_result)
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        
if __name__ == "__main__":
 main()


#Finite Fibonacci Generator:
def fibonacci():
    a = 0
    b = 1
    for _ in range(50):  # Change range as nedded....
        print(b)
        a, b = b, a + b

obj =fibonacci()



##Infinite Fibonacci Generator:

def fibonacciGenerator():
    a = 0
    b = 1
    while True:
        yield b
        a, b = b, a + b

obj = fibonacciGenerator()
print(next(obj))  # 1
print(next(obj))  # 1
print(next(obj))  # 2
print(next(obj))  # 3
# Continue calling next(obj) to get more Fibonacci numbers
