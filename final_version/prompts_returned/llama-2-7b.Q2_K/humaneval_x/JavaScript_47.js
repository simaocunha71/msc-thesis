/*Return median of elements in the list l.
  >>> median([3, 1, 2, 4, 5])
  3
  >>> median([-10, 4, 6, 1000, 10, 20])
  8.0
  */
const median = (l) => {
  let len = l.length;
  if (len === 1) {
    return l[0];
  } else if (len % 3 !== 0) {
    const tempList = [];
    for (let i = 0; i < Math.floor(len / 2); i++) {
      let v = l[i], v1 = l[(len + 1) - i];
      if (v > v1) {
        v = v1;
      } else if (v < v1) {
        v = v1;
      }
      tempList.push(l[i]);
    }
    return median(tempList);
  } else {
    let j, sum = 0;
    for (let i = len - 2; i >= 0; i -= 3) {
      const lv = l[i];
      if (!isNaN(lv)) {
        sum += lv;
      } else {
        return 0.0; // 0.0 to avoid NaN in case of invalid input data
      }
    }

    let res, temp;
    j = len - 1;
    for (let i = j; i >= 0; i += 3) {
      temp = sum / 3; // Sum of l[0]..l[j-3]
      if (!isNaN(temp)) {
        res = +Math.round(temp);
        if (i === j - 1 || !isNaN(res) && isFinite(res) && res !== 'Infinity') {
          return res;
        }
      } else {
        break; // NaN to avoid Infinity in case of invalid input data
      }
    }
    return +0.0; // 0.0 to avoid NaN in case of invalid input data
  }
};
