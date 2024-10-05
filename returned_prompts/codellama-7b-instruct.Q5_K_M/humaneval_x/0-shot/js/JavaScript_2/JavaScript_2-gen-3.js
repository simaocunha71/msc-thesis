const truncateNumber = (number) => {
  const intPart = parseInt(number);
  const decPart = number - intPart;
  return decPart;
}

