  return (x + y === z || x + z === y || y + z === x) && typeof x === 'number' && typeof y === 'number' && typeof z === 'number';
}