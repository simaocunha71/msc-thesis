const rescaleToUnit = (numbers) => numbers.map(n => n - Math.min(...numbers)) / Math.max(...numbers);

