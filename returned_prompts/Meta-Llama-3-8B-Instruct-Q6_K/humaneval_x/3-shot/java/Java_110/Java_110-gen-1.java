        Set<Integer> set2 = new HashSet<>(lst2);
        for (int num : lst1) {
            if (num % 2 != 0) {
                if (!set2.remove(num)) {
                    return "NO";
                }
            }
        }
        return "YES";
    }
}

