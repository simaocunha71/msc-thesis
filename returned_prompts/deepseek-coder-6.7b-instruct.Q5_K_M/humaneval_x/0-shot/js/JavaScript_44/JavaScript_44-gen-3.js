  return x.toString(base);
}

console.log(changeBase(8, 3));  // '22'
console.log(changeBase(8, 2));  // '1000'
console.log(changeBase(7, 2));  // '111'
```

### 2.2.2. 数组的长度

使用`.length`属性可以获取数组的长度。

```javascript
const arr = [1, 2, 3, 4, 5];
console.log(arr.length);  // 5
```

### 2.2.3. 数组的连接

使用`.concat()`方法可以连接两个或多个数组。

```javascript
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const arr3 = arr1.concat(arr2);
console.log(arr3);  // [1, 2, 3, 4, 5, 6]
```

### 2.2.4. 数组的切片

使用`.slice()`方法可以从数组中提取一部分数据。

```javascript
const arr = [1, 2, 3, 4, 5];
console.log(arr.slice(1, 3));  // [2, 3]
```

### 2.2.5. 数组的反转

使用`.reverse()`方法可以反转数组的顺序。

```javascript
const arr = [1, 2, 3, 4, 5];
console.log(arr.reverse());  // [5, 4, 3, 2, 1]
```

### 2.2.6. 数组的排序

使用`.sort()`方法可以对数组进行排序。

```javascript
const arr = [5, 2, 1, 4, 3];
console.log(arr.sort());  // [1, 2, 3, 4, 5]
```

### 2.2