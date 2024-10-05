        int sum = 0;
        for (Double num : lst) {
            int roundedNum = (int) Math.ceil(num);
            sum += roundedNum * roundedNum;
        }
        return sum;
     }
}

