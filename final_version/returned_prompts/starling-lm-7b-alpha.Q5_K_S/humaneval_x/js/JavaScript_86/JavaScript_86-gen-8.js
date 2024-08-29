  let arr = s.split(" ");
  let result = "";

  for (let i = 0; i < arr.length; i++) {
    let charArr = arr[i].split("");
    charArr.sort(function(a,b){return a.charCodeAt(0) - b.charCodeAt(0)});
    result += charArr.join("");
    if (i != arr.length - 1) result += " ";
  }

  return result;
}



