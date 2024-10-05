        String rev_string = new StringBuffer(string).reverse().toString();
        int i = 0;
        int j = string.length() - 1;
        while (i < j) {
            if (string.charAt(i) != rev_string.charAt(j)) {
                string = string.substring(0, i + 1) + rev_string.substring(0, j);
                return string;
            }
            i++;
            j--;
        }
        return string;
    }
}

