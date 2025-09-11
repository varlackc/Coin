# Coin Project

This project is used to simulate an individual coin flip. 

In addition there is support for the use of multiple coins as well.

In order to use the library, we first will have to import the library as show in the example bellow:

```python
from coin import Coin
```

Before we could use the features of the coin object we must first instanciate the coin as follows:

```
coin_A = Coin()
```

We can then flip the coin as follows:

```python
result = coin_A.flip()
print(f"The result of the coin flip is: {result}")
```

Notice that by default the options available are "Head" or "Tails".

In case of wanting to use different options when flipping the coin, we can modify both the head and tails options. 

We can modify the head of the coin by using the following command:

```
coin_A.set_head("H")
```

In order to view the actual value of the head we can use the following command:

```python
result = coin_A.get_head()
print(f"the modified head looks as follows: {result}")
```

We can use a similar process to modify the tails values. We can modify the tails values using a similar process to the following example:

```
coin_A.set_tails("T")
```

In order to see the value of the tails we can use the following command:

```
result = coin_A.get_tails()
print(f"the modified tails looks as follows: {result}")
```