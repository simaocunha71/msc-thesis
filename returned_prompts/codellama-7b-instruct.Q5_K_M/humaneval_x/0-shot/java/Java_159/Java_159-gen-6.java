        if(number>1000 || need>1000 || remaining>1000){
            return null;
        }
        int total = number+remaining;
        int eaten = total-number;
        int left = total-eaten;
        List<Integer> result = new ArrayList<>();
        result.add(eaten);
        result.add(left);
        return result;
    }
}


