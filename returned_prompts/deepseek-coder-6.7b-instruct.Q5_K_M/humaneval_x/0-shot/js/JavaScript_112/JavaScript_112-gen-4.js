  let str = Array.from(s).filter(val => !c.includes(val)).join('');
  let rev = Array.from(s).reverse().filter(val => !c.includes(val)).join('');
  
  return [str, str === rev];
};

console.log(reverseDelete('abcde', 'ae')); // 应返回 ['bcd', false]
console.log(reverseDelete('abcdef', 'b')); // 应返回 ['acdef', false]
console.log(reverseDelete('abcdedcba', 'ab')); // 应返回 ['cdedc', true]

// 通过从字符串 s 中删除任何在字符串 c 中出现的字符，然后检查结果字符串是否为回文来解决问题。
// 我们通过将字符串转换为数组，使用 filter 方法过滤掉在字符串 c 中出现的字符，然后使用 join 方法将数组转换回字符串。
// 为了检查结果字符串是否为回文，我们将字符串与其反转版本进行比较。如果它们相等，则字符串是回文，我们返回 true，否则返回 false。
// 我们将结果字符串和布尔值一起返回。
// 该解决方案的时间复杂度为 O(n)，因为我们需要遍历字符串 s 和 c 中的每个字符一次。
// 空间复杂度也为 O(n)，因为我们创建了字符串 s 的数组副本，并且在过滤和连接过程中创建了新的数组。

// 注意：这个解决方案假设字符串 s 和 c 只包含小写字母。如果可能包含大写字母或其他字符，则需要相应地修改过滤条件。
```

### 解决方案

```javascript
const reverseDelete = (s, c) => {

  let str = Array.from(s).filter(val => !c.includes(val)).join('');
  let rev = Array.from(s).reverse().filter(val => !c.includes(val)).join('');
  
 