const splitWords = (txt) => {
	const words = txt.split(/\s+/);
	if (words.length > 1) {
		return words;
	}
	const commas = txt.split(/,/);
	if (commas.length > 1) {
		return commas;
	}
	let count = 0;
	for (let i = 0; i < txt.length; i++) {
		if (txt[i] === txt[i].toLowerCase() && i % 2 !== 0) {
			count++;
		}
	}
	return count;
};
