        if(lst.isEmpty())
            return new ArrayList<Optional<Integer>>(){{
                add(Optional.empty());
                add(Optional.empty());
            }};

        int smallest = lst.get(0), largest = lst.get(0);
        for(int i: lst) {
            if(i < 0 && i < smallest)
                smallest = i;
            else if(i > 0 && i > largest)
                largest = i;
        }

        if(smallest == Integer.MAX_VALUE)
            smallest = Optional.empty();
        if(largest == Integer.MIN_VALUE)
            largest = Optional.empty();

        return new ArrayList<Optional<Integer>>(){{
            add(Optional.ofNullable(smallest));
            add(Optional.ofNullable(largest));
        }};
    }
}

