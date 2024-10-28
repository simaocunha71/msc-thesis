        List<String> result = new ArrayList<>();
        for (String word : s.split("[,\\s]+")) {
            result.add(word);
        }
        return result;
    }
}

