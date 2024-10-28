        if(arr.isEmpty())
            return new ArrayList<>();

        int smallestEven = Integer.MAX_VALUE;
        int smallestIndex = -1;
        for(int i = 0; i < arr.size(); i++){
            int num = arr.get(i);
            if(num % 2 == 0 && num < smallestEven){
                smallestEven = num;
                smallestIndex = i;
            }
        }
        if(smallestEven == Integer.MAX_VALUE)
            return new ArrayList<>();
        List<Integer> res = new ArrayList<>();
        res.add(smallestEven);
        res.add(smallestIndex);
        return res;
    }
}
