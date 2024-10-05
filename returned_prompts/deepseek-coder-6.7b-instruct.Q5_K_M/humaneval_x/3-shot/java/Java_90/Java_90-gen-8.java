        if(lst.size() < 2) return Optional.empty();
        int first = Integer.MAX_VALUE;
        int second = Integer.MAX_VALUE;
        for(int n : lst){
            if(n < first){
                second = first;
                first = n;
            }else if(n < second && n != first){
                second = n;
            }
        }
        return (second == Integer.MAX_VALUE)? Optional.empty() : Optional.of(second);
    }
}

