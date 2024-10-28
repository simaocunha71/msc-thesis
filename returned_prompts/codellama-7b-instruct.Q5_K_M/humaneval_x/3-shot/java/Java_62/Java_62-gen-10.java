        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < xs.size() - 1; i++) {
            result.add(xs.get(i) * (i + 1));
        }
        return result;
    }
}

