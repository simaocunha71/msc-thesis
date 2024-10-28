  let evenLengthStrings = lst.filter(str => str.length % 2 === 0);
  return evenLengthStrings.sort((a, b) => {
    if (a.length !== b.length) {
      return a.length - b.length;
    } else {
      return a.localeCompare(b);
    }
  });
}



