        int sum = 0;
        for (Object obj : lst) {
            if (obj instanceof Integer) {
                Integer num = (Integer) obj;
                if (num > 0 && num % 2 == 1) {
                    sum += num * num;
                }
            }
        }
        return sum;
     }
}

