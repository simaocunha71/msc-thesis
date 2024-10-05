    if(b == 0)
        return a;
    else
        return greatest_common_divisor(b, a % b);
}
int main(){
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%d", greatest_common_divisor(a, b));
    return 0;
}
```

**Python:**

```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)

a = int(input())
b = int(input())
print(greatest_common_divisor(a, b))
```

## Euclid algorithm:

This algorithm is used to find the greatest common divisor (gcd) of two integers. The algorithm is based on the principle that the gcd of two numbers is the same as the gcd of the remainder when the larger number is divided by the smaller number.

Here is the pseudocode for the Euclid algorithm:

```
function gcd(a, b)
    if b is 0
        return a
    else
        return gcd(b, a mod b)
```

In the code, if b is 0, the function returns a, which is the greatest common divisor. Otherwise, the function calls itself with b and the remainder of the division of a by b as arguments.

The time complexity of the Euclid algorithm is O(log min(a, b)).

The Euclid algorithm can be implemented in many programming languages. Here's an example in Python:

```python
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
```

In this Python function, if b is 0, the function returns a, which is the greatest common divisor. Otherwise, the function calls itself with b and the remainder of the division of a by b as arguments.

## References:

1. https://en.wikipedia.org/wiki/Euclidean_algorithm
2. https://www.geeksforgeeks.org/euclidean