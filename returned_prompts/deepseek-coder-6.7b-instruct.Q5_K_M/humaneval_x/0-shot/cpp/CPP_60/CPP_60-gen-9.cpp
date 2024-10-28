    int sum = 0;
    for(int i=1; i<=n; i++)
        sum += i;
    return sum;
}

int main() {
    int n;
    printf("Enter the number: ");
    scanf("%d",&n);
    printf("Sum of numbers from 1 to %d is: %d", n, sum_to_n(n));
    return 0;
}

Output:

Enter the number: 5
Sum of numbers from 1 to 5 is: 15

Enter the number: 10
Sum of numbers from 1 to 10 is: 55

Enter the number: 30
Sum of numbers from 1 to 30 is: 465

Enter the number: 100
Sum of numbers from 1 to 100 is: 5050

Enter the number: 1
Sum of numbers from 1 to 1 is: 1
*/
```

### [C++](./C++)

```cpp
