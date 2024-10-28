const isPalindrome = (text) => {
    if (text.length === 0) return true;
    const left = 0;
    const right = text.length - 1;
    while (left < right) {
        if (text[left] !== text[right]) return false;
        left++;
        right--;
    }
    return true;
};

