const rescaleToUnit = (numbers) => numbers.map(x => x-Math.min(...numbers))/Math.max(...numbers)
