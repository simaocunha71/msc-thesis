    char[] arr = text.toCharArray();
    String ans = "";
    for (char c : arr) {
        if (!(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')) {
            ans += c;
        }
    }
    return ans;
    }
}




```
