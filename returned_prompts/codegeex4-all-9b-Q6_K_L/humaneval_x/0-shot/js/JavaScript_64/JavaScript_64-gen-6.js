const vowelsCount = (s) => {
  // let count = 0;
  // for (let i = 0; i < s.length; i++) {
  //   if (s[i] === "a" || s[i] === "e" || s[i] === "i" || s[i] === "o" || s[i] === "u") {
  //     count++;
  //   }
  // }
  // if (s[s.length - 1] === "y") {
  //   count++;
  // }
  // return count;
  return [...s].filter((x) => "aeiouAEIOU".includes(x)).length + (s[s.length - 1] === "y");
}
