        StringBuilder result = new StringBuilder();
        int i = 0;
        while (i < a.length() && i < b.length()) {
            if (a.charAt(i) == b.charAt(i)) result.append('0');
            else result.append('1');
            i += 1;
        }
        while (i < a.length()) {
            if (a.charAt(i) == '1') result.append('1');
            else result.append('0');
            i += 1;
        }
        while (i < b.length()) {
            if (b.charAt(i) == '1') result.append('1');
            else result.append('0');
            i += 1;
        }
        return result.toString();

    }
}

