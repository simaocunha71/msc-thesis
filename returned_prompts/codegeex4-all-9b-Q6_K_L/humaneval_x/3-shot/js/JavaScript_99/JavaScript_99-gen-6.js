  let result = Math.round(Number(value));
  if (result == Number(value)) {
    return result;
  } else {
    return Math.sign(Number(value)) * Math.round(Math.abs(Number(value)));
  }
}



