    let levels = [];
    let i = 0;
    while (i < paren_string.length) {
        let j = i;
        while (paren_string[j] === '(') {
            j++;
            levels.push(0);
        }
        let k = i;
        while (paren_string[k] === ')') {
            k++;
            levels[levels.length - 1]++;
        }
        i = Math.max(j, k);
    }
    return levels;
};

parseNestedParens('(()()) ((())) () ((())()())');






// My Solution
function parseNestedParens(parenString) {
    let result = [];
    let curLevel = 0;
    for (let i = 0; i < parenString.length; i++) {
        if (parenString[i] === '(') {
            curLevel++;
        } else if (parenString[i] === ')') {
            curLevel--;
        } else {
            result.push(curLevel);
        }
    }
    return result;
}

parseNestedParens('(()()) ((())) () ((())()())');







// My Solution
function parseNestedParens(parenString) {
    let levels = [];
    let curLevel = 0;
    for (let i = 0; i < parenString.length; i++) {
        if (parenString[i] === '(') {
            curLevel++;
        } else if (parenString[i] === ')') {
            curLevel--;
        } else {
            levels.push(curLevel);
        }
    }
    return levels;
}

parseNestedParens('(()()) ((())) () ((())()())');












































































