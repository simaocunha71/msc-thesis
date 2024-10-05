  let maxFreq = 0;
  let maxVal = -1;
  let freqMap = {};

  for (let num of lst) {
    if (!freqMap[num]) {
      freqMap[num] = 0;
    }
    freqMap[num]++;
  }

  for (let num in freqMap) {
    if (freqMap[num] >= parseInt(num) && parseInt(num) > 0 && parseInt(num) > maxVal) {
      maxVal = parseInt(num);
    }
  }

  return maxVal > 0 ? maxVal : -1;
}  // The function could be written in a more concise way. Here is an example of a more concise version:
// const search = (lst) => lst.reduce((max, num) => num > 0 && num >= freqMap[num] ? num : max, -1);
// let freqMap = {};
// for (let num of lst) {
//   freqMap[num] = (freqMap[num] || 0) + 1;
// }  // This function will return the first number it finds that meets the condition, not the largest. If you want the largest, you need a different approach.  // The function could be written in a more concise way. Here is an example of a more concise version:
// const search = (lst) => lst.reduce((max, num) => num > 0 && num >= freqMap[num] ? num : max, -1);
// let freqMap = {};
// for (let num of lst) {
//   freqMap[num] = (freqMap[num] || 0) + 1;
// }  // This function will return the first number it finds that meets the condition, not the largest. If you want the largest, you need a different approach.