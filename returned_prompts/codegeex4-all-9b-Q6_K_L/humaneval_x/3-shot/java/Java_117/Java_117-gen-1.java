        List<String> result = new ArrayList<>();
        String[] words = s.split(" ");
        for (String word : words) {
            int count = 0;
            for (char c : word.toCharArray()) {
                if ("bcdfghjklmnpqrstvwxyz".indexOf(Character.toLowerCase(c)) != -1) {
                    count++;
                }
            }
            if (count == n) {
                result.add(word);
            }
        }
        return result;
    }
}

