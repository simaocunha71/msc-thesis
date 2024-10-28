
    function findUniqueTokens(str1, str2) {
        var tokens1 = str1.split(" ");
        var tokens2 = str2.split(" ");
        var uniqueTokens = [];
        for (var i = 0; i < tokens1.length; i++) {
            for (var j = 0; j < tokens2.length; j++) {
                if (tokens1[i] == tokens2[j]) {
                    continue;
                }
            }
            uniqueTokens.push(tokens1[i]);
        }
        return uniqueTokens.join(" ");
    }

