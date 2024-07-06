<h1>Dolphys: The Last Calculator You'll Ever Need.</h1>

Welcome to Dolphys, a powerful command-line python calculator that can perform a wide range of mathematical operations, from simple arithmetic to advanced calculus and currency conversions.

Features
--------

* Function Calculator: Calculate the properties of a single-variable function, including its domain, range, x-intercepts, y-intercepts, derivative, integral, asymptotes, intervals of increase and decrease, critical points, extrema points, intervals of concavity, inflection points, limit, and Taylor polynomial.
* Normal Math Operations: Perform basic arithmetic operations such as addition, subtraction, multiplication, division, square root, exponentiation, logarithm, and trigonometry.
* Calculus: Perform numerical differentiation, numerical integration, optimization, and motion problems.
* Money Conversion: Convert between different currencies, including USD, EUR, GBP, JPY, CNY, AUD, CAD, CHF, HKD, INR, MXN, NZD, RUB, SGD, and ZAR.

How to Use
-----------

1. Run the program and select an option from the menu:
	* Function Calculator
	* Normal Math Operations
	* Calculus
	* Money Conversion
	* Exit
2. Follow the prompts to enter the required information, such as the function or numbers to operate on.
3. The program will display the results of the calculation.

How it Works (Code Overview)
-----------------------------

The Dolphys calculator is written in Python and uses several libraries to perform its calculations:

* `sympy` for symbolic mathematics (Function Calculator and Calculus)
* `numpy` for numerical computations (Calculus and Money Conversion)
* `matplotlib` for plotting graphs (Function Calculator)

The program is structured as follows:

* `main.py`: The main entry point of the program, which displays the menu and handles user input.
* `function_calculator.py`: Contains the implementation of the Function Calculator, which uses `sympy` to calculate the properties of a single-variable function.
* `normal_math_operations.py`: Contains the implementation of the Normal Math Operations, which uses basic Python arithmetic operations.
* `calculus.py`: Contains the implementation of the Calculus module, which uses `numpy` and `sympy` to perform numerical differentiation, numerical integration, optimization, and motion problems.
* `money_conversion.py`: Contains the implementation of the Money Conversion module, which uses `numpy` to perform currency conversions.

When the user selects an option from the menu, the corresponding module is called and executed. The module then prompts the user for the required input and performs the calculation using the relevant library. The results are then displayed to the user.

Credits/Licensing
----------------

Dolphys was made by VelCT. It is an open source software licensed under the GPL-2.0 license.
