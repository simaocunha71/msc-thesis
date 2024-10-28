  return Math.round(parseFloat(value));
}
// or
const closestInteger = (value) => {
  const num = parseFloat(value);
  return num < 0 ? Math.ceil(num) : Math.floor(num);
}