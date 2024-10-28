
function capCount(s) {
    let cap = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === s[i].toUpperCase()) {
            cap++;
        }
    }
    return cap;
}

function lowCount(s) {
    let low = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === s[i].toLowerCase()) {
            low++;
        }
    }
    return low;
}

function strength(s) {
    return capCount(s) - lowCount(s);
}

function extensionName(s) {
    return s.split('')
        .reduce((acc, v) => {
            if (v === v.toUpperCase()) {
                acc.cap++;
            } else {
                acc.low++;
            }
            return acc;
        }, {cap: 0, low: 0})
        .low;
}

function indexOfMaxStrength(extensions) {
    return extensions.reduce((acc, val, i) => {
        if (strength(val) > strength(extensions[acc])) {
            return i;
        }
        return acc;
    }, 0);
}

return class_name + '.' + extensions[indexOfMaxStrength(extensions)];

};









































































































































































