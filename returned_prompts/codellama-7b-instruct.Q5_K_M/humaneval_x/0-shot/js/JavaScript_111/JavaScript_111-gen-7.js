const histogram = (str) => {
    const letters = str.split(' ');
    const counts = {};

    letters.forEach(letter => {
        if (counts[letter] === undefined) {
            counts[letter] = 0;
        }
        counts[letter]++;
    });

    return counts;
}

*/
