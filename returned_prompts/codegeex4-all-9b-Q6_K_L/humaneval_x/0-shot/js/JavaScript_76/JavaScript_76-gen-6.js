const isSimplePower = (x, n) => {
  if(x <= 0 || n <= 0) return false;
  const power = Math.pow(n, Math.floor(Math.log(x) / Math.log(n)));
  return power === x;
};