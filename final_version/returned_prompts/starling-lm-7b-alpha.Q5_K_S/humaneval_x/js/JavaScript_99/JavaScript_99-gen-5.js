  const valueNum = parseFloat(value);

  const roundedUp = Math.ceil(valueNum);
  const roundedDown = Math.floor(valueNum);

  if (roundedUp - valueNum === valueNum - roundedDown) {
    if (valueNum > 0) {
      return roundedUp;
    } else {
      return roundedDown;
    }
  } else if (roundedUp - valueNum > valueNum - roundedDown) {
    return roundedUp;
  } else {
    return roundedDown;
  }
}



