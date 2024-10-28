        List<Optional<Integer>> result = new ArrayList<Optional<Integer>>();
        Optional<Integer> largest = Optional.empty();
        Optional<Integer> smallest = Optional.empty();

        for(Integer i : lst){
            if(i < 0 && (smallest.isEmpty() || i < smallest.get())){
                smallest = Optional.of(i);
            }
            if(i > 0 && (largest.isEmpty() || i > largest.get())){
                largest = Optional.of(i);
            }
        }
        result.add(largest);
        result.add(smallest);
        return result;
    }
}

