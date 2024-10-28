        int sum1 = lst1.stream().map(String::length).reduce(0, Integer::sum);
        int sum2 = lst2.stream().map(String::length).reduce(0, Integer::sum);

        if (sum1 < sum2) {
            return lst1;
        } else {
            return lst2;
        }
    }
}

