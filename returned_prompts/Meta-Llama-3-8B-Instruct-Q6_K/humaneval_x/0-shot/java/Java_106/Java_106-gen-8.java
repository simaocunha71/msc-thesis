        List<Integer> res = new ArrayList<>();
        for(int i = 1; i <= n; i++) {
            if(i % 2 == 0) {
                int temp = 1;
                for(int j = 2; j <= i; j++) {
                    temp *= j;
                }
                res.add(temp);
            } else {
                int sum = 0;
                for(int j = 1; j <= i; j++) {
                    sum += j;
                }
                res.add(sum);
            }
        }
        return res;
    }
}
S:
The function `f` takes an integer `n` as a parameter and returns a list of size `n`. The value of the element at index `i` is determined by the following conditions:
- If `i` is even, the value is the factorial of `i`.
- If `i` is odd, the value is the sum of numbers from 1 to `i`.

The function uses a loop to iterate over the range from 1 to `n`. For each `i`, it checks if `i` is even or odd using the modulus operator (`%`). If `i` is even, it calculates the factorial of `i` using a nested loop and adds the result to the result list. If `i` is odd, it calculates the sum of numbers from 1 to `i` using a nested loop and adds the result to the result list.

Finally, the function returns the result list.

Example:
```
f(5) == [1, 2, 6, 24, 15]
```
Explanation:
- `f(1)` returns `[1]` because 1 is odd and the sum of numbers from 1 to 1 is 1.
- `f(2)` returns `[1, 2]` because 2 is even and the factorial of 2 is 2.
- `f(3)` returns `[1, 3, 6]` because 3 is odd and the sum of numbers from 1 to 3 is 6.
- `f(4)` returns `[1, 2, 6, 24]` because 4 is even and the factorial of 4 is 24.
- `f(5)` returns `[1, 2, 6, 24, 15]` because 5 is odd and the sum of numbers from 1 to 5 is 15.