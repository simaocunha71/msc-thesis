  arr.sort((a, b) => b - a);
  return arr.slice(0, k);

};
*/

// 使用JavaScript的sort()函数对数组进行降序排序，然后使用slice()函数获取前k个元素。

/*
  测试:

  console.log(maximum([-3, -4, 5], 3)); // 期望输出: [-4, -3, 5]
  console.log(maximum([4, -4, 4], 2)); // 期望输出: [4, 4]
  console.log(maximum([-3, 2, 1, 2, -1, -2, 1], 1)); // 期望输出: [2]
*/

// 这段代码的时间复杂度是O(n log n)，其中n是数组的长度，因为涉及到排序。空间复杂度是O(1)，因为没有使用额外的空间。

const maximum = (arr, k) => {
  return arr
    .sort((a, b) => b - a)
    .slice(0, k);
};

console.log(maximum([-3, -4, 5], 3)); // 期望输出: [-4, -3, 5]
console.log(maximum([4, -4, 4], 2)); // 期望输出: [4, 4]
console.log(maximum([-3, 2, 1, 2, -1, -2, 1], 1)); // 期望输出: [2]

/*
  测试:

  console.log(maximum([-3, -4, 5], 3)); // 期望输出: [-4, -3, 5]
  console.log(maximum([4, -4, 4], 2)); // 期望输出: [4, 4]
  console.log(maximum([-3, 2, 1, 2, -1, -2, 1], 1)); // 期望输出: [2]
*/

// 这段