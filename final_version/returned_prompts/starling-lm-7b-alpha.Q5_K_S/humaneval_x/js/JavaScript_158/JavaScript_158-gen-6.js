  let max = 0;
  let res = "";
  for (let i = 0; i < words.length; i++) {
    let temp = 0;
    for (let j = 0; j < words[i].length; j++) {
      let t = 0;
      for (let k = 0; k < words.length; k++) {
        if (words[k].indexOf(words[i][j]) != -1) {
          t += 1;
        }
      }
      temp = Math.max(temp, t);
    }
    if (temp > max) {
      max = temp;
      res = words[i];
    }
  }
  return res;
}



