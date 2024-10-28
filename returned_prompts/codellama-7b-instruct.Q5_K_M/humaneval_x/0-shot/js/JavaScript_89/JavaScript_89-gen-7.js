const encrypt = (s) => {
  let str = s.toLowerCase();
  let result = "";
  for (let i = 0; i < str.length; i++) {
    if (str[i] === " ") {
      result += " ";
    } else {
      let charCode = str.charCodeAt(i) + 2 * 2;
      result += String.fromCharCode(charCode);
    }
  }
  return result;
};
