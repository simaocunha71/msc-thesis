  const isPal = (str) => str == str.split('').reverse().join('');
  const longestPal = (str) => {
    for (let i = str.length - 1; i >= 0; i--) {
      if (isPal(str.slice(0, i))) {
        return str.slice(0, i);
      }
    }
    return '';
  };
  const shortestPal = (str) => {
    let longest = longestPal(str);
    if (longest.length == 0) {
      return str;
    }
    let prefix = str.slice(0, longest.length - longest.split('').reverse().join('').length);
    return str + prefix + str.slice(longest.length).split('').reverse().join('');
  };
  return shortestPal(string);
};



