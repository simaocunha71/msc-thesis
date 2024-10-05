    if (arr.size() == 0) {
        return Optional.empty();
    }
    long sum = 0;
    long product = 1;
    for (int i : arr) {
        if (i == 0) {
            product = 0;
            break;
        }
        sum += Math.abs(i);
        if (i < 0) {
            product *= -1;
        } else {
            product *= 1;
        }
    }
    if (product == 0) {
        return Optional.empty();
    }
    return Optional.of((int) sum * product);
}
}



class Solution {
    /**
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all