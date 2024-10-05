const digits = (n) => {
  let product = 1;
  for (let i = 0; i < n.length; i++) {
    if (n[i] % 2 !== 0) {
      product *= n[i];
    }
  }
  return product;
}
