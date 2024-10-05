        List<String> words = Arrays.asList(s.split(" "));
        List<String> result = new ArrayList<String>();
        String consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ";

        for (String word : words) {
            int count = 0;
            for (char c : word.toCharArray()) {
                if (consonants.indexOf(c) != -1) {
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

