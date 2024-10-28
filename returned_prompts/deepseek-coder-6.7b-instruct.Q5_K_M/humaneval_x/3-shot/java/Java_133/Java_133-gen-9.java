        int sum = 0;
        for (double d : lst) {
            int rounded = (int)Math.ceil(d);
            sum += rounded * rounded;
        }
        return sum;
     }
}

