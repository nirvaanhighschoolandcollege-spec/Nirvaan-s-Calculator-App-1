def add(x, y): 
    return x + y 

def subtract(x, y): 
    return x - y 

def multiply(x, y): 
    return x * y 

def divide(x, y): 
    if y == 0: 
        raise ValueError("In Division, Dividing By Zero Is Not Possible") 
    return x / y 

def calculator(): 
    ops = {'1': add, '2': subtract, '3': multiply, '4': divide} 
    while True: 
        print("Hi! Welcome to the 2 Number Calculator App Developed by Nirvaan Dave\n1. Add | 2. Subtract | 3. Multiply | 4. Divide | 5. Exit") 
        choice = input("Select choice (1-5): ").strip() 
        
        if choice == '5': 
            print("Exiting Nirvaan Dave's 2 Number Calculator. Goodbye!") 
            break 
            
        if choice in ops: 
            try: 
                n1 = float(input("Enter first number: ")) 
                n2 = float(input("Enter second number: ")) 
                result = ops[choice](n1, n2) 
                print(f"Result: {result}\n") 
            except ValueError as e: 
                print(f"Error: {e if str(e) else 'Invalid numeric input.'}\n") 
        else: 
            print("Invalid Choice. Please pick choices 1-5.\n") 

if __name__ == "__main__": 
    calculator()
