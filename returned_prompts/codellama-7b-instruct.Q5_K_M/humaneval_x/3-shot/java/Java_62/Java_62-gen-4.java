        List<Integer> result = new ArrayList<>();
        int length = xs.size();
        for (int i = 1; i < length; i++) {
            result.add(xs.get(i) * i);
        }
        return result;
    }
}

