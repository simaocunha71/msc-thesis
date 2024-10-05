        String[] words = s.split(" ");
        StringBuilder result = new StringBuilder();

        for (String word : words) {
            char[] charArray = word.toCharArray();
            Arrays.sort(charArray);
            result.append(new String(charArray)).append(" ");
        }

        return result.toString().trim();
    }
}

