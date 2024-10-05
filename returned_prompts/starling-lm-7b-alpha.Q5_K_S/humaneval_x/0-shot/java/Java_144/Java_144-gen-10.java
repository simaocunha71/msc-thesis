        int n1 = Integer.parseInt(x.substring(0, x.indexOf("/")));
        int d1 = Integer.parseInt(x.substring(x.indexOf("/") + 1));
        int n2 = Integer.parseInt(n.substring(0, n.indexOf("/")));
        int d2 = Integer.parseInt(n.substring(n.indexOf("/") + 1));

        int lcm = (n1 * d2) / gcd(n1, d2);
        int gcd = gcd(lcm / d1, lcm / d2);
        int res = (lcm / gcd) / d1;
        return (res % 1 == 0);
    }

    int gcd(int a, int b) {
        if (b == 0) return a;
        else return gcd(b, a % b);
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

``