  let arr = Array.from(s);
  let isLower = false;
  let isUpper = false;

  for(let i = 0; i < arr.length; i++) {
    if(arr[i] === arr[i].toLowerCase()) {
      isLower = true;
      arr[i] = arr[i].toUpperCase();
    } else if(arr[i] === arr[i].toUpperCase()) {
      isUpper = true;
      arr[i] = arr[i].toLowerCase();
    }
  }

  if(!isLower) {
    return s.split("").reverse().join("");
  }

  if(!isUpper) {
    return s;
  }

  return arr.join("");
}



