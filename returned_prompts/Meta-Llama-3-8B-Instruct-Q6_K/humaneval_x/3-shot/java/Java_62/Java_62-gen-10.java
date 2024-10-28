        List<Integer> result = new ArrayList<>();
        result.add(xs.get(1)); // coefficient of x
        for (int i = 2; i < xs.size(); i++) {
            result.add(xs.get(i) * i); // coefficient of x^i
        }
        return result;
    }
}

