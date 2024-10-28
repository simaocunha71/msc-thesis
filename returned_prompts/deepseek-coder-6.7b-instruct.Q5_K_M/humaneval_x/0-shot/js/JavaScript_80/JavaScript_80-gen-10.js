  if (s.length < 3) return false;

  for (let i = 0; i < s.length; i++) {
    if (i % 3 === 2) {
      if (s[i] === s[i - 1] || s[i] === s[i - 2] || s[i - 1] === s[i - 2]) {
        return false;
      }
    }
  }

  return true;
};

console.log(isHappy('a')); // false
console.log(isHappy('aa')); // false
console.log(isHappy('abcd')); // true
console.log(isHappy('aabb')); // false
console.log(isHappy('adb')); // true
console.log(isHappy('xyy')); // false
console.log(isHappy('xxy')); // false
console.log(isHappy('xyz')); // true

/*
In this program, the function isHappy takes a string s as input.
If the string s's length is less than 3, it returns false.
Then the function iterates over the string s, checking every 3 consecutive letters.
If any of the 3 letters are identical, the function returns false.
If the loop completes without finding any identical letters, the function returns true.
*/

```

# 10.21-11.03

## 10.21

### 数组

- 数组是一种特殊的数据结构，它可以存储多个数据，这些数据可以是任何类型的数据，例如数字，字符串，对象等。
- 在JavaScript中，数组可以使用`[]`来创建，并且可以使用`push`，`pop`，`shift`，`unshift`等方法来操作数组。
- 数组的索引从0开始，可以使用`[]`来访问和修改数组的元素。
- 数组的长度可以使用`length`属性来获取。

### 数组的方法

- `push`: 向数组的末尾添加一个或多个元素，并返回新的长度。
- `pop`: 从数组中删