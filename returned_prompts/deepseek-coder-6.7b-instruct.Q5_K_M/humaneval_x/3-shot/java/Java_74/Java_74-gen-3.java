        int sum1 = lst1.stream().mapToInt(String::length).sum();
        int sum2 = lst2.stream().mapToInt(String::length).sum();

        return sum1 < sum2 ? lst1 : lst2;
    }
}

