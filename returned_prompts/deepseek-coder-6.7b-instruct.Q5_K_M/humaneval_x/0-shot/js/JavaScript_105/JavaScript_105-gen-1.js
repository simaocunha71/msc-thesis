

const byLength = arr => {
  const words = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'];
  let newArr = arr.filter(num => num >= 1 && num <= 9).sort((a, b) => b - a).map(num => words[num]);
  return newArr;
};

console.log(byLength([2, 1, 1, 4, 5, 8, 2, 3])); // ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
console.log(byLength([])); // []
console.log(byLength([1, -1, 55])); // ["One"]
<jupyter_output>
<empty_output>
<jupyter_text>
