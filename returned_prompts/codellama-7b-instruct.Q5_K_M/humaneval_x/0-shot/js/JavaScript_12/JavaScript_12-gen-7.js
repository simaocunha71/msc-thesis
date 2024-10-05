const longest = (strings) => {
    if (strings.length === 0) return null;
    let longest = strings[0];
    for (let i = 1; i < strings.length; i++) {
        if (strings[i].length > longest.length) longest = strings[i];
    }
    return longest;
}

B:
const longest = (strings) => {
    if (strings.length === 0) return null;
    let longest = {length: 0, string: null};
    for (let string of strings) {
        if (string.length > longest.length) longest = {length: string.length, string};
    }
    return longest.string;
}

C:
const longest = (strings) => {
    if (strings.length === 0) return null;
    let longest = {length: 0, string: null};
    for (let string of strings) {
        if (string.length > longest.length) longest = {length: string.length, string};
    }
    return longest.string;
}

D:
const longest = (strings) => {
    if (strings.length === 0) return null;
    let longest = {length: 0, string: null};
    for (let string of strings) {
        if (string.length > longest.length) longest = {length: string.length, string};
    }
    return longest.string;
}
