const allPrefixes = (string) => {
    let prefixes = [];
    for (let i = 0; i < string.length; i++) {
        let prefix = string.slice(0, i + 1);
        prefixes.push(prefix);
    }
    return prefixes;
};

