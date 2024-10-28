        StringBuilder result = new StringBuilder();
        long i = number;
        while (i > 0) {
            int rem = (int) (i % 2);
            i /= 2;
            result.append(rem);
        }
        return result.reverse().toString();
    }
}








```
