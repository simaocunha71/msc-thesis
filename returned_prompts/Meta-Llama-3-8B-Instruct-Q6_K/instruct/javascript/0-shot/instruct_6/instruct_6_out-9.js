    function uniqueTokens(str1, str2) {
        let result = '';
        for (let i = 0; i < str1.length; i++) {
            let token = '';
            for (let j = i; j < str1.length; j++) {
                if (str1[j] === ' ') {
                    break;
                }
                token += str1[j];
            }
            if (token.length > 0) {
                let found = false;
                for (let k = 0; k < str2.length; k++) {
                    if (str2[k] === ' ') {
                        break;
                    }
                    let token2 = '';
                    for (let l = k; l < str2.length; l++) {
                        if (str2[l] === ' ') {
                            break;
                        }
                        token2 += str2[l];
                    }
                    if (token === token2) {
                        found = true;
                        break;
                    }
                }
                if (!found) {
                    result += token + ' ';
                }
            }
        }
        return result.trim();
    }  // Don't forget to trim the result!  // Don't forget to trim the result!  // Don't forget to trim the result!  // Don't forget to trim the result!  // Don't forget to trim the result!  // Don't forget to trim the result!  // Don't forget to trim the result!  // Don't forget to trim the result!  // Don't forget to trim the result!  // Don't forget to trim the result!  // Don't forget to trim the result!  // Don't forget to trim the result!  // Don't forget to trim the result!  // Don't forget to trim the result!  // Don't forget to trim the result!  // Don't forget to trim the result!  // Don't forget to trim the result!  // Don't forget to trim the result!  // Don't forget to trim the result!  // Don't forget to trim the result!  // Don't forget to trim the result!  // Don't forget to trim the result!  // Don't forget to trim the result!  // Don't forget to trim the result!  // Don't forget to trim the result!  // Don't forget to trim the result!  // Don't forget to trim the result!  // Don't forget to trim the result!  // Don't forget