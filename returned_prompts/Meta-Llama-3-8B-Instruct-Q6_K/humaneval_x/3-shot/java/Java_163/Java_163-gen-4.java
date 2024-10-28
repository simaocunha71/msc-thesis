        List<Integer> result = new ArrayList<>();
        for (int i = Math.min(a, b); i <= Math.max(a, b); i++) {
            if (i % 2 == 0) {
                result.add(i);
            }
        }
        Collections.sort(result);
        return result;
    }
}

