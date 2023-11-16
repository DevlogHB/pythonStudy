from art import logo

print(logo);

# 더하기
def add(num1, num2):
    return num1 + num2;

# 빼기
def subtract(num1, num2):
    return num1 - num2;

# 곱하기
def multiply(num1, num2):
    return num1 * num2;

# 나누기
def divide(num1, num2):
    return num1 / num2;

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
};

def calculator():
    num1 = float(input("What's the first number?: "));

    for operation in operations:
        print(operation);

    should_continue = True;
    # 사용자가 n 입력시 종료
    while should_continue:
        operation_symbol = input("Pick an operation: ");
        num2 = float(input("What's the sccond number?: "));

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2); # 함수처리 방식
        print(f"{num1} {operation_symbol} {num2} = {answer}");

        if input(f"Type 'y' to continue calculating wiht {answer}: , or type 'n' to start a new calculation: ").lower() == "y":
            num1 = answer; 
        else:
            should_continue = False;
            calculator();

calculator();