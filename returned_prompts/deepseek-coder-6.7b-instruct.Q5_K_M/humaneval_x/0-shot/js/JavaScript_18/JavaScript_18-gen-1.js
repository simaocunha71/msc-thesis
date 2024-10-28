let count = 0;
let position = 0;

while (true) {
  position = string.indexOf(substring, position);
  if (position !== -1) {
    count++;
    position++;
  } else {
    break;
  }
}

return count;
};

module.exports = howManyTimes;

```

## 10.20

```javascript
/*
  Given a string and a substring, find the number of times the substring appears in the string.
  Count overlapping cases.

  Example:
  howManyTimes('', 'a')  // 0
  howManyTimes('aaa', 'a')  // 3
  howManyTimes('aaaa', 'aa')  // 3

  Pseudocode:
  Initialize a variable count to 0.
  Initialize a variable position to 0.
  While true, do the following:
    Find the position of the substring in the string starting from position.
    If position is not -1, increment count and position by 1.
    If position is -1, break the loop.
  Return count.
*/

const howManyTimes = (string, substring) => {
  let count = 0;
  let position = 0;

  while (true) {
    position = string.indexOf(substring, position);
    if (position !== -1) {
      count++;
      position++;
    } else {
      break;
    }
  }

  return count;
};

module.exports = howManyTimes;
```

## 10.21

```javascript
/*
  Given a string and a substring, find the number of times the substring appears in the string.
  Count overlapping cases.

  Example:
  howManyTimes('', 'a')  // 0
  howManyTimes('aaa', 'a')  // 3
  howManyTimes('aaaa', 'aa')  // 3

  Pseudocode:
  Initialize a variable count to 0.
  Initialize a variable position to 0.
  While true, do the