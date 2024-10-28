        List<Integer> result = new ArrayList<>();
        int current_stones = n;

        for  (int i = 0; i < n; i++) {
            result.add(current_stones);
            current_stones = current_stones % 2 == 0 ? current_stones + 2 : current_stones + 2;
        }
        return result;
     }
}

