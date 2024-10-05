/* Filter an input list of strings only for ones that contain given substring
  >>> filterBySubstring([], 'a')
  []
  >>> filterBySubstring(['abc', 'bacd', 'cde', 'array'], 'a')
  ['abc', 'bacd', 'array']
  */
const filterBySubstring = (strings, substring) => {
  return strings.filter(str => str.includes(substring));
}
```

</details>

### 04. 노트북 생성

<details><summary>풀이 보기</summary>

```javascript
