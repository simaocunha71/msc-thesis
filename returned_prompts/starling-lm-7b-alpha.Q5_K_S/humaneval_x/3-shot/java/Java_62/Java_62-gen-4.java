        List<Integer> result = new ArrayList<>();
        result.add(xs.get(0));
        for (int i = 1; i < xs.size(); i++) {
            result.add(result.get(i - 1) + xs.get(i) * (i + 1));
        }
        return result;
    }
}

