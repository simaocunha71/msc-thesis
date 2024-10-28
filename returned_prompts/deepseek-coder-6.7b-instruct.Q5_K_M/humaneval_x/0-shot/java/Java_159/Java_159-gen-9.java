        List<Integer> result = new ArrayList<>();
        int total = number;
        if(need <= remaining) {
            total += need;
            remaining -= need;
        } else {
           