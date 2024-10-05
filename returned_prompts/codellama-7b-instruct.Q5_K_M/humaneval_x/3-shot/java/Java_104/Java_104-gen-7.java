        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < x.size(); i++) {
            if (x.get(i) % 2 != 0) {
                result.add(x.get(i));
            }
        }
        result.sort((a, b) -> a - b);
        return result;
    }
}

