    double num = stod(value);
    int a = floor(num);
    int b = ceil(num);
    if(num > 0){
        if(num - a < b - num)
            return a;
        else
            return b;
    }
    else{
        if(a - num < num - b)
            return a;
        else
            return b;
    }
}

int main(){
    printf("%d\n", closest_integer("10"));
    printf("%d\n", closest_integer("15.3"));
    printf("%d\n", closest_integer("14.5"));
    printf("%d\n", closest_integer("-14.5"));
    return 0;
}
```

Explanation:
The given function `closest_integer` takes a string as a parameter. 

In the function, we first convert the string to a double using `stod()`. 

Then, we find the floor and ceiling of the number using `floor()` and `ceil()`. 

If the given number is positive, we check which one is closer to the given number. If the number is closer to the floor, we return the floor, else we return the ceiling.

If the given number is negative, we again check which one is closer to the given number. If the number is closer to the floor, we return the floor, else we return the ceiling.

The `main` function is used for testing the `closest_integer` function.
*/

