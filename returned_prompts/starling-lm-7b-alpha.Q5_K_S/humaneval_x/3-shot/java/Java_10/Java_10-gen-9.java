        String result = string;
        StringBuilder sb = new StringBuilder(string);
        while (true) {
            int i = sb.length() - 1;
            while (i > 0 && sb.charAt(i) == sb.charAt(sb.length() - i - 1)) {
                i--;
            }
            if (i == 0) {
                break;
            }
            sb.setLength(i + 1);
            result = sb.reverse().toString() + result;
        }
        return result;
    }
}

