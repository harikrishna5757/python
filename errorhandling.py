def error_handling(number):
    try:
        result = 10 / number
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError:
        print("Invalid input")
    else:
        print("Division successful, result:", result)
    finally:
        print("This block is always executed")


error_handling(0)
error_handling(2)
error_handling(1)
