const truncateNumber = (number) => {
  let truncated = number.toString();
  let index = truncated.indexOf('.');
  return truncated.substring(index, truncated.length);
};

B:
const truncateNumber = (number) => {
  let truncated = number.toString();
  return parseFloat(truncated.substring(truncated.indexOf('.')));
};

C:
const truncateNumber = (number) => {
  return number % 1;
};
