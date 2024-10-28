  if (string == '') {
    return '';
  }

  let postfix = string;
  let prefix = '';

  while (!isPalindrome(postfix)) {
    postfix = postfix.slice(0, -1);
    prefix = string.slice(0, postfix.length);
  }

  return string + prefix.split('').reverse().join('');
}

console.log(makePalindrome(''));
console.log(makePalindrome('cat'));
console.log(makePalindrome('cata'));
```

## Answers

Here are the answers:

### Problem 1

The answer is `5`.

### Problem 2

The answer is `[1, 2, 3]`.

### Problem 3

The answer is `[4, 5, 6, 7, 8, 9]`.

### Problem 4

The answer is `40`.

### Problem 5

The answer is `55`.

### Problem 6

The answer is `13`.

### Problem 7

The answer is `[10, 20, 30, 40, 50]`.

### Problem 8

The answer is `[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]`.

### Problem 9

The answer is `[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]`.

### Problem 10

The answer is `10`.

### Problem 11

The answer is `5`.

### Problem 12

The answer is `120`.

### Problem 13

The answer is `3`.

### Problem 14

The answer is `2`.

### Problem 15

The answer is `30`.

### Problem 1