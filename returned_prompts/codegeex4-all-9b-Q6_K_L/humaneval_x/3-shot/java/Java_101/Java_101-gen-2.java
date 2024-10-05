        List<String> result = new ArrayList<>();
        String[] words = s.split("[,\\s]+");
        for (String word : words) {
            result.add(word);
        }
        return result;
    }
}

