        List<Integer> result = new ArrayList<>();
        for (Object o : values) {
            if (o instanceof Integer) {
                result.add((Integer) o);
            }
        }
        return result;
    }
}

