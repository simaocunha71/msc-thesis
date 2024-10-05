        int sum = 0;
        for (double num : lst) {
            int ceil = (int) Math.ceil(num);
            sum += ceil * ceil;
        }
        return sum;
     }
}

