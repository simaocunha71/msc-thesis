        List<Integer> result = new ArrayList<>();
        result.add(1);
        result.add(3);
        result.add(2);
        for (int i = 0; i < n - 3; i++) {
            int temp = result.get(result.size() - 1) + result.get(result.size() - 2) + result.get(result.size() - 3);
            result.add(temp);
        }
        return result;
    }
}

