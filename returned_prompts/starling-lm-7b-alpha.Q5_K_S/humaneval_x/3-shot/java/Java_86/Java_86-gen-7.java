        String[] words = s.split(" ");
        StringBuilder result = new StringBuilder();
        for (String word : words) {
            StringBuilder tmp = new StringBuilder();
            for (char c : word.toCharArray()) {
                tmp.append((char) (c + 1));
            }
            result.append(tmp).append(" ");
        }
        return result.toString().trim();
    }
}


