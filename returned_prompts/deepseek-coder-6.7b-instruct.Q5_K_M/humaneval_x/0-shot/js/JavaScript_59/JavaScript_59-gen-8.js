  let factor = 2;
  while (factor !== n) {
    if (n % factor === 0) {
      n = n / factor;
    } else {
      factor++;
    }
  }
  return factor;
};


// TEST CASES:
console.log(largestPrimeFactor(13195)); // 29
console.log(largestPrimeFactor(2048)); // 2
```

- 在开始时，我们用2作为最小可能的因子，然后尝试将输入的数`n`除以这个因子。如果`n`能被整除，我们将`n`设置为`n / factor`，并继续这个过程。如果`n`不能被整除，我们将`factor`增加1，并继续尝试。我们一直这样做，直到`factor`等于`n`，此时`n`的最大因子就是我们正在寻找的最大质因子。



#### 问题2：

```javascript
