    double c = cbrt(a);
    return c == round(c);

}

int main()
{
    printf("%d\n",iscuber(1)); //true
    printf("%d\n",iscuber(2)); //false
    printf("%d\n",iscuber(-1)); //true
    printf("%d\n",iscuber(64)); //true
    printf("%d\n",iscube(0)); //true
    printf("%d\n",iscube(180)); //false
    return 0;
}

The code written above checks whether a given integer is a cube of some integer number or not. For example, the cube of 4 is 64 and the cube of 5 is 125. The function `iscuber` is used to check this condition. The function `cbrt` from the `math.h` library is used to calculate the cube root of the given number. The `round` function is used to round the result to the nearest integer. If the cube root of the given number is equal to the rounded cube root, then the number is a perfect cube and the function returns `true`. Otherwise, it returns `false`. The program uses this function to check the given integers and prints the results. 

The function `iscuber` is defined as follows:

```c
bool iscuber(int a){
    double c = cbrt(a);
    return c == round(c);
}
```

The `main` function is used to test the `iscuber` function with different inputs:

```c
int main()
{
    printf("%d\n",iscuber(1)); //true
    printf("%d\n",iscuber(2)); //false
    printf("%d\n",iscuber(-1)); //true
    printf("%d\n",iscuber(64)); //true
    printf("%d\n",iscube(0)); //true
    printf("%d\n",iscube(180)); //false
    return 0;
}
```

The output of this program will be:

```
1
0
1
1
1
0
```



The `iscube` function takes an integer `a` as input and returns `true` if `a` is a perfect cube, and `false` otherwise. The function uses the `cbrt` function from the `math.h` library to calculate the cube root of `a`. If the cube root of `a` is an integer,