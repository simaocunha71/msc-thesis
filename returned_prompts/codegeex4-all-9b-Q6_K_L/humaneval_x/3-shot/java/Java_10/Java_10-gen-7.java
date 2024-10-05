        int i = 0;
        int j = string.length() - 1;
        while (i < j) {
            if (string.charAt(i)!= string.charAt(j)) {
                return string + new StringBuilder(string.substring(0, i)).reverse().toString();
            }
            i++;
            j--;
        }
        return string;
    }
}

