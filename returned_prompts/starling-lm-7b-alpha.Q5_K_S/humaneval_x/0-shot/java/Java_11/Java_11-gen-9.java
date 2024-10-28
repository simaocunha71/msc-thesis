        int i = 0, j = 0;
        StringBuilder sb = new StringBuilder();

        while (i < a.length() && j < b.length()) {
            if (a.charAt(i) == b.charAt(j)) {
                if (a.charAt(i) == '0') {
                    sb.append('0');
                } else {
                    sb.append('1');
                }
            } else {
                sb.append('1');
            }
            i++;
            j++;
        }

        while (i < a.length()) {
            if (a.charAt(i) == '0') {
                sb.append('0');
            } else {
                sb.append('1');
            }
            i++;
        }

        while (j < b.length()) {
            if (b.charAt(j) == '0') {
                sb.append('0');
            } else {
                sb.append('1');
            }
            j++;
        }

        return sb.toString();
    }
}




















































































































































































































































