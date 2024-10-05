        int xNumerator = Integer.parseInt(x.split("/")[0]);
        int xDenominator = Integer.parseInt(x.split("/")[1]);
        int nNumerator = Integer.parseInt(n.split("/")[0]);
        int nDenominator = Integer.parseInt(n.split("/")[1]);

        int lcm = (xNumerator * nDenominator) / gcd(xNumerator, nDenominator);
        int gcd = gcd(lcm, xDenominator * nNumerator);
        return (lcm / gcd) * (xDenominator * nNumerator) % (nDenominator * xNumerator) == 0;
    }

    int gcd(int a, int b) {
        while (b != 0) {
            int t = b;
            b = a % b;
            a = t;
        }
        return a;
    }
}



















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
```
```

```
```
```
```
```
