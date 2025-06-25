def filter_even_numbers(numbers):
    """
    Returns a list of even numbers from the given list.

    Args:
        numbers (list): List of integers.

    Returns:
        list: List containing only even integers.
    """
    return [num for num in numbers if num % 2 == 0]

#I need to write a function to converto celsius to fahrenheit
def celsius_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit.

    Args:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.
    """
    return (celsius * 9/5) + 32

# now I need to write a function to convert fahrenheit to celsius
def fahrenheit_to_celsius(fahrenheit):  
    """
    Converts Fahrenheit to Celsius.

    Args:
        fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Celsius.
    """
    return (fahrenheit - 32) * 5/9