const flipCase = (string) => {
    return string.split('').map(char => {
        if (/[a-z]/.test(char)) {
            return char.toUpperCase();
        } else {
            return char.toLowerCase();
        }
    }).join('');
}
