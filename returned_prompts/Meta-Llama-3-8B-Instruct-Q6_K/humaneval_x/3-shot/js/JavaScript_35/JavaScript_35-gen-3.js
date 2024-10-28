  return Math.max(...l);
} // or return Math.max.apply(null, l);
} // or return l.reduce((a, b) => a > b ? a : b); // ES6


