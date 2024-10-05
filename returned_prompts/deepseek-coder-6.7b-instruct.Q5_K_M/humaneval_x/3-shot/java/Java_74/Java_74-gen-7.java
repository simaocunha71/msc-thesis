        int sum1 = lst1.stream().mapToInt(String::length).sum();
        int sum2 = lst2.stream().mapToInt(String::length).sum();

        if (sum1 < sum2) return lst1;
        else if (sum1 > sum2) return lst2;
        else return lst1;
     }
}

