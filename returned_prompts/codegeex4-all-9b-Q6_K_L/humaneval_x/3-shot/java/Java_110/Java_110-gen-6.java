        boolean lst1HasOdd = lst1.stream().anyMatch(n -> n % 2 != 0);
        boolean lst2HasEven = lst2.stream().anyMatch(n -> n % 2 == 0);

        return lst1HasOdd && lst2HasEven ? "YES" : "NO";
    }
}

