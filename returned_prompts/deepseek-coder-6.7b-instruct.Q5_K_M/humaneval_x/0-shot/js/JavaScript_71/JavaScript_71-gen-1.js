  if(a + b > c && a + c > b && b + c > a){
    let s = (a + b + c) / 2;
    return Number((Math.sqrt(s * (s - a) * (s - b) * (s - c))).toFixed(2));
  }
  else {
    return -1;
  }
}

console.log(triangleArea(3,4,5));
console.log(triangleArea(1,2,10));

*/

function triangleArea(a, b, c) {
  if (a + b > c && a + c > b && b + c > a) {
    let s = (a + b + c) / 2;
    return Number((Math.sqrt(s * (s - a) * (s - b) * (s - c))).toFixed(2));
  } else {
    return -1;
  }
}

console.log(triangleArea(3,4,5));
console.log(triangleArea(1,2,10));


/*
  This function takes three arguments which represent the lengths of the sides of a triangle.
  It checks if these lengths can form a valid triangle by using the triangle inequality theorem.
  If they can, it calculates the area of the triangle using Heron's formula and returns it.
  If they can't, it returns -1.
*/

















































































































































































