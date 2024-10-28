    return (a * h) / 2;
};

/*Given length of two sides and an angle return area for a triangle.
  >>> rightArea(3, 4, 90)
  6
  */
const rightArea = (a, b, c) => {

B:
    return (a * b) / 2;
};

/*Given length of two sides and an angle return area for a triangle.
  >>> scaleneArea(3, 4, 90)
  6
  */
const scaleneArea = (a, b, c) => {

C:
    const p = (a + b + c) / 2;
    return Math.sqrt(p * (p - a) * (p - b) * (p - c));
};

/*Given length of a side and high return area for a triangle.
  >>> triangleArea(5, 3)
  7.5
  */

/*Given length of two sides and an angle return area for a triangle.
  >>> rightArea(3, 4, 90)
  6
  */

/*Given length of two sides and an angle return area for a triangle.
  >>> scaleneArea(3, 4, 90)
  6
  */


// Exporting functions
module.exports = {
    triangleArea,
    rightArea,
    scaleneArea
};


















































































































































































