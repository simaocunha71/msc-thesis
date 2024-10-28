        String[] words = s.split(" ");
        StringBuilder result = new StringBuilder();

        for (String word : words) {
            StringBuilder sb = new StringBuilder();
            for (char c : word.toCharArray()) {
                sb.append((char) (c));
            }
            result.append(sb.toString());
        }
        return result.toString();
    }
}

