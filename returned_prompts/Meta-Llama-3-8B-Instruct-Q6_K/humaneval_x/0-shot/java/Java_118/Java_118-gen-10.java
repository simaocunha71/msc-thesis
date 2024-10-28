    public String getClosestVowel(String word) {
        char[] arr = word.toCharArray();
        int n = arr.length;
        for (int i = n - 1; i >= 0; i--) {
            if (isVowel(arr[i])) {
                if (i < n - 1 && !isVowel(arr[i + 1])) {
                    return String.valueOf(arr[i]);
                }
                if (i > 0 && !isVowel(arr[i - 1])) {
                    return String.valueOf(arr[i]);
                }
            }
        }
        return "";
    }

    public boolean isVowel(char c) {
        c = Character.toLowerCase(c);
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}
