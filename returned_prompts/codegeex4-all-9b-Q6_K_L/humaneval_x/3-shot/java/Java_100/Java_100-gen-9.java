        List<Integer> result = new ArrayList<>();
        int current_number = n;
        for (int i = 0; i < n; i++) {
            result.add(current_number);
            current_number = current_number + 2;
        }
        return result;
    }
}

