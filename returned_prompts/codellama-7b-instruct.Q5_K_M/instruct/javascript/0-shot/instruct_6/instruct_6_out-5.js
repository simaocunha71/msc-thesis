    function getUniqueTokens(str1, str2) {
        var uniqueTokens = "";

        for (var i = 0; i < str1.length; i++) {
            var token = str1[i];

            if (!str2.includes(token)) {
                uniqueTokens += token + " ";
            }
        }

        return uniqueTokens;
    }

