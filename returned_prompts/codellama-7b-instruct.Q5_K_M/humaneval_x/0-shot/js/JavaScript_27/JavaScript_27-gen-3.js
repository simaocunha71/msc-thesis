        int i = 0;
        int j = string.length() - 1;
        while (i < j) {
            if (string.charAt(i)!= string.charAt(j)) {
                break A;
            }
            i++;
            j--;
        }
        String prefix = string.substring(0, i);
        String suffix = string.substring(i, string.length());
        String reversedSuffix = new StringBuilder(suffix).reverse().toString();
        return prefix + reversedSuffix + suffix;
    }
}

