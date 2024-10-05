const intersperse = (numbers, delimeter) => numbers.reduce((a, c, i, arr) => a.concat(c, i < arr.length - 1 ? delimeter : ''), []);
