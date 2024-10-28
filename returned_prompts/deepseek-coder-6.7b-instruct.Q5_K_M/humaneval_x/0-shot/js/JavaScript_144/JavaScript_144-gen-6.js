  const [numX, denX] = x.split("/").map(Number);
  const [numN, denN] = n.split("/").map(Number);

  return numX * denN === numN * denX;
}

console.log(simplify("1/5", "5/1")); // true
console.log(simplify("1/6", "2/1")); // false
console.log(simplify("7/10", "10/2")); // false

module.exports = simplify;

*/

const simplify = (x, n) => {
  const [numX, denX] = x.split("/").map(Number);
  const [numN, denN] = n.split("/").map(Number);

  return numX * denN === numN * denX;
};

console.log(simplify("1/5", "5/1")); // true
console.log(simplify("1/6", "2/1")); // false
console.log(simplify("7/10", "10/2")); // false

module.exports = simplify;

// The function first splits the input strings into numerators and denominators,
// then converts them to numbers. If the result of multiplying the numerator of
// the first fraction by the denominator of the second fraction is equal to the
// result of multiplying the numerator of the second fraction by the denominator
// of the first fraction, it returns true; otherwise, it returns false.

// It's a bit like checking if the fractions are equivalent.
// For example, the fractions 1/2 and 2/4 are equivalent, so simplify("1/2", "2/4") returns true.

// Also note that the question asks for the function to return true if the simplified
// product of the two fractions is a whole number, not if the fractions themselves are simplified.
// For example, the fractions 4/8 and 2/1 are equivalent, so simplify("4/8", "2/1") would return true,
// but 4/8 simplifies to 1/2, which is not a whole number, so the