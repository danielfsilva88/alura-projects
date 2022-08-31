# Python: introduction to Object Oriented Programming

## 1. The problem of procedural paradigm

- Data and functionality/behavior walks together
- Code with cohesive responsibilities

## 2. Classes and objects

### 2.1. Class and object

Class definition example:

``` python
class Conta:

    pass
```

Creating an object and checking where it was stored in memory address:

``` python
>>> from conta import Conta
>>> Conta()
<conta.Conta object at 0x10715f518>

>>> conta = Conta()
>>> conta
<conta.Conta object at  0x10715fe10>
```

### 2.2. Defining a class

1. A Class is a type specification, defining values and behaviours;
2. An object is a Class' instance, where we can define values for its attributes;
3. A good analogy to Class is a dish recipe.

### 2.3. Constructor

Object was created when the class `Conta` was called. Its memory address was stored inside variable `conta`. In OOP, those variables are called **references**.

Now, to set the class content, we're going to define its characteristics, that in OOP its called **attributes**.

To create an object and set its attributes, Python can run an automatic function inside the class. 

As a special function, it will receive a special name. Two `_` chars will be added befone and after the name of the **constructor function `init`**. In Python we have this constructor function using the method `__init__`, but in other languages like Java or C++ the constructor has the same name as the Class and its a bit different than the Python's constructor function.

So, Python will build the object, allocate a space in memory, and then call the function `__init__`, e.g.:  

``` python
class Conta:
    def __init__(self):
          print("Building the object...")

# after reload the library
>>> from conta import Conta
>>> conta = Conta()
Building the object...
```

To understand the `self` variable, we're going to use it inside print function:

``` python
class Conta:
    def __init__(self):
          print("Building the object {}...".format(self))

# after reload the library
>>> from conta import Conta
>>> conta = Conta()
Building the object <conta.Conta object at 0x00000132BA64D4F0>...
<conta.Conta object at 0x00000132BA64D4F0>
```

So, **self is the reference to find the object built in memory**.

And now that we have the reference, we're going to use it to access the object and set its attributes. We use a dot `.` to access the object and then we set the attributes that we want.

``` python
class Conta:
    def __init__(self, numero, titular, saldo, limite):
          print("Building the object {}...".format(self))
          self.numero  = numero
          self.titular = titular
          self.saldo   = saldo
          self.limite  = limite

# after reload the library
>>> from conta import Conta
>>> conta = Conta(123, "Nico", 55.4, 1000.0) 
Building the object <conta.Conta object at 0x00000174BD631F40>...
>>> conta2 = Conta(321, "Marco", 100.0, 1000.0)     
Building the object <conta.Conta object at 0x00000174BD65E520>...
>>> conta
<conta.Conta object at 0x00000174BD631F40>
>>> conta2
<conta.Conta object at 0x00000174BD65E520>
```

### 2.7. Accessing attributes

Conta() is inside a `module` - in other languages could be called `package` or `namespace` - that cuold have one or more syntaxes.

To access object attributes, we're going to use the **reference**, that is `conta` or `conta2` created earlier, plus dot `.`, plus the desired attribute:

``` python
>>> conta.saldo
55.4
>>> conta2.saldo
100.0
```

## 3. Implementing methods

### 3.1. Using methods

Now that we already have the object attributes, it's time to add what the object can "do". The functions related to the objects, specifying its "actions" is called **methods**, e.g.:

``` python
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Building the object {} ... ".format(self))
        self.numero  = numero
        self.titular = titular
        self.saldo   = saldo
        self.limite  = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.saldo, self.titular))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor

# after reload the library
>>> from conta import Conta
>>> conta = Conta(123, "Nico", 55.4, 1000.0) 
>>> conta2 = Conta(321, "Marco", 100.0, 1000.0)     
>>> conta.extrato()
Saldo de 55.4 do titular Nico
>>> conta.deposita(15.0)
>>> conta.extrato()
Saldo de 70.4 do titular Nico
>>> conta.saca(10.0)
>>> conta.extrato()
Saldo de 60.5 do titular Nico
```

### 3.2. Class method's problem

``` python
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    exibe_nome_e_sobrenome():
        print("{0} {1}".format(self.nome, self.sobrenome))


pessoa = Pessoa("Chalita", "Steppat")
pessoa.exibe_nome_e_sobrenome()
```

<details>
<summary>How many errors is there in this code?</summary>
<br>
There are two errors. This code doesn't declare method using `def` and the method doesn't receive `self` as parameter.
</details>

### 3.4. Content review

![UML class Conta example](.\auxiliary_files\3_4_UML_class_conta.PNG)

### 3.5. None and garbage collector

![object without reference example](.\auxiliary_files\3_5_object_without_reference_example.png)

The _garbage collector_ is responsible to identify those "forgotten objects", delete them, and then free the memory space to be used again.

If we want to undo a reference, we can use the special word `None` like this:

``` python
conta_test = conta # here, conta_test has the same reference as conta
conta_test = None # and here we delete this reference, but "conta" reference keeps existing
```
### 3.9. Challenge: date class

``` python
class Data:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def formatada(self):
        print("{0}/{1}/{2}".format(day, month, year)) 
```

## 4. Encapsulation

