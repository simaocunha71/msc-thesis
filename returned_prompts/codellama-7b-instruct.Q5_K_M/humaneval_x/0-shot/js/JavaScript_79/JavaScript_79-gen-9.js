const decimalToBinary = (decimal) => {
  // Step 1: Convert the decimal to binary
  const binary = decimal.toString(2);

  // Step 2: Add the "db" characters to the beginning and end of the binary string
  return `db${binary}db`;
};

