        List<Integer> maxList = new ArrayList<Integer>();
        if(numbers.size()>0){
            maxList.add(numbers.get(0));
        }
        for(int i=1; i<numbers.size(); i++){
            maxList.add(Math.max(maxList.get(i-1), numbers.get(i)));
        }
        return maxList;
    }
}