  if (a + b > c && a + c > b && b + c > a) {
    let s = (a + b + c) / 2;
    let area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
    return Number(area.toFixed(2));
  } else {
    return -1;
  }
};



console.log(triangleArea(3, 4, 5)) //== 6.00
console.log(triangleArea(1, 2, 10)) //== -1
console.log(triangleArea(3, 4, 5)) //== 6.00
console.log(triangleArea(7, 24, 25)) //== 84.00




```

This problem can be solved by using the formula for the area of a triangle. The formula is derived from the properties of the triangle and the lengths of its sides. 

Firstly, we check if the given sides can form a valid triangle. The sum of any two sides should be greater than the third side.

If the sides can form a valid triangle, we calculate the semi-perimeter of the triangle and use it to find the area of the triangle. The formula for the semi-perimeter is (a + b + c) / 2, and for the area, we use Heron's formula: sqrt[s * (s - a) * (s - b) * (s - c)], where s is the semi-perimeter.

Finally, we return the area of the triangle rounded to 2 decimal points. If the sides cannot form a valid triangle, we return -1.

This solution works for any positive real numbers as the sides of the triangle.

Note: This solution assumes that the input will be positive real numbers. If the input can include non-numeric values, additional error checking should be added.

Note: The area of the triangle can be a non-integer value. The Number.prototype.toFixed() method is used to round the area to 2 decimal points.




```javascript

```


```javascript

```


```javascript

```


```javascript