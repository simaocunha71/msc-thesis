
    var uniqueTokens = function(str1, str2) {
      var uniqueTokens = "";

      for (var i = 0; i < str1.length; i++) {
        var token = str1[i];
        var found = false;

        for (var j = 0; j < str2.length; j++) {
          if (str2[j] === token) {
            found = true;
            break;
          }
        }

        if (!found) {
          uniqueTokens += token;
        }
      }

      return uniqueTokens;
    };

    var str1 = "a b c d e";
    var str2 = "b c d";
    var result = uniqueTokens(str1, str2);

    console.log(result); // "a e"
