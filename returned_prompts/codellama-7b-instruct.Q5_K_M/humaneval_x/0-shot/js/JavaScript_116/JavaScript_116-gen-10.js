const sortArray = (arr) => arr.sort((a, b) => a.toString(2).split('1').length - b.toString(2).split('1').length || a - b);

B:
const sortArray = (arr) => arr.sort((a, b) => a.toString(2).match(/1/g) && b.toString(2).match(/1/g) ? a.toString(2).match(/1/g).length - b.toString(2).match(/1/g).length : a - b);

C:
const sortArray = (arr) => arr.sort((a, b) => a.toString(2).split('').filter(c => c === '1').length - b.toString(2).split('').filter(c => c === '1').length || a - b);

D:
const sortArray = (arr) => arr.sort((a, b) => a.toString(2).match(/1/g).length - b.toString(2).match(/1/g).length || a - b);
