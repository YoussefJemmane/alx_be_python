def perform_operation(num1, num2, operation):
    """
    Perform arithmetic operations based on the operation parameter.
    
    Parameters:
        num1 (float): First number
        num2 (float): Second number
        operation (str): Type of operation ('add', 'subtract', 'multiply', 'divide')
        
    Returns:
        float: Result of the operation or error message for division by zero
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        return num1 / num2
    else:
        return "Error: Invalid operation. Please use 'add', 'subtract', 'multiply', or 'divide'"

