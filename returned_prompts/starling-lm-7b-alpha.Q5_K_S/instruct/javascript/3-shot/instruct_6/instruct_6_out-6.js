function unique_tokens(str1, str2) {
    const tokens1 = str1.split(' ');
    const tokens2 = str2.split(' ');
    const unique_tokens = [];

    for (let i = 0; i < tokens1.length; i++) {
        let token = tokens1[i];
        for (let j = 0; j < tokens2.length; j++) {
            if (token === tokens2[j]) {
                continue;
            }
            unique_tokens.push(token);
            break;
        }
    }

    return unique_tokens.join(' ');
}

