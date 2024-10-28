        String[] words = s.split(" ");
        StringBuilder result = new StringBuilder();
        for (String word : words) {
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            result.append(chars);
            result.append(" ");
        }
        result.deleteCharAt(result.length() - 1);
        return result.toString();
    }
}

