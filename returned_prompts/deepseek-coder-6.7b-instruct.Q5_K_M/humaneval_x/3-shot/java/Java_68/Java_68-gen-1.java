        if(arr.size() == 0) return new ArrayList<>();

        int min_even_val = Integer.MAX_VALUE;
        int min_even_index = -1;

        for(int i=0; i<arr.size(); i++) {
            if(arr.get(i) % 2 == 0 && arr.get(i) <= min_even_val) {
                min_even_val = arr.get(i);
                min_even_index = i;
            }
        }

        if(min_even_index == -1) return new ArrayList<>();
        return Arrays.asList(min_even_val, min_even_index);
    }
}

