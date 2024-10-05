        List<String> result = new ArrayList<>();
        for (String word : txt.split(" ")) {
            result.add(word);
        }
        if (result.size() > 0) {
            return result;
        } else {
            int count = 0;
            for (int i = 0; i < txt.length(); i++) {
                if (txt.charAt(i) == ',') {
                    count += 1;
                }
            }
            if (count > 0) {
                return result;
            } else {
                for (int i = 0; i < txt.length(); i++) {
                    if (i % 2 == 1) {
                        count += 1;
                    }
                }
                return count;
            }
        }
    }
}

