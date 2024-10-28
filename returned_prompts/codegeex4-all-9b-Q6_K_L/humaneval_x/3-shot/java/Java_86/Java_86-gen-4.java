        String[] words = s.split(" ");
        StringBuilder sb = new StringBuilder();
        for (String word : words) {
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            sb.append(new String(chars));
            sb.append(" ");
        }
        return sb.toString().trim();
    }
}

