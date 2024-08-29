  let result = "";
  let words = s.split(" ");

  for (let word of words) {
    let chars = word.split("");
    let sorted = chars.sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0));
    result += sorted.join("") + " ";
  }

  return result.trim();
}



