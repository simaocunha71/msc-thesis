  const palindromePrefix = string.split('').reverse().findIndex((item, index) => {
    return string.slice(0, index + 1) === string.slice(index + 1).split('').reverse().join('');
  });
  const palindromeSuffix = string.split('').reverse().slice(0, palindromePrefix + 1).join('');

  return `${string}${palindromeSuffix}${palindromeSuffix.split('').reverse().join('')}`;
};

/* Get the middle character of a string */
const getMiddleChar = (string) => {
  if (string.length % 2 === 0) {
    return `${string[Math.floor((string.length - 1) / 2)]}${string[Math.floor((string.length) / 2)]}`;
  }
  else {
    return string[Math.floor((string.length - 1) / 2)];
  }
};

/* Capitalize the first letter of each word in a string */
const capitalize = (string) => {
  return string.split(' ').map(item => {
    return item.charAt(0).toUpperCase() + item.slice(1);
  }).join(' ');
};

/* Remove all non-alphanumeric characters from a string */
const removeNonAlphaNumeric = (string) => {
  return string.replace(/\W/g, '');
};

/* Capitalize and remove non-alphanumeric characters */
const capitalizeAndRemoveNonAlphaNumeric = (string) => {
  return capitalize(removeNonAlphaNumeric(string));
};

/* Shuffle an array */
const shuffle = array => {
  let currentIndex = array.length, temporaryValue, randomIndex;

  while (currentIndex !== 0) {
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex -= 1;

    temporaryValue = array[currentIndex];
    array[currentIndex] = array[randomIndex];
    array[randomIndex] = temporaryValue;
  }

  return array;
};

/* Check if a