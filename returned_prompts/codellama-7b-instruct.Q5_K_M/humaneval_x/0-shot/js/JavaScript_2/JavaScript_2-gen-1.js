  const integerPart = Math.floor(number);
  const decimals = number - integerPart;
  const truncatedDecimals = decimals.toFixed(3);
  const truncatedDecimalsArray = truncatedDecimals.split('.');
  const lastTwoDecimals = truncatedDecimalsArray[1].substr(0, 2);
  return lastTwoDecimals;

}

