        List<Integer> result = new ArrayList<>();
        while (x > 0) {
            result.add(x % base);
            x /= base;
        }
        StringBuilder result_string = new StringBuilder();
        for (int i = result.size() - 1; i >= 0; i--) {
            result_string.append(result.get(i));
        }
        return result_string.toString();
    }
}

