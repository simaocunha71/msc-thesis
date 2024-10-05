const findMax = (words) => {
  let unique = 0;
  let max = 0;
  let result = "";
  for (let i = 0; i < words.length; i++) {
    if (words[i].length > max) {
      max = words[i].length;
      result = words[i];
    }
  }
  return result;
};

