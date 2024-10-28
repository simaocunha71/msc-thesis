        int a = interval1.get(1);
        int b = interval2.get(0);
        int c = interval2.get(1);
        int d = interval1.get(0);
        if (a > c || b > d) {
            return "NO";
        }
        int e = c - d;
        if (e == 1) {
            return "YES";
        }
        for (int i = 2; i * i <= e; ++i) {
            if (e % i == 0) {
                return "NO";
            }
        }
        return "YES";
    }
}

































```

ANSWER:
NO

EXPLANATION:
The length of intersection of these two intervals is 1, which is not a prime number.

*/

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

``