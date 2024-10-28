        List<String> result = new ArrayList<>();
        s = s.toLowerCase();
        for (String word : s.split(" ")) {
            int count = 0;
            for (char c : word.toCharArray()) {
                if ("bcdfghjklmnpqrstvwxyz".contains(Character.toString(c))) {
                    count += 1;
                }
            }
            if (count == n) {
                result.add(word);
            }
        }
        return result;
    }
}

