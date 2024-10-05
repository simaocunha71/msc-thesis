        // Create a buffer to store the decoded string.
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c != '0' && c != '1' && c != '2' && c != '3' && c != '4' && c != '5' && c != '6' && c != '7' && c != '8' && c != '9') {
                break A;
            }
        }
        if (i != s.length()) {
            return "Invalid input.";
        }
        // Create a buffer to store the decoded string.
        StringBuilder sb = new StringBuilder();

        while (s.length() > 0) {
            // get a digit from the string.
            int c = s.charAt(s.length() - 1) - '0';

            // if the buffer is not empty, insert the digit to it.
            if (sb.length() > 0) {
                sb.insert(0, c);
            } else {
                sb.append(c);
            }

            // remove the last digit from the string.
            s = s.substring(0, s.length() - 1);
        }

        return sb.toString();
    }
}































































































































































































