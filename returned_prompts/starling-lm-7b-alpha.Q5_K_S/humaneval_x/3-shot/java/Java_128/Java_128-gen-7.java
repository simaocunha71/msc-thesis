        if (arr.size() == 0) return Optional.empty();
        int sign = 1;
        long result = 0;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) < 0) sign *= -1;
            result += Math.abs(arr.get(i));
        }
        return Optional.of((int) (result * sign));
    }
}

