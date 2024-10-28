        int i = 0;
        int j = string.length() - 1;
        while (i < j) {
            if (string.charAt(i)!= string.charAt(j)) {
                break;
            }
            i++;
            j--;
        }
        String suffix = string.substring(i);
        return string + new StringBuilder(suffix).reverse().toString();
    }
}

