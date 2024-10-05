const smallestChange = (arr) => {
  const len = arr.length;
  const middle = len / 2;
  const left = arr.slice(0, middle);
  const right = arr.slice(middle);

  const leftMap = {};
  const rightMap = {};

  for (let i = 0; i < left.length; i += 1) {
    leftMap[left[i]] = true;
  }
  for (let i = 0; i < right.length; i += 1) {
    rightMap[right[i]] = true;
  }

  let ans = 0;
  for (let i = 0; i < len; i += 1) {
    if (leftMap[right[i]]) {
      delete leftMap[right[i]];
      delete rightMap[left[i]];
      ans += 1;
    }
  }

  return ans;
};

const arr = [1, 2, 3, 2, 1];
console.log(smallestChange(arr)); // 0

arr = [1, 2, 3, 5, 4, 7, 9, 6];
console.log(smallestChange(arr)); // 4

arr = [1, 2, 3, 4, 3, 2, 2];
console.log(smallestChange(arr)); // 1

arr = [1, 2, 3, 4, 5, 6, 7, 8];
console.log(smallestChange(arr)); // 3

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
console.log(smallestChange(arr)); // 4

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
console.log(smallestChange(arr)); // 5

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1