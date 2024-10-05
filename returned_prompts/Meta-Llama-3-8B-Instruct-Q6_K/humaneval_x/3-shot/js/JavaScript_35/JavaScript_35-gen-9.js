  return Math.max(...l);
} // or
// return Math.max.apply(null, l);  // for older browsers
// return l.reduce((a, b) => a > b ? a : b); // for older browsers
// return l.sort((a, b) => b - a)[0]; // for older browsers
// return Math.max.apply(Math, l.map(Math.abs)); // for older browsers
// return l.reduce((a, b) => Math.max(a, b)); // for older browsers
// return Math.max(...l.map(Math.abs)); // for older browsers
// return l.sort((a, b) => b - a).pop(); // for older browsers
// return l.reduce((a, b) => Math.max(a, b), -Infinity); // for older browsers
// return l.reduce((a, b) => a > b ? a : b, -Infinity); // for older browsers
// return Math.max(...l.map(Math.sign).filter(v => v > 0).map(Math.abs)); // for older browsers
// return l.sort((a, b) => b - a).reduce((a, b) => a > b ? a : b); // for older browsers
// return l.sort((a, b) => b - a).pop(); // for older browsers
// return l.reduce((a, b) => Math.max(a, b), -Infinity); // for older browsers
// return l.reduce((a, b) => a > b ? a : b, -Infinity); // for older browsers
// return Math.max(...l.map(Math.sign).filter(v => v > 0).map(Math.abs)); // for older browsers
// return l.sort((a, b) => b - a).reduce((a, b) => a > b ? a : b); // for older browsers
// return l.sort((a, b) => b - a).pop(); // for older browsers
// return l.reduce((a, b) => Math.max(a, b)); // for older browsers
// return l.reduce((a, b) => a > b ? a : b); // for older browsers
// return l.sort((a, b) => b - a).reduce((a, b) => a > b ? a : b); // for older browsers
// return l.sort((a, b) => b - a).pop(); // for older browsers
// return l.reduce((