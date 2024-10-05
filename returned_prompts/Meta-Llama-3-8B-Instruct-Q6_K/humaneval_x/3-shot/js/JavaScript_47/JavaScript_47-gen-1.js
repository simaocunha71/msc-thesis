  l.sort((a, b) => a - b);
  let n = l.length;
  if (n % 2 === 0) {
    return (l[n / 2 - 1] + l[n / 2]) / 2;
  } else {
    return l[Math.floor(n / 2)];
  }
}
//test cases
console.log(median([3, 1, 2, 4, 5])); //3
console.log(median([-10, 4, 6, 1000, 10, 20])); //8.0
console.log(median([1])); //1
console.log(median([1, 2, 3, 4])); //2.5
console.log(median([1, 3, 5])); //3
console.log(median([1, 2, 3, 4, 5])); //3
console.log(median([1, 2, 3, 4, 5, 6])); //3.5
console.log(median([1, 2, 3, 4, 5, 6, 7])); //4
console.log(median([1, 2, 3, 4, 5, 6, 7, 8])); //4.5
console.log(median([1, 2, 3, 4, 5, 6, 7, 8, 9])); //5
console.log(median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])); //5.5
console.log(median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])); //5.5
console.log(median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])); //6
console.log(median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])); //6.5
console.log(median([1, 2, 3, 4, 5, 6, 