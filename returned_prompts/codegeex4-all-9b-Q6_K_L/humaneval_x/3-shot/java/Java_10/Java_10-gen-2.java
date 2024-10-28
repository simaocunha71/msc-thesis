        int i = 0;
        int j = string.length() - 1;
        while (i < j) {
            if (string.charAt(i)!= string.charAt(j)) {
                break;
            }
            i++;
            j--;
        }
        if (i == j) {
            return string;
        }
        return string + new StringBuilder(string.substring(0, i)).reverse().toString();
    }
}

