        List<Integer> result = new ArrayList<>();
        int current = n;
        while (current > 0) {
            result.add(current);
            current += n % 2 == 0 ? 2 : 1;
        }
        return result;
    }
}

