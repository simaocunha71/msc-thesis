        if  (lst.size()  < 2) {
            return Optional.empty();
        }

        int smallest = Integer.MAX_VALUE;
        int secondSmallest = Integer.MAX_VALUE;

        for  (int num : lst) {
            if  (num < smallest) {
                secondSmallest = smallest;
                smallest = num;
            } else if  (num > smallest && num < secondSmallest) {
                secondSmallest = num;
            }
        }

        if  (secondSmallest == Integer.MAX_VALUE) {
            return Optional.empty();
        }
        return Optional.of(secondSmallest);
     }
}

