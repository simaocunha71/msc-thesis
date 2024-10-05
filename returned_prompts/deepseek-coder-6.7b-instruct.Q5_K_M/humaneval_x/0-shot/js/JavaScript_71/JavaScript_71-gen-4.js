  if (a + b > c && a + c > b && b + c > a) {
    let s = (a + b + c) / 2;
    let area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
    return Number(area.toFixed(2));
  } else {
    return -1;
  }
}

console.log(triangleArea(3, 4, 5)) // 6.00
console.log(triangleArea(1, 2, 10)) // -1
console.log(triangleArea(3, 4, 6)) // 5.34
console.log(triangleArea(7, 24, 25)) // 84.00
```

This JavaScript function works by first checking if the three input lengths can form a valid triangle. If they can, it calculates the semi-perimeter of the triangle and then uses Heron's formula to find the area. It then rounds the area to 2 decimal places and returns it. If the input lengths cannot form a valid triangle, it returns -1.


### **JavaScript**

```javascript
