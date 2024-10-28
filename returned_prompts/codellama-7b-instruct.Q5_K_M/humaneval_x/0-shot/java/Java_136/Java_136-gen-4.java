        Optional<Integer> largest = Optional.empty();
        Optional<Integer> smallest = Optional.empty();
        for (Integer i: lst){
            if (i < 0 && (largest.isEmpty() || i > largest.get())){
                largest = Optional.of(i);
            }
            if (i > 0 && (smallest.isEmpty() || i < smallest.get())){
                smallest = Optional.of(i);
            }
        }

        return Arrays.asList(largest, smallest);
    }
}