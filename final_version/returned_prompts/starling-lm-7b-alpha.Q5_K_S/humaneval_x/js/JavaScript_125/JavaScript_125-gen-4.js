  let result = [];

  let splitOnWhitespace = txt.split(/\s+/);

  if (splitOnWhords.length > 0) {
    result = splitOnWhitespace;
  } else {
    let splitOnComma = txt.split(/,/);

    if (splitOnComma.length > 0) {
      result = splitOnComma;
    } else {
      result = txt.match(/[a-z]/gi).filter((char) => {
        return char % 2 === 1;
      }).length;
    }
  }

  return result;
}



