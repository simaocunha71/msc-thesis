let uniqueArr = [...new Set(l)];
return uniqueArr.sort((a, b) => a - b);
}

console.log(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]));
```

You can also use the filter method to accomplish this:

```javascript
// 