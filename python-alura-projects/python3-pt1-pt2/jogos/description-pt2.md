# Python 3 part 2: progressing in language

## 1. Preparing the Hangman Game (forca)
- *Truth Value Testing*
``` python
>>> bool(0)
False
>>> bool("")
False
>>> bool(None)
False
>>> bool(1)
True
>>> bool(-100)
True
>>> bool(13.5)
True
>>> bool("test")
True
>>> bool(True)
True
```

## 2. Handling strings
- function `str.find(char,[start index])`, e.g.
- iterating over the string
- functions `str.lower()`, `str.upper()`, `str.capitalize()`, `str.strip()` (strip removes space in start and end of string, and also special characters - like `\n`)
- **Python strings are immutable! Immutable sequences!**

## 3. Knowing and working with lists
- data structure: list `[]`; [documentation](https://docs.python.org/3.6/library/stdtypes.html#sequence-types-list-tuple-range)
- **List is a mutable sequence type!** [Documentation](https://docs.python.org/3.6/library/stdtypes.html#mutable-sequence-types)
- `index` (`list[index]` or `index in list`)
- `min(list)`, `max(list)`, `len(list)`, `del(list[index])`
- `list.append(element)`, `list.pop(index)`, `list.count(element)`, `list.index(element)`

## 4. Knowing and working with tuples and sets
### tuples
- data structure: tuple `()`; [documentation](https://docs.python.org/3.6/library/stdtypes.html#sequence-types-list-tuple-range)
- **tuple is a immutable sequence!** We can't add or remove elements.
- `index` (`tuple[index]`)
- `len(tuple)`, `max(tuple)`, `min(tuple)` (**these functions works with any sequence type, as string, range, list or tuple**)
- function `tuple(sequence)` turn a mutable sequence into a immutable one
- function `list(sequence)` can do the same as above, but on backwards

### sets
- data structure: set `{}`; 
- **set doesn't allow duplicated elements**, tuple and list allows 
- you can add values using `set.add(element)`
- you can't add a repeated value, e.g
```python
test_set = {11122233344, 22233344455, 33344455566}
test_set.add(44455566677) # works and add a value
test_set.add(11122233344) # doesn't work, despite don't give you any error 
print(test_set)
```
- **set doesn't have an index!** So, **set is not a sequence!** 
- you can loop a set, but the elements are printed without order (after all, it doesn't have an index)

### dictionaries
- just a brief presentation about it
- dict is implemented like a set `{}` and is always implemented with a pair of values and a **colon** between it
- example:
``` python
instructors = {'Nico' : 39, 'Flavio': 37, 'Marcos' : 30}
```

## 5. Implementing game closure
- **list comprehension**: `[x for x in list]`
  
## 6. Writing and reading files
- built-in function `var_file = open(filename, mode)`
    - mode "w" creates or overwrites a file
    - mode "a" appends to a file
    - mode "r" reads a file 
    - mode "b" to works with binary, e.g. `img = open("photo.jpg", "rb") `
- function `var_file.write(something)`; when writes a string, this function returns number of characters that it was written into file 
- function `var_file.close()`
- function `var_file.read()` and `var_file.readine()`
- function `with`

## 7. Improving the code and its presentation
- Python convention to naming functions: **snake_case**
- breaking a large complex function into small functions is a good practice because:
  - Maintaining code is easier: examine some small blocks is easier to understand than one large block of code;
  - Leaving each function with fewer responsibilities: the ideal goal is each function have only one responsibility;
  - Easier to test: if we have several small functions, we can test one by one for errors;
  - readability: giving semantic names to the functions clearify what part of code should do and facilitate understanding of the whole.

- functions with default parameter, so the parameter when calling the function becomes optional
- named parameters 