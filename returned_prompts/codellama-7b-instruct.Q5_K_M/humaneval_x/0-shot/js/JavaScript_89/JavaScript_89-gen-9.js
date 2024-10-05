const encrypt = (s) => {
    const alphabet = 'abcdefghijklmnopqrstuvwxyz';
    const shiftedAlphabet = alphabet.slice(2) + alphabet.slice(0, 2);
    return s.split('').map(char => shiftedAlphabet[alphabet.indexOf(char)]).join('');
}

