  let arr = s.split(" ");
  let result = "";
  for (const str of arr) {
    let arr2 = str.split("");
    arr2.sort();
    result += arr2.join("") + " ";
  }
  return result;
}



