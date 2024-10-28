        if (txt.contains(" ")) {
            String[] words = txt.split(" ");
            return Arrays.asList(words);
        } else if (txt.contains(",")) {
            String[] words = txt.split(",");
            return Arrays.asList(words);
        } else {
            int result = 0;
            for (char c : txt.toCharArray()) {
                if (c >= 'a' && c <= 'z') {
                    if ((c - 'a') % 2 == 1) {
                        result += 1;
                    }
                }
            }
            return result;
        }
    }
}

