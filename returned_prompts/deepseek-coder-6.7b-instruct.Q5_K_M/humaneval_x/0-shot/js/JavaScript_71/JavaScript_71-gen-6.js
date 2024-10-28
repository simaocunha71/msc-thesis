  // first check if triangle is valid
  if(a + b > c && a + c > b && b + c > a){
    // calculate semi-perimeter
    let s = (a + b + c) / 2;
    // calculate area using Heron's formula
    let area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
    // return area rounded to 2 decimal places
    return Math.round(area * 100) / 100;
  }else{
    // if triangle is not valid return -1
    return -1;
  }
};

console.log(triangleArea(3, 4, 5)); // 6.00
console.log(triangleArea(1, 2, 10)); // -1
console.log(triangleArea(3, 4, 5)); // 6.00
console.log(triangleArea(6, 8, 10)); // 24.00
console.log(triangleArea(1, 1, 2)); // -1
console.log(triangleArea(2, 10, 12)); // -1
```


## 15. Factorial

