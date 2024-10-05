        List<Integer> result = new ArrayList<>(l);
        Collections.sort(result);
        for (int i = 0; i < result.size(); i += 2) {
            result.set(i, result.get(i / 2));
        }
        return result;
    }
}

