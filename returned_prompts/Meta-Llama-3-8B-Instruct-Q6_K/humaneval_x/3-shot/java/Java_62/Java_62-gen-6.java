        List<Integer> result = new ArrayList<>();
        result.add(xs.get(1)); // derivative of xs[0] is 0
        for (int i = 2; i < xs.size(); i++) {
            result.add(xs.get(i) * i);
        }
        return result;
    }
}

