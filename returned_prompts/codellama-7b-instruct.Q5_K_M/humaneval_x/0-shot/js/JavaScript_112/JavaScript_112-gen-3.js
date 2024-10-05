const reverseDelete = (s, c) => {
  let result = s.split("").filter(item => !c.includes(item)).join("");
  return [result, result.split("").every((item, i) => item === result[result.length - 1 - i])];
}