  return values.filter(x => typeof x === 'number' && x % 1 === 0);
} // or return values.filter(Number.isInteger); // if using ES7



