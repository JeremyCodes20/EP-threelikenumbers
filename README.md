# Project Euler- 3 like numbers
This program takes in a number and returns the number of substrings within 
said number that are divisible by 3. A more in-depth description of this 
can be found within [Plan](doc/Plan.md).  
At the moment, the program only implements the first and most simple function. I aim 
to later implement the entire problem.

### Notes
Problem is composed of three parts:  
* f(n): returns the number of non-empty substrings of n that are divisible by 3.  
  Examples- f(2573) = 3
* is_three_like(n): returns if f(n) is divisible by 3.  
  Examples- is_three_like(2573) = True
* F(d): how many d-digit numbers are 3-like  
  Examples- F(2) = 30; F(6) = 290898