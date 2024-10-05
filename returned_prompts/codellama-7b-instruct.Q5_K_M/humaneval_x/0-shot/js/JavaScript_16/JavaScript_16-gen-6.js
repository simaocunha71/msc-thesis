function countDistinctCharacters(string) {
    var distinctCharacters = 0;
    for (var i = 0; i < string.length; i++) {
        var currentChar = string.charAt(i);
        var isCharPresent = false;
        for (var j = 0; j < i; j++) {
            if (currentChar === string.charAt(j)) {
                isCharPresent = true;
                break;
            }
        }
        if (!isCharPresent) {
            distinctCharacters++;
        }
    }
    return distinctCharacters;
}

