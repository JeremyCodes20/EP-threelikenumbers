# Project Euler- 3 like numbers
This program takes in a number and returns the number of substrings within 
said number that are divisible by 3, 
as well as whether or not the number is "three-like".
Additionally, the program can determine how many numbers within a given 
"digit-range" are three-like (although this is not very efficient and will 
likely not produce results for larger numbers). 
A more in-depth description of this 
can be found within [Plan](doc/Plan.md).  

### Notes
Problem is composed of three parts:  
* f(n): returns the number of non-empty substrings of n that are divisible by 3.  
  Examples- f(2573) = 3
* is_three_like(n): returns if f(n) is divisible by 3.  
  Examples- is_three_like(2573) = True
* F(d): how many d-digit numbers are 3-like  
  Examples- F(2) = 30; F(6) = 290898
