        List<Integer> result = new ArrayList<>();
        result.add(0);
        for (int i = 1; i < xs.size(); i++) {
            result.set(i - 1, i * xs.get(i));
        }
        return result;
    }
}

