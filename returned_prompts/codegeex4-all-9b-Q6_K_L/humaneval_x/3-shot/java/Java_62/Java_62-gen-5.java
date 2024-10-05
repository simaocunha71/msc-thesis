        List<Integer> result = new ArrayList<>();

        for (int i = 1; i < xs.size(); i++) {
            int derivative = xs.get(i) * i;
            result.add(derivative);
        }
        return result;
    }
}

