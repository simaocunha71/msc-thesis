        int i = 0;
        int j = string.length() - 1;
        while (i < j) {
            if (string.charAt(i) != string.charAt(j)) {
                break A;
            }
            i++;
            j--;
        }
        int k = i;
        int l = j;
        while (k < j) {
            if (string.charAt(k) != string.charAt(l)) {
                break A;
            }
            k++;
            l--;
        }
        String prefix = string.substring(0, k+1);
        String postfix = string.substring(l);
        String revPrefix = new StringBuilder(prefix).reverse().toString();
        return prefix + revPrefix + postfix;
    }
}