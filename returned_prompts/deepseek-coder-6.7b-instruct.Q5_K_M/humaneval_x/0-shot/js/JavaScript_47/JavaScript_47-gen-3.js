  l.sort((a, b) => a - b);
  let median;
  if (l.length % 2 === 0) {
    let mid = l.length / 2;
    median = (l[mid - 1] + l[mid]) / 2;
  } else {
    median = l[Math.floor(l.length / 2)];
  }
  return median;
};



module.exports = median;





```






```javascript
// Q2

