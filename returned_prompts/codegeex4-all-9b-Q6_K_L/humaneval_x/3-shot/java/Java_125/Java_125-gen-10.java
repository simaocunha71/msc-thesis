        if (txt.indexOf(' ') == -1) {
            if (txt.indexOf(',') == -1) {
                int count = 0;
                for (char c : txt.toCharArray()) {
                    if (c >= 'a' && c <= 'z') {
                        if ((c - 'a') % 2 == 1) count += 1;
                    }
                }
                return count;
            } else {
                return Arrays.asList(txt.split(","));
            }
        } else {
            return Arrays.asList(txt.split(" "));
        }
    }
}

