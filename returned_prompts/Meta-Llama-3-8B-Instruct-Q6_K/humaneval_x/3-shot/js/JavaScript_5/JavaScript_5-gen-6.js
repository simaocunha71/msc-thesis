  return [numbers[0]].concat(...numbers.slice(1).map(x => [delimeter, x])).slice(1);
} // or
// return [numbers[0]].concat(delimeter, ...numbers.slice(1).map(x => [x])).slice(1);
} // or
// return numbers.slice(0, 1).concat(delimeter, numbers.slice(1).flat()); // ES2019
} // or
// return [...numbers[0]].concat(delimeter, ...numbers.slice(1).flat()); // ES2019
} // or
// return numbers.reduce((acc, val) => acc.concat(delimeter, [val]), []); // ES2019
} // or
// return numbers.reduce((acc, val, i) => i > 0 ? acc.concat([delimeter, val]) : acc.concat([val]), []); // ES2019
} // or
// return numbers.slice().reduce((acc, val) => acc.concat(delimeter, [val]), []); // ES2019
} // or
// return numbers.slice().reduce((acc, val, i) => i > 0 ? acc.concat([delimeter, val]) : acc.concat([val]), []); // ES2019
} // or
// return numbers.map((val, i) => i > 0 ? [delimeter, val] : val).flat(); // ES2019
} // or
// return numbers.map((val, i) => i > 0 ? [delimeter].concat([val]) : [val]).flat(); // ES2019
} // or
// return numbers.map((val, i) => i > 0 ? [delimeter].concat([val]) : [val]).flat().filter(x => x !== delimeter); // ES2019
} // or
// return numbers.map((val, i) => i > 0 ? [delimeter, val] : val).flat().filter(x => x !== delimeter); // ES2019
} // or
// return numbers.map((val, i) => i > 0 ? [delimeter].concat([val]) : [val]).flat().filter(x => x !== delimeter); // ES2019
} // or
// return numbers.map((val, i) => i > 0 ? [delimeter].concat([val]) : [val]).flat().filter(x => x !== delimeter).join