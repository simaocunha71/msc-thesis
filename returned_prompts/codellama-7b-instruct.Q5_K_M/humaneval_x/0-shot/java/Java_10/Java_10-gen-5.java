        if (string == null || string.length() == 0) {
            return "";
        }
        int maxLen = string.length();
        int i = 0;
        int j = string.length() - 1;
        while (i < j) {
            if (string.charAt(i) != string.charAt(j)) {
                break;
            }
            i++;
            j--;
        }
        int palindromeSuffixStart = i;
        int palindromeSuffixLen = maxLen - palindromeSuffixStart;
        int prefixLen = j - i - 1;
        String prefix = string.substring(0, j - i);
        String suffix = string.substring(palindromeSuffixStart);
        String revPrefix = new StringBuilder(prefix).reverse().toString();
        return prefix + revPrefix + suffix;
    }
}
