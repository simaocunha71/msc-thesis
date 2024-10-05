        int length = string.length();
        for (int i = length / 2; i >= 0; i--) {
            int j = length - i;
            if (string.charAt(i) != string.charAt(j)) {
                continue;
            }
            int k = i + 1;
            while (k < j) {
                if (string.charAt(k) != string.charAt(j)) {
                    break;
                }
                k++;
                j--;
            }
            if (k == j) {
                return string.substring(i, j + 1);
            }
        }
        return "";
    }
}

