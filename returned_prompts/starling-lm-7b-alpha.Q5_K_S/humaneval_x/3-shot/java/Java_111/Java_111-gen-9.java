        Map<String, Integer> result = new HashMap<>();
        for (char c : test.toLowerCase().toCharArray()) {
            result.merge(c + "", 1, Integer::sum);
        }
        return result;
    }
}

