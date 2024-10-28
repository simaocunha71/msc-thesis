  if(l.length < 3){
    return false;
  }

  l.sort((a, b) => a - b);

  for(let i = 0; i < l.length - 2; i++){
    let j = i + 1;
    let k = l.length - 1;

    while(j < k){
      let sum = l[i] + l[j] + l[k];

      if(sum === 0){
        return true;
      } else if(sum < 0){
        j++;
      } else {
        k--;
      }
    }
  }

  return false;
};

module.exports = triplesSumToZero;
```

## 4. 数组排序

### 4.1. 冒泡排序

冒泡排序是一种简单的排序算法，它通过重复遍历列表，比较相邻的元素并交换它们的位置，直到列表排序完成。

```javascript
const bubbleSort = (arr) => {
  let len = arr.length;
  for(let i = 0; i < len; i++){
    for(let j = 0; j < len - i - 1; j++){
      if(arr[j] > arr[j + 1]){
        // 交换元素
        let temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
  return arr;
};

console.log(bubbleSort([5, 3, 8, 4, 6])); // 期望输出: [3, 4, 5, 6, 8]
```

### 4.2. 选择排序

选择排序算法通过重复从未排序的部分中找到最小元素，并将其放在已排序部分的开头来对数组进行排序。

```javascript
const selectionSort = (arr) => {
  let len = arr.length;
  for(let i = 0; i < len; i++){
    let