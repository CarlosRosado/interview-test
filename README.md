# Introduction 
Technical Test for interview.

# Problems

## 1. Balanced Symbols Problem

For the balanced symbols problem, a solution has been implemented in which two functions, these functions can be found in utils/common_utils.py:

- **Replace Comments:** with this function, we can remove from any string all comments stating with the character /* and ending with the character */, so that we get a string without comments.
- **Balanced symbols function:** with this function, we can calculate if the input string is balanced or not, for this function we use dictionary.

We can found this solution in the file FuncInterview/balanced_symbols.py.

## 2. Cost Prorating Problem

For the cost prorating problem, a solution has been implemented in CostProrating funcion (utils/common_utils.py). In this function, we calculate the prorating cost with input amount and list of weights. We use the formula described in the problem and enter the results in a list to calculate the cost prorating of the input amount using the given weights.

We can found this solution in the file FuncInterview/cost_prorating.py.

## 3. Water Juggs Problem

For the water juggs, we have implemented some classes and functions that can be seen in utils/juggers_utils.py:

- **TargetFound:** this class is for save steps if the target has been found.
- **Jugger:** this class is for defining a jugger its operations (empty, insert_water, fill_jugger, etc).
- **StateJugger:** this class is for state of jugger and calculate all possible operations with these.
- **JuggersGraph:** this class id for save and print the solution of jugger water problem for a input target and input juggers. the printed solution is as follows:

Solution is:<br /> 
[Jugger: 0/3, Jugger: 0/5]<br /> 
[Jugger: 0/3, Jugger: 5/5]<br /> 
[Jugger: 3/3, Jugger: 2/5]<br /> 
[Jugger: 0/3, Jugger: 2/5]<br /> 
[Jugger: 2/3, Jugger: 0/5]<br /> 
[Jugger: 2/3, Jugger: 5/5]<br /> 
[Jugger: 3/3, Jugger: 4/5]<br /> 

The first column (Jugger: 0/3) represent jugger capacity for the total and the second column represent the other jugger, for example in first line 0 because is empty and 3 the total capacity. Line by line we can see how all the juggers are being filled/empty.

We can found this solution in the file FuncInterview/water_jugs.py.

# Build and Test
For build and testing, we created a Makefile for execute all steps:
-  make env: for create environment.
-  make install (requirements.txt): for install all packages in a environment, execute this task for all requirements files.
-  make lint lint_folder=$folder: for check code quality, replace folder for FuncInterview/ or unit.
-  make run_pytest test_forder=tests/unit/: for execute test.
-  python balanced_symbols.py: for execute balanced symbols problem.
-  python cost_prorating.py: for execute cost prorating problem.
-  python water_jugs.py: for execute water juggs problem.
