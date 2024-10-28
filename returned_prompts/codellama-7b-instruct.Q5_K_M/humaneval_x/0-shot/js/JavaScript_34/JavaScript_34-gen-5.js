const unique = (l) => {
    const seen = new Set();
    return l.filter(item => {
        if (seen.has(item)) {
            return false;
        } else {
            seen.add(item);
            return true;
        }
    }).sort();
};

