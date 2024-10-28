        List<Integer> result = new ArrayList<>();
        if (xs.size() == 0) return result;

        result.add(xs.get(1));
        for (int i = 2; i < xs.size(); i++) {
            result.add(result.get(i - 2) + xs.get(i) * i);
        }
        return result;
    }
}

