const rescaleToUnit = numbers => numbers.map(num => (num - Math.min(...numbers)) / (Math.max(...numbers) - Math.min(...numbers)));

