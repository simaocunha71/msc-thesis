        if(arr.isEmpty()) return Optional.empty();

        int sum = 0;
        int sign = 1;

        for(int i : arr){
            if(i < 0){
                sign *= -1;
                sum += Math.abs(i);
            } else if(i > 0){
                sum += i;
            }
        }

        return Optional.of(sum * sign);
     }
}

