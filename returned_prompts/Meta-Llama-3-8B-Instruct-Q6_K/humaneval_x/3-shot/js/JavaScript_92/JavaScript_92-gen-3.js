  return (x + y === z || x + z === y || y + z === x) && parseInt(x) === x && parseInt(y) === y && parseInt(z) === z;
}
// parseInt(x) === x checks if x is an integer. If it's not, it will return false. This is a common trick in JavaScript to check if a number is an integer.