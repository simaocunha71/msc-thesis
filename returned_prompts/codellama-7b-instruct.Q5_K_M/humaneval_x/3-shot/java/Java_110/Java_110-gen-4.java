        if (lst1.stream().filter(x -> x % 2 != 0).count() == 0 &&
            lst2.stream().filter(x -> x % 2 != 0).count() == 0)
            return "YES";
        else
            return "NO";
    }
}

