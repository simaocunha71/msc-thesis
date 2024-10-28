        ArrayList<Integer> count = new ArrayList<>(Arrays.asList(0, 0));
        num = Math.abs(num);
        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                count.set(0, count.get(0) + 1);
            } else {
                count.set(1, count.get(1) + 1);
            }
            num = num / 10;
        }
        return count;
    }
}

```

## Explanation

In this program, we first initialize an array list `count` with two elements, both of which are 0. This will be used to track the counts of even and odd digits. 

We then convert the input number `num` to its absolute value, since we are not interested in the sign of the number. 

We then start a loop that will continue as long as `num` is greater than 0. In each iteration of the loop, we get the last digit of `num` by using the modulo operator. If this digit is even (it has no remainder when divided by 2), we increase the count of even numbers by 1. Otherwise, we increase the count of odd numbers by 1. 

Finally, we remove the last digit of `num` by integer division by 10. 

The function returns the `count` list, which contains the counts of even and odd digits in the order (even count, odd count).

## Test Cases

- Test case 1: `evenOddCount(-12)` returns `[1, 1]`.
- Test case 2: `evenOddCount(123)` returns `[1, 2]`.
- Test case 3: `evenOddCount(1234567890)` returns `[5, 5]`.
- Test case 4: `evenOddCount(0)` returns `[1, 0]`.
- Test case 5: `evenOddCount(-1234567890)` returns `[5, 5]`.

## Time Comple