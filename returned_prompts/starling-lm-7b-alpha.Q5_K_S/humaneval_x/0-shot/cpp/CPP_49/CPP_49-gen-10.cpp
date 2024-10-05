    if(n == 0)
        return 1;
    int r = modp(n/2,p);
    r = (r*r)%p;
    if(n%2 == 1)
        r = (r*p)%p;
    return r;
}

/*
Return 2^n modulo p (be aware of numerics).
>>> modp(3, 5)
3
>>> modp(1101, 101)
2
>>> modp(0, 101)
1
>>> modp(3, 11)
8
>>> modp(100, 101)
1
*/
int modp(int n,int p){
    if(n == 0)
        return 1;
    int r = modp(n/2,p);
    r = (r*r)%p;
    if(n%2 == 1)
        r = (r*p)%p;
    return r;
}

*/

In the above code, I'm trying to implement a function that can calculate 2^n modulo p. However, I'm getting an error in the line `r = (r*r)%p;` saying:

```
error: invalid operands to binary % (type 'int' is not same as type 'int [1]')
```

I don't understand the error as I'm trying to calculate the modulo of the product of r and r.

I have tried to define the modulo operation as follows:

```
inline int mod(int a, int b) { return a%b; }
```

and use it in the function like this:

```
int modp(int n,int p){
    if(n == 0)
        return 1;
    int r = modp(n/2,p);
    r = mod(r*r,p);
    if(n%2 == 1)
        r = mod(r*p,p);
    return r;
}
```

But I'm getting the same error.

I also