        Map<String, Integer> result = new HashMap<>();
        for (char c : test.toCharArray()) {
            result.merge(String.valueOf(c), 1, Integer::sum);
        }
        return result;
    }
}

