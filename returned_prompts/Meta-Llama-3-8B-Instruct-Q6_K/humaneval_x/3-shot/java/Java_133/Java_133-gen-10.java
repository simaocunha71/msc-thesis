        int sum = 0;
        for (Double num : lst) {
            double ceilNum = Math.ceil(num);
            sum += (int) Math.pow(ceilNum, 2);
        }
        return sum;
    }
}

