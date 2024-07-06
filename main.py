import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, sympify, diff, integrate, solve, limit, series

def calculate_function_properties(func, x):
    # Calculate domain, range, x-intercepts, y-intercepts, derivative, integral, asymptotes, intervals of increase and decrease, critical points, extrema points, intervals of concavity, inflection points, limit, Taylor polynomial, and graph of the single-variable function
    x_symbol = symbols('x')
    func_symbol = sympify(func)
    
    # Domain
    domain = solve(func_symbol, x_symbol)
    
    # Range
    range_ = [func_symbol.subs(x_symbol, i) for i in domain]
    
    # X-intercepts
    x_intercepts = [i for i in domain if func_symbol.subs(x_symbol, i) == 0]
    
    # Y-intercepts
    y_intercepts = [func_symbol.subs(x_symbol, 0)]
    
    # Derivative
    derivative = diff(func_symbol, x_symbol)
    
    # Integral
    integral = integrate(func_symbol, x_symbol)
    
    # Asymptotes
    asymptotes = [limit(func_symbol, x_symbol, i) for i in [-float('inf'), float('inf')]]
    
    # Intervals of increase and decrease
    intervals_increase = solve(diff(func_symbol, x_symbol) > 0, x_symbol)
    intervals_decrease = solve(diff(func_symbol, x_symbol) < 0, x_symbol)
    
    # Critical points
    critical_points = solve(diff(func_symbol, x_symbol), x_symbol)
    
    # Extrema points
    extrema_points = solve(diff(diff(func_symbol, x_symbol), x_symbol), x_symbol)
    
    # Intervals of concavity
    intervals_concavity = solve(diff(diff(func_symbol, x_symbol), x_symbol) > 0, x_symbol)
    
    # Inflection points
    inflection_points = solve(diff(diff(func_symbol, x_symbol), x_symbol), x_symbol)
    
    # Limit
    limit_ = limit(func_symbol, x_symbol, float('inf'))
    
    # Taylor polynomial
    taylor_polynomial = series(func_symbol, x_symbol, 0, 10)
    
    # Graph
    try:
        plt.clf()  # Clear the canvas
        x_values = np.linspace(-10, 10, 400)
        y_values = [float(func_symbol.subs(x_symbol, i)) for i in x_values]
        plt.plot(x_values, y_values)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Graph of the function')
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"Error graphing: {str(e)}")
    
    return {
        'domain': domain,
        'range': range_,
        'x_intercepts': x_intercepts,
        'y_intercepts': y_intercepts,
        'derivative': derivative,
        'integral': integral,
        'asymptotes': asymptotes,
        'intervals_increase': intervals_increase,
        'intervals_decrease': intervals_decrease,
        'critical_points': critical_points,
        'extrema_points': extrema_points,
        'intervals_concavity': intervals_concavity,
        'inflection_points': inflection_points,
        'limit': limit_,
        'taylor_polynomial': taylor_polynomial
    }

