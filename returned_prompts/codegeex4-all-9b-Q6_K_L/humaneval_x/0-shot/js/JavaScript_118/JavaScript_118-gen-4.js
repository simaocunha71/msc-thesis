```java
const getClosestVowel = (word) => {
  let p = word.length - 2
  while (p > 0) {
    if (
      'aeiouAEIOU'.includes(word[p]) &&
      !'aeiouAEIOU'.includes(word[p - 1]) &&
      !'aeiouAEIOU'.includes(word[p + 1])
    )
      return word[p]
    p--
  }
  return ''
}
```
