        List<Integer> result = new ArrayList<>();
        result.add(0);
        for (int i = 0; i < xs.size() - 1; i++) {
            result.set(i, xs.get(i + 1));
        }
        result.set(result.size() - 1, result.get(result.size() - 1) + 1);
        return result;
    }
}

