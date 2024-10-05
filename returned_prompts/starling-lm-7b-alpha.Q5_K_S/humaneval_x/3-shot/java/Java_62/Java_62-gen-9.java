        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < xs.size() - 1; i++) {
            result.add(xs.get(i + 1) * (i + 1));
        }
        return result;
    }
}


