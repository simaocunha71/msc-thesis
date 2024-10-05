  if (n < 2) return 0;
  if (n === 2) return 2;
  if (n === 3) return 0;
  
  let a = 0, b = 0, c = 2, d = 0;
  
  for(let i = 4; i <= n; i++){
    let temp = d + c + b + a;
    a = b;
    b = c;
    c = d;
    d = temp;
  }
  
  return d;
};

module.exports = fib4;

// fib4(5) -> 4
// fib4(6) -> 8
// fib4(7) -> 14
```

## Functionality

The function `fib4` takes in an integer `n` and returns the nth number in the fib4 sequence.

The function starts by checking if `n` is less than 2, 3 or 4 and returns 0, 2 or 0 respectively. 

Then it initializes four variables `a`, `b`, `c` and `d` to 0, 0, 2 and 0 respectively.

After that, it enters a loop from 4 to `n` and each iteration calculates the next number in the sequence by adding the previous four numbers together (`d + c + b + a`). It then updates the four variables `a`, `b`, `c` and `d` to the next four numbers in the sequence.

Finally, it returns the `n`th number in the fib4 sequence.

## Performance

The time complexity of this function is O(n) because it performs a single loop from 4 to `n`. The space complexity is O(1) because it uses a constant amount of space to store the four variables `a`, `b`, `c` and `d`.

## Code Review

The code is well-structured and efficient. It uses a loop to compute the nth number in the fib4 sequence, which avoids the need for recursion, which would increase the space complexity of the function. The variables `a`, `b`, `c` and `d` are used to keep track of the last four numbers in