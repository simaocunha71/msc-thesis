        String[] words = txt.split(" ");
        if (words.length > 1) return Arrays.asList(words);
        else if (txt.indexOf(',') != -1) return Arrays.asList(txt.split(","));
        else {
            int count = 0;
            for (char c : txt.toCharArray()) {
                if (Character.isLowerCase(c) && c % 2 == 1) {
                    count += 1;
                }
            }
            return count;
        }
    }
}

