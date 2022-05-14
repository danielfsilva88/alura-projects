# Python 3 part 1: introduction to the new language version

## 1. Introduction and Python 3 install
- functions  
  - `print()`, `help()`, `type()`
- brief explanation of dynamic typing and Snake_Case
- *string* type

## 2. Handling with user input
- comparing variables
- function `input()` and `int()` 
- handle with operations between integer and string
- differences between Python 2 and 3
- small comparison between JavaScript and Python
- *integer* type

## 3. Testing values
- bigger than `>` , small than `<`
- one line boolean check
- `if`, `else`, and `elif`
- *bool* (**True** and **False**) and *float* types

## 4. Game (jogo) sequence
- loop using `while` and enter condition
- python doesn't have `do-while`
- string composition (using format)

## 5. Iterating in a different way
- loop using `for`
- function `range(start, stop, [step])`
- `break` stops the loop immediately, `continue` jumps to next iteration
- string composition (formatting integers, floats, and dates)
  - e.g. `print("{:02d}".format(4))`, `print("{:05.2f}".format(1.5))`, or `print("{:02d}/{:02d}".format(9, 4))`
  - [string compostion documentation](https://docs.python.org/3/library/string.html#formatexamples)
- from version 3.6 and on we have **f-strings**, e.g.:
``` python
name = 'Creedence'
print(f'My name is {name.lower()}')
```

## 6. Generating random numbers
- [standard library](https://docs.python.org/3/library/)
- [built-in functions](https://docs.python.org/3/library/functions.html)
- random module: `import random`, `random.random()`, and `random.randrange(start, [stop])`
- pseudo-random concept and seed `random.seed(int)`

## 7. Level and points
- function `abs()` (math module) and `round()`
- Python 3 **Banker's rounding** (or "round half to even"), e.g.:
  - `round(2.4)` == 2; `round(2.6)` == 3; `round(2.5)` == 2 (closest even);  `round(3.5)` == 4 (closest even)
- `/` operator (float division) and `//` operator (integer division)
  - `3 / 2` == 1.5, `3 // 2` == 1

## 8. Tidying our code even better
- importing ad-hoc files and programs
  - e.g. `import advinhacao` and `import forca` from this project
- defining (`def`) and calling functions
  - parameters and return
- **Main program** vs imported program
  - **`__name__ == "__main__"`**

## 9. Comparing Python and C
- built-in functions
- main function
- compiler
- compiled language and interpreted language