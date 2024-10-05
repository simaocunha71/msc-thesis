const removeDuplicates = (numbers) => numbers.filter((num, index) => numbers.indexOf(num) === index);

B:
const removeDuplicates = (numbers) => numbers.filter((num, index) => numbers.lastIndexOf(num) === index);

C:
const removeDuplicates = (numbers) => numbers.filter((num) => numbers.indexOf(num) === numbers.lastIndexOf(num));

D:
const removeDuplicates = (numbers) => numbers.filter((num, index) => numbers.lastIndexOf(num) === index && numbers.indexOf(num) === index);
