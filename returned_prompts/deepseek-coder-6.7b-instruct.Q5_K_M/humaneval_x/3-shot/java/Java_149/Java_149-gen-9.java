        List<String> result = new ArrayList<>();
        int maxLength = 0;

        for (String word : lst) {
            if (word.length() % 2 == 0) {
                result.add(word);
                maxLength = Math.max(maxLength, word.length());
            }
        }

        Collections.sort(result);

        List<String> finalList = new ArrayList<>();
        for (int length = 2; length <= maxLength; length += 2) {
            List<String> temp = new ArrayList<>();
            for (String word : result) {
                if (word.length() == length) {
                    temp.add(word);
                }
            }
            if (!temp.isEmpty()) {
                finalList.addAll(temp);
            }
        }

        return finalList;
    }
}

