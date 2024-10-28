        int sum1 = 0;
        int sum2 = 0;
        for (String str : lst1) {
            sum1 += str.length();
        }
        for (String str : lst2) {
            sum2 += str.length();
        }
        if (sum1 <= sum2) {
            return lst1;
        } else {
            return lst2;
        }
    }
}

