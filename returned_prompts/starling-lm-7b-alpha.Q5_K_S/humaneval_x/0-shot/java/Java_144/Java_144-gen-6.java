    int numX,denX,numN,denN;
    numX = Integer.parseInt(x.substring(0, x.indexOf('/')));
    denX = Integer.parseInt(x.substring(x.indexOf('/') + 1));
    numN = Integer.parseInt(n.substring(0, n.indexOf('/')));
    denN = Integer.parseInt(n.substring(n.indexOf('/') + 1));

    if(numN * denX % denN == 0) return true;
    return false;

    }
}















```
Here is a function that implements the solution to this problem.

The function first takes the numerator and denominator of the first fraction (x) and converts them to integers. Then it does the same for the second fraction (n).

Next, it uses the modulo operator to check if the product of the numerator of the second fraction and the denominator of the first fraction, divided by the denominator of the second fraction, is 0. If it is, then the product of the two fractions is a whole number and the function returns true. Otherwise, it returns false.

This solution has a time complexity of O(1) because it only performs a constant amount of arithmetic operations.
```

```
```

```
```

```
```

```
```

```
```
```