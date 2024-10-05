  const sortString = (string) => {
    return string.split('').sort().join('');
  }

  return sortString(s0) === sortString(s1);
}

sameChars('eabcdzzzz', 'dddzzzzzzzddeddabc'); // true
sameChars('abcd', 'dddddddabc'); // true
sameChars('dddddddabc', 'abcd'); // true
sameChars('eabcd', 'dddddddabc'); // false
sameChars('abcd', 'dddddddabce'); // false
sameChars('eabcdzzzz', 'dddzzzzzzzddddabc'); // false
```


## 10.3.5

