const isBored = (S) => {
    let boredoms = 0;
    let sentences = S.split('.');
    for (let sentence of sentences) {
        if (sentence.startsWith('I')) {
            boredoms++;
        }
    }
    return boredoms;
};
