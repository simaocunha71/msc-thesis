function uniqueTokens(str1, str2) {
    var tokens1 = str1.split(' ');
    var tokens2 = str2.split(' ');
    var result = [];

    for (var i = 0; i < tokens1.length; i++) {
        for (var j = 0; j < tokens2.length; j++) {
            if (tokens1[i] === tokens2[j]) {
                continue;
            }
        }
        result.push(tokens1[i]);
    }

    return result.join(' ');
}

