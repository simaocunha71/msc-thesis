        List<Integer> result = new ArrayList<>();
        while (n > 0) {
            result.add(n);
            n = (n % 2 == 0) ? n + 1 : n + 2;
        }
        return result;
    }
}

