        int sum1 = 0, sum2 = 0;
        for(String s : lst1) sum1 += s.length();
        for(String s : lst2) sum2 += s.length();

        return sum1 < sum2 ? lst1 : lst2;
    }
}

