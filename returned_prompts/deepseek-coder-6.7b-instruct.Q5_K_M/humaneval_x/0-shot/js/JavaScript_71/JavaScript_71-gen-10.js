  if(a + b > c && a + c > b && b + c > a){
    let s = (a + b + c) / 2;
    let area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
    return Math.round(area * 100) / 100;
  }
  else{
    return -1;
  }
}

module.exports = triangleArea;

*/

// This function first checks if the input values can form a valid triangle using the triangle inequality theorem.
// If it can, it calculates the semi-perimeter s of the triangle and then uses Heron's formula to calculate and return the area.
// If the inputs can't form a valid triangle, it returns -1.

// Heron's formula:
// Area = sqrt(s(s - a)(s - b)(s - c))
// where a, b, c are the sides of the triangle and s is the semi-perimeter of the triangle, given by s = (a + b + c) / 2

// The area is then rounded to two decimal places by multiplying by 100, rounding to the nearest whole number, and then dividing by 100.

// This is done using JavaScript's Math.round() function, which rounds a number to the nearest whole number.

// If the area is a whole number, the decimal point and following zeros will be removed, since JavaScript's rounding function doesn't include them.

// The function is exported so it can be tested in the test file.

// Note: JavaScript's Math.sqrt() function is used to calculate the square root of a number.















































































































