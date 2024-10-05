const histogram = (test) => {
  let hist = {};
  let max = 0;

  for (let i = 0; i < test.length; i++) {
    if (test[i] in hist) {
      hist[test[i]]++;
    } else {
      hist[test[i]] = 1;
    }
    if (hist[test[i]] > max) {
      max = hist[test[i]];
    }
  }
  let result = {};
  for (let key in hist) {
    if (hist[key] == max) {
      result[key] = hist[key];
    }
  }
  return result;
};
