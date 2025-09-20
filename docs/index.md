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

```python
result = coin_A.get_tails()
print(f"the modified tails looks as follows: {result}")
```

We also have the ability to have entire sets of coins. In order to use multiple coins we will have to declare a coin set and declare the individual coins. Then the coins can be added either individually or as a group.

The following example shows how the coins can be added individually:

```python
from coin import Coin, CoinSet
coin_A = Coin()
coin_B = Coin()
coin_set_A = CoinSet()

coin_set_A.add_coin(coin_A)
coin_set_A.add_coin(coin_B)
```

There is however a better way to add coins to a coin set. We can use the `add_coins` to add a list of coins all at once.

```python
from coin import Coin, CoinSet
coin_A = Coin()
coin_B = Coin()
coin_set_A = CoinSet()

coin_set_A.add_coins([coin_A, coin_B])
```

We can see the faces of the coins held in the `CoinSet` by using the `get_faces` method as shown in the next section:

```
coin_set_A.get_faces()
```

We can also set the faces of multiple coins using the `set_faces` method.

```
coin_set_A.set_faces(["H","H"])
```

In addition we can also flip multiple coins in one instance using the `flip` method.

```
coin_set_A.flip()
```