let sides = [a, b, c].sort((a, b) => a - b);

return Math.pow(sides[0], 2) + Math.pow(sides[1], 2) === Math.pow(sides[2], 2);

};

console.log(rightAngleTriangle(3, 4, 5)); // true
console.log(rightAngleTriangle(1, 2, 3)); // false

*/

