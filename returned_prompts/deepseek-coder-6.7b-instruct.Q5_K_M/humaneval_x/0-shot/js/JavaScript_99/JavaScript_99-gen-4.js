  const num = Number(value);
  return (num < 0) ? Math.floor(num - 0.5) : Math.floor(num + 0.5);
}

module.exports = closestInteger;

*/

const closestInteger = (value) => {
  const num = Number(value);
  return (num < 0) ? Math.floor(num - 0.5) : Math.floor(num + 0.5);
}

module.exports = closestInteger;

/*
