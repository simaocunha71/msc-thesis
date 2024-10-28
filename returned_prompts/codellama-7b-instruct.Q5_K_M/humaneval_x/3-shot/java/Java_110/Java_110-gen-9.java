        if (lst1.size() == 0 || lst2.size() == 0) return "NO";

        for (int i : lst1) {
            if (i % 2 != 0) return "NO";
        }

        for (int i : lst2) {
            if (i % 2 != 0) return "NO";
        }

        return "YES";
    }
}

