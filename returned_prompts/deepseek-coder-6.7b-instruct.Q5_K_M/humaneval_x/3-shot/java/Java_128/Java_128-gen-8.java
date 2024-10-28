        if(arr.size() == 0) return Optional.empty();

        int sign = 1;
        int sum = 0;
        for(int num : arr) {
            if(num < 0) sign *= -1;
            sum += Math.abs(num);
        }
        return Optional.of(sign * sum);
    }
}

