    int n = word.length();
    int i = 0;
    for(i = 0; i < n; i++) {
        if(word.charAt(i) == 'a' || word.charAt(i) == 'e' || word.charAt(i) == 'i' || word.charAt(i) == 'o' || word.charAt(i) == 'u') {
            break;
        }
    }

    if(i == n) {
        return "";
    }

    int j = i + 1;
    while(j < n) {
        if(word.charAt(j) == 'a' || word.charAt(j) == 'e' || word.charAt(j) == 'i' || word.charAt(j) == 'o' || word.charAt(j) == 'u') {
            break;
        }
        j++;
    }

    if(j == n) {
        return "";
    }

    int vowel_i = i + 1;
    int vowel_j = n - j;

    if(vowel_i < vowel_j) {
        return word.charAt(i + 1) + "";
    } else {
        return word.charAt(n - j) + "";
    }

    }
}







```
