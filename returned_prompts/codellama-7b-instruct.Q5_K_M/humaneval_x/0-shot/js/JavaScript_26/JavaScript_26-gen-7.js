const removeDuplicates = (numbers) => {
    const seen = new Set();
    return numbers.filter((number) => {
        if (!seen.has(number)) {
            seen.add(number);
            return true;
        }
        return false;
    });
};

