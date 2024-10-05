        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < xs.size(); i++) {
            int derivative = 0;
            for (int j = i; j < xs.size(); j++) {
                derivative += j * xs.get(j);
            }
            result.add(derivative);
        }
        return result;
    }
}
