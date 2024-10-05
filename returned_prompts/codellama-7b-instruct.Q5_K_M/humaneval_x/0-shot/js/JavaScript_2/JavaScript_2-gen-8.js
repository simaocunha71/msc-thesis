const truncateNumber = (number) => {
  const intPart = Math.floor(number);
  const decPart = number - intPart;
  return decPart;
};

B:
const truncateNumber = (number) => {
  const intPart = Math.floor(number);
  return number.toString().split(".")[1];
};

C:
const truncateNumber = (number) => {
  return Math.abs(number) - Math.floor(Math.abs(number));
};
