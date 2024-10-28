        if (txt.indexOf(' ') != -1) {
            return Arrays.asList(txt.split("\\s+"));
        } else if (txt.indexOf(',') != -1) {
            return Arrays.asList(txt.split(","));
        } else {
            int count = 0;
            for (char c : txt.toCharArray()) {
                if (Character.isLetter(c) && Character.toLowerCase(c) - 'a' % 2 == 1) {
                    count++;
                }
            }
            return count;
        }
    }
}

