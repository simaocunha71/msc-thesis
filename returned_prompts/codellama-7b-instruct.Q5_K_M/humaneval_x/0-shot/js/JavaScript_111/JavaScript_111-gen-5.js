const histogram = (string) => {
    let hist = {};
    let letters = string.split(' ');

    letters.forEach(letter => {
        if (letter in hist) {
            hist[letter] += 1;
        } else {
            hist[letter] = 1;
        }
    });

    return hist;
}

B:
const histogram = (string) => {
    const hist = {};
    string.split(' ').forEach(letter => {
        if (letter in hist) {
            hist[letter] += 1;
        } else {
            hist[letter] = 1;
        }
    });
    return hist;
}

C:
const histogram = (string) => {
  let hist = {};
  string.split(' ').forEach(letter => {
    hist[letter] = hist[letter] || 0;
    hist[letter]++;
  });
  return hist;
}