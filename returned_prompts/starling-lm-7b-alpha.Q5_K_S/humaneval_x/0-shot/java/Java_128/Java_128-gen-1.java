    if(arr.size() == 0) {
        return Optional.empty();
    }

    long product = 1;

    for(int i = 0; i < arr.size(); i++) {
        int num = arr.get(i);
        if(num == 0) {
            return Optional.of(0);
        } else if(num < 0) {
            product *= -1;
        } else {
            product *= 1;
        }
    }

    long sum = 0;

    for(int i = 0; i < arr.size(); i++) {
        int num = arr.get(i);
        if(num < 0) {
            sum -= Math.abs(num);
        } else {
            sum += Math.abs(num);
        }
    }

    if(product > 0) {
        return Optional.of((int) sum);
    } else {
        return Optional.of((int) -sum);
    }

}

}








































































































































































































































































