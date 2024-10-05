        if(arr.isEmpty()) return Optional.empty();

        int sum = 0;
        int sign = 1;

        for(Integer num: arr) {
            if(num < 0) {
                sign *= -1;
            } else if(num > 0) {
                sign *= 1;
            }

            sum += Math.abs(num);
        }

        return Optional.of(sum * sign);
     }
}

