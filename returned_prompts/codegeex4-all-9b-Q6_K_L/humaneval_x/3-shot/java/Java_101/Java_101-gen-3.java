        List<String> result = new ArrayList<>();
        String[] words = s.split("[, ]");
        for (String word : words) {
            result.add(word);
        }
        return result;
    }
}

