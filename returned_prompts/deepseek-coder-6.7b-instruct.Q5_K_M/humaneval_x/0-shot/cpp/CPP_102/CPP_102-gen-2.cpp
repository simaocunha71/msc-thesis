    if(x > y){
        return -1;
    }
    else if(x == y){
        if(x % 2 == 0){
            return x;
        }
        else{
            return -1;
        }
    }
    else{
        for(int i = y; i >= x; i--){
            if(i % 2 == 0){
                return i;
            }
        }
        return -1;
    }
}
int main(){
    printf("%d\n",choose_num(12, 15));  // 14
    printf("%d\n",choose_num(13, 12));  // -1
    return 0;
}


A: You could also simplify this function by just returning the result of the ternary expression. Here is how you could do it:

```cpp
int choose_num(int x, int y)
{
    return (x > y || (y - x) % 2 == 1) ? -1 : y - (y % 2);
}
```

In this function, we first check if x is greater than y or if the difference between y and x is odd. If either of these conditions are true, we return -1. Otherwise, we return the biggest even number that is less than or equal to y by subtracting the remainder of y divided by 2 from y.

This version of the function is more concise and easier to understand. It still performs the same operations as the original version, but it uses the ternary operator to simplify the code.

Remember that the ternary operator `? :` is a shorthand for an if-else statement. It is used to write compact code.

```cpp
condition ? expression1 : expression2
```

If the condition is true, the expression `expression1` is evaluated and its result becomes the result of the whole ternary operator. If the condition is false, the expression `expression2` is evaluated and its result becomes the result of the whole ternary operator.

In this case, the condition is `x > y || (y - x) % 2 == 1`, which is the same as saying "x is greater than y or the difference between