        if (arr.size() == 0) return Optional.empty();
        long result = 0;
        for (int i = 0; i < arr.size(); i++) {
            int sign = arr.get(i) > 0 ? 1 : arr.get(i) < 0 ? -1 : 0;
            result += Math.abs(sign * arr.get(i));
        }
        return Optional.of((int) result);
    }
}

