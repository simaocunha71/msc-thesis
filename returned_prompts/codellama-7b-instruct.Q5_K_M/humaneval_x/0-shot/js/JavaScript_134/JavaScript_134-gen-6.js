function checkIfLastCharIsALetter(str) {
    // Check if the last character is a letter
    if (/[a-zA-Z]$/.test(str)) {
        // Check if the last character is not part of a word
        if (!/[a-zA-Z]$/.test(str)) {
            return true;
        }
    }
    return false;
}

