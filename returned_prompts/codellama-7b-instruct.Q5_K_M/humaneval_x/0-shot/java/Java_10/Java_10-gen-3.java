        int i = 0;
        int j = string.length() - 1;
        int k = string.length();
        while (i < j) {
            if (string.charAt(i)!= string.charAt(j)) {
                k = j;
                break;
            }
            i++;
            j--;
        }
        String suffix = string.substring(k);
        String prefix = string.substring(0, k);
        prefix = new StringBuilder(prefix).reverse().toString();
        return string + prefix + suffix;
    }
}