def normal_math():
    print("Normal Math Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Exponentiation")
    print("7. Logarithm")
    print("8. Trigonometry")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 + num2
        print(f"The result is: {result}")
    elif choice == 2:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 - num2
        print(f"The result is: {result}")
    elif choice == 3:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 * num2
        print(f"The result is: {result}")
    elif choice == 4:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if num2!= 0:
            result =num1 / num2
            print(f"The result is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    elif choice == 5:
        num = float(input("Enter the number: "))
        if num >= 0:
            result = num ** 0.5
            print(f"The result is: {result}")
        else:
            print("Error: Cannot calculate the square root of a negative number.")
    elif choice == 6:
        num1 = float(input("Enter the base: "))
        num2 = float(input("Enter the exponent: "))
        if num1 > 0 and num2 >= 0:
            result = num1 ** num2
            print(f"The result is: {result}")
        else:
            print("Error: The base must be positive and the exponent must be non-negative.")
    elif choice == 7:
        num = float(input("Enter the number: "))
        if num > 0:
            base = float(input("Enter the base: "))
            if base > 0 and base!= 1:
                result = np.log(num) / np.log(base)
                print(f"The result is: {result}")
            else:
                print("Error: The base must be positive and not equal to 1.")
        else:
            print("Error: The number must be positive.")
    elif choice == 8:
        print("Trigonometry:")
        print("1. Sine")
        print("2. Cosine")
        print("3. Tangent")
        
        trig_choice = int(input("Enter your choice: "))
        
        if trig_choice == 1:
            angle = float(input("Enter the angle in degrees: "))
            result = np.sin(np.radians(angle))
            print(f"The result is: {result}")
        elif trig_choice == 2:
            angle = float(input("Enter the angle in degrees: "))
            result = np.cos(np.radians(angle))
            print(f"The result is: {result}")
        elif trig_choice == 3:
            angle = float(input("Enter the angle in degrees: "))
            result = np.tan(np.radians(angle))
            print(f"The result is: {result}")
        else:
            print("Invalid choice. Please try again.")
    else:
        print("Invalid choice. Please try again.")

def calculus():
    print("Calculus Operations:")
    print("1. Numerical Differentiation")
    print("2. Numerical Integration")
    print("3. Optimization")
    print("4. Motion Problems")
    
    calc_choice = int(input("Enter your choice: "))
    
    if calc_choice == 1:
        func = input("Enter the function (in the format 'x**2 + 3*x + 2'): ")
        x = float(input("Enter the point: "))
        h = float(input("Enter the step size: "))
        func_symbol = sympify(func)
        derivative = (func_symbol.subs(x, x + h) - func_symbol.subs(x, x)) / h
        print(f"The derivative at x = {x} is: {derivative}")
    elif calc_choice == 2:
        func = input("Enter the function (in the format 'x**2 + 3*x + 2'): ")
        a = float(input("Enter the lower limit: "))
        b = float(input("Enter the upper limit: "))
        n = int(input("Enter the number of subintervals: "))
        func_symbol = sympify(func)
        integral = 0
        dx = (b - a) / n
        for i in range(n):
            x = a + i * dx
            integral += func_symbol.subs(x, x) * dx
        print(f"The approximate value of the integral is: {integral}")
    elif calc_choice == 3:
        func = input("Enter the function (in the format 'x**2 + 3*x + 2'): ")
        x = symbols('x')
        func_symbol = sympify(func)
        constraint = input("Enter the constraint (in the format 'x >= 0'): ")
        constraint_symbol = sympify(constraint)
        result = solve((func_symbol, constraint_symbol), x)
        print(f"The optimal value is: {result}")
    elif calc_choice == 4:
        print("Motion Problems:")
        print("1. Distance and Displacement")
        print("2. Velocity and Acceleration")
        
        motion_choice = int(input("Enter your choice: "))
        
    elif calc_choice == 4:
        print("Motion Problems:")
        print("1. Distance and Displacement")
        print("2. Velocity and Acceleration")
        
        motion_choice = int(input("Enter your choice: "))
        
        if motion_choice == 1:
            s = input("Enter the position function (in the format 't**2 + 3*t + 2'): ")
            t = float(input("Enter the time: "))
            s_symbol = sympify(s)
            distance = s_symbol.subs('t', t)
            print(f"The distance at t = {t} is: {distance}")
        elif motion_choice == 2:
            v = input("Enter the velocity function (in the format 't**2 + 3*t + 2'): ")
            t = float(input("Enter the time: "))
            v_symbol = sympify(v)
            velocity = v_symbol.subs('t', t)
            print(f"The velocity at t = {t} is: {velocity}")
        else:
            print("Invalid choice. Please try again.")

def money_conversion():
    print("Money Conversion:")
    print("1. US Dollar to Other Currencies")
    print("2. Other Currencies to US Dollar")
    print("3. Other Currencies to Other Currencies")
    
    conversion_choice = int(input("Enter your choice: "))
    
    if conversion_choice == 1:
        amount = float(input("Enter the amount in US Dollars: "))
        currency = input("Enter the currency (in the format 'EUR' for Euro): ")
        if currency == "EUR":
            result = amount * 0.83
            print(f"The equivalent amount in Euros is: {result}")
        elif currency == "GBP":
            result = amount * 0.73
            print(f"The equivalent amount in British Pounds is: {result}")
        elif currency == "JPY":
            result = amount * 110.52
            print(f"The equivalent amount in Japanese Yen is: {result}")
        elif currency == "CNY":
            result = amount * 6.37
            print(f"The equivalent amount in Chinese Yuan is: {result}")
        elif currency == "AUD":
            result = amount * 1.31
            print(f"The equivalent amount in Australian Dollars is: {result}")
        elif currency == "CAD":
            result = amount * 1.23
            print(f"The equivalent amount in Canadian Dollars is: {result}")
        elif currency == "CHF":
            result = amount * 0.92
            print(f"The equivalent amount in Swiss Francs is: {result}")
        elif currency == "HKD":
            result = amount * 7.85
            print(f"The equivalent amount in Hong Kong Dollars is: {result}")
        elif currency == "INR":
            result = amount * 74.83
            print(f"The equivalent amount in Indian Rupees is: {result}")
        elif currency == "MXN":
            result = amount * 20.64
            print(f"The equivalent amount in Mexican Pesos is: {result}")
        elif currency == "NZD":
            result = amount * 1.43
            print(f"The equivalent amount in New Zealand Dollars is: {result}")
        elif currency == "RUB":
            result = amount * 74.15
            print(f"The equivalent amount in Russian Rubles is: {result}")
        elif currency == "SGD":
            result = amount * 1.35
            print(f"The equivalent amount in Singapore Dollars is: {result}")
        elif currency == "ZAR":
            result = amount * 14.35
            print(f"The equivalent amount in South African Rand is: {result}")
        else:
            print("Invalid currency. Please try again.")
    elif conversion_choice == 2:
        amount = float(input("Enter the amount in the foreign currency: "))
        currency = input("Enter the currency (in the format 'EUR' for Euro): ")
        if currency == "EUR":
            result = amount / 0.83
            print(f"The equivalent amount in US Dollars is: {result}")
        elif currency == "GBP":
            result = amount / 0.73
            print(f"The equivalent amount in US Dollars is: {result}")
        elif currency == "JPY":
            result = amount / 110.52
            print(f"The equivalent amount in US Dollars is: {result}")
        elif currency == "CNY":
            result = amount / 6.37
            print(f"The equivalent amount in US Dollars is: {result}")
        elif currency == "AUD":
            result = amount / 1.31
            print(f"The equivalent amount in US Dollars is: {result}")
        elif currency == "CAD":
            result = amount / 1.23
            print(f"The equivalent amount in US Dollars is: {result}")
        elif currency == "CHF":
            result = amount / 0.92
            print(f"The equivalent amount in US Dollars is: {result}")
        elif currency == "HKD":
            result = amount / 7.85
            print(f"The equivalent amount in US Dollars is: {result}")
        elif currency == "INR":
            result = amount / 74.83
            print(f"The equivalent amount in US Dollars is: {result}")
        elif currency == "MXN":
            result = amount / 20.64
            print(f"The equivalent amount in US Dollars is: {result}")
        elif currency == "NZD":
            result = amount / 1.43
            print(f"The equivalent amount in US Dollars is: {result}")
        elif currency == "RUB":
            result = amount / 74.15
            print(f"The equivalent amount in US Dollars is: {result}")
        elif currency == "SGD":
            result = amount / 1.35
            print(f"The equivalent amount in US Dollars is: {result}")
        elif currency == "ZAR":
            result = amount / 14.35
            print(f"The equivalent amount in US Dollars is: {result}")
        else:
            print("Invalid currency. Please try again.")
    elif conversion_choice == 3:
        amount = float(input("Enter the amount in the foreign currency: "))
        currency_from = input("Enter the currency you want to convert from (in the format 'EUR' for Euro): ")
        currency_to = input("Enter the currency you want to convert to (in the format 'GBP' for British Pounds): ")
        if currency_from == "EUR" and currency_to == "GBP":
            result = amount * 0.83 * 1.22
            print(f"The equivalent amount in British Pounds is: {result}")
        elif currency_from == "EUR" and currency_to == "JPY":
            result = amount * 0.83 * 110.52
            print(f"The equivalent amount in Japanese Yen is: {result}")
        elif currency_from == "GBP" and currency_to == "CNY":
            result = amount * 1.22 * 6.37
            print(f"The equivalent amount in Chinese Yuan is: {result}")
        elif currency_from == "JPY" and currency_to == "EUR":
            result = amount / 110.52 / 0.83
            print(f"The equivalent amount in Euros is: {result}")
        elif currency_from == "JPY" and currency_to == "GBP":
            result = amount / 110.52 * 1.22
            print(f"The equivalent amount in British Pounds is: {result}")
        elif currency_from == "JPY" and currency_to == "CNY":
            result = amount / 110.52 * 6.37
            print(f"The equivalent amount in Chinese Yuan is: {result}")
        elif currency_from == "CNY" and currency_to == "EUR":
            result = amount / 6.37 / 0.83
            print(f"The equivalent amount in Euros is: {result}")
        elif currency_from == "CNY" and currency_to == "GBP":
            result = amount / 6.37 * 1.22
            print(f"The equivalent amount in British Pounds is: {result}")
        elif currency_from == "CNY" and currency_to == "JPY":
            result = amount / 6.37 * 110.52
            print(f"The equivalent amount in Japanese Yen is: {result}")
        elif currency_from == "AUD" and currency_to == "EUR":
            result = amount / 1.31 / 0.83
            print(f"The equivalent amount in Euros is: {result}")
        elif currency_from == "AUD" and currency_to == "GBP":
            result = amount / 1.31 * 1.22
            print(f"The equivalent amount in British Pounds is: {result}")
        elif currency_from == "AUD" and currency_to == "JPY":
            result = amount / 1.31 * 110.52
            print(f"The equivalent amount in Japanese Yen is: {result}")
        elif currency_from == "AUD" and currency_to == "CNY":
            result = amount / 1.31 * 6.37
            print(f"The equivalent amount in Chinese Yuan is: {result}")
        elif currency_from == "CAD" and currency_to == "EUR":
            result = amount / 1.23 / 0.83
            print(f"The equivalent amount in Euros is: {result}")
        elif currency_from == "CAD" and currency_to == "GBP":
            result = amount / 1.23 * 1.22
            print(f"The equivalent amount in British Pounds is: {result}")
        elif currency_from == "CAD" and currency_to == "JPY":
            result = amount / 1.23 * 110.52
            print(f"The equivalent amount in Japanese Yen is: {result}")
        elif currency_from == "CAD" and currency_to == "CNY":
            result = amount / 1.23 * 6.37
            print(f"The equivalent amount in Chinese Yuan is: {result}")
        elif currency_from == "CHF" and currency_to == "EUR":
            result = amount / 0.92 / 0.83
            print(f"The equivalent amount in Euros is: {result}")
        elif currency_from == "CHF" and currency_to == "GBP":
            result = amount / 0.92 * 1.22
            print(f"The equivalent amount in British Pounds is: {result}")
        elif currency_from == "CHF" and currency_to == "JPY":
            result = amount / 0.92 * 110.52
            print(f"The equivalent amount in Japanese Yen is: {result}")
        elif currency_from == "CHF" and currency_to == "CNY":
            result = amount / 0.92 * 6.37
            print(f"The equivalent amount in Chinese Yuan is: {result}")
        elif currency_from == "HKD" and currency_to == "EUR":
            result = amount / 7.85 / 0.83
            print(f"The equivalent amount in Euros is: {result}")
        elif currency_from == "HKD" and currency_to == "GBP":
            result = amount / 7.85 * 1.22
            print(f"The equivalent amount in British Pounds is: {result}")
        elif currency_from == "HKD" and currency_to == "JPY":
            result = amount / 7.85 * 110.52
            print(f"The equivalent amount in Japanese Yen is: {result}")
        elif currency_from == "HKD" and currency_to == "CNY":
            result = amount / 7.85 * 6.37
            print(f"The equivalent amount in Chinese Yuan is: {result}")
        elif currency_from == "INR" and currency_to == "EUR":
            result = amount / 74.83 / 0.83
            print(f"The equivalent amount in Euros is: {result}")
        elif currency_from == "INR" and currency_to == "GBP":
            result = amount / 74.83 * 1.22
            print(f"The equivalent amount in British Pounds is: {result}")
        elif currency_from == "INR" and currency_to == "JPY":
            result = amount / 74.83 * 110.52
            print(f"The equivalent amount in Japanese Yen is: {result}")
        elif currency_from == "INR" and currency_to == "CNY":
            result = amount / 74.83 * 6.37
            print(f"The equivalent amount in Chinese Yuan is: {result}")
        elif currency_from == "MXN" and currency_to == "EUR":
            result = amount / 20.64 / 0.83
            print(f"The equivalent amount in Euros is: {result}")
        elif currency_from == "MXN" and currency_to == "GBP":
            result = amount / 20.64 * 1.22
            print(f"The equivalent amount in British Pounds is: {result}")
        elif currency_from == "MXN" and currency_to == "JPY":
            result = amount / 20.64 * 110.52
            print(f"The equivalent amount in Japanese Yen is: {result}")
        elif currency_from == "MXN" and currency_to == "CNY":
            result = amount / 20.64 * 6.37
            print(f"The equivalent amount in Chinese Yuan is: {result}")
        elif currency_from == "NZD" and currency_to == "EUR":
            result = amount / 1.43 / 0.83
            print(f"The equivalent amount in Euros is: {result}")
        elif currency_from == "NZD" and currency_to == "GBP":
            result = amount / 1.43 * 1.22
            print(f"The equivalent amount in British Pounds is: {result}")
        elif currency_from == "NZD" and currency_to == "JPY":
            result = amount / 1.43 * 110.52
            print(f"The equivalent amount in Japanese Yen is: {result}")
        elif currency_from == "NZD" and currency_to == "CNY":
            result = amount / 1.43 * 6.37
            print(f"The equivalent amount in Chinese Yuan is: {result}")
        elif currency_from == "RUB" and currency_to == "EUR":
            result = amount / 74.15 / 0.83
            print(f"The equivalent amount in Euros is: {result}")
        elif currency_from == "RUB" and currency_to == "GBP":
            result = amount / 74.15 * 1.22
            print(f"The equivalent amount in British Pounds is: {result}")
        elif currency_from == "RUB" and currency_to == "JPY":
            result = amount / 74.15 * 110.52
            print(f"The equivalent amount in Japanese Yen is: {result}")
        elif currency_from == "RUB" and currency_to == "CNY":
            result = amount / 74.15 * 6.37
            print(f"The equivalent amount in Chinese Yuan is: {result}")
        elif currency_from == "SGD" and currency_to == "EUR":
            result = amount / 1.35 / 0.83
            print(f"The equivalent amount in Euros is: {result}")
        elif currency_from == "SGD" and currency_to == "GBP":
            result = amount / 1.35 * 1.22
            print(f"The equivalent amount in British Pounds is: {result}")
        elif currency_from == "SGD" and currency_to == "JPY":
            result = amount / 1.35 * 110.52
            print(f"The equivalent amount in Japanese Yen is: {result}")
        elif currency_from == "SGD" and currency_to == "CNY":
            result = amount / 1.35 * 6.37
            print(f"The equivalent amount in Chinese Yuan is: {result}")
        elif currency_from == "ZAR" and currency_to == "EUR":
            result = amount / 14.35 / 0.83
            print(f"The equivalent amount in Euros is: {result}")
        elif currency_from == "ZAR" and currency_to == "GBP":
            result = amount / 14.35 * 1.22
            print(f"The equivalent amount in British Pounds is: {result}")
        elif currency_from == "ZAR" and currency_to == "JPY":
            result = amount / 14.35 * 110.52
            print(f"The equivalent amount in Japanese Yen is: {result}")
        elif currency_from == "ZAR" and currency_to == "CNY":
            result = amount / 14.35 * 6.37
            print(f"The equivalent amount in Chinese Yuan is: {result}")
        else:
            print("Invalid currency. Please try again.")
    else:
        print("Invalid conversion choice. Please try again.")

def main():
    while True:
        print("Dolphys")
        print("Made By VelCT")
        print("Calculator Menu:")
        print("1. Function Calculator")
        print("2. Normal Math Operations")
        print("3. Calculus")
        print("4. Money Conversion")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            func = input("Enter the function (in the format 'x**2 + 3*x + 2'): ")
            x = symbols('x')
            properties = calculate_function_properties(func, x)
            print("Properties of the function:")
            for key, value in properties.items():
                print(f"{key.capitalize()}: {value}")
        elif choice == 2:
            normal_math()
        elif choice == 3:
            calculus()
        elif choice == 4:
            money_conversion()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()