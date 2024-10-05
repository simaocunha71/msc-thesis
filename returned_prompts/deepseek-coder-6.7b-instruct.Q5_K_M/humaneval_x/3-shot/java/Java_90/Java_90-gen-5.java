        if(lst.size() < 2){
            return Optional.empty();
        }
        int firstMin = Integer.MAX_VALUE;
        int secondMin = Integer.MAX_VALUE;
        for(int num: lst){
            if(num < firstMin){
                secondMin = firstMin;
                firstMin = num;
            }else if(num > firstMin && num < secondMin){
                secondMin = num;
            }
        }
        if(secondMin == Integer.MAX_VALUE){
            return Optional.empty();
        }
        return Optional.of(secondMin);
    }
}

