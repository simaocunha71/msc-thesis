        List<Integer> result = new ArrayList<>();

        while (x > 0) {
            result.add(x % base);
            x /= base;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = result.size() - 1; i >= 0; i--) {
            sb.append(result.get(i));
        }
        return sb.toString();
    }
}

