def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celsius fahrenheit 
    ##################################################
    """

    celsius = int(input('Enter the number of the temperature in Celsius'))
    fahrenheit = 9/5 * celsius + 32

    print (f'Farenheit: {fahrenheit:.2f}')

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celsius, fahrenheit


if __name__ == '__main__':
    main()
