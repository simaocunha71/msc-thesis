        int evenCount = 0;
        for (int num : lst1) {
            if (num % 2 == 0) {
                evenCount++;
            }
        }

        if (evenCount == lst1.size()) {
            return "YES";
        } else {
            for (int num : lst2) {
                if (num % 2 == 0) {
                    evenCount++;
                }
            }

            if (evenCount >= evenCount) {
                return "YES";
            } else {
                return "NO";
            }
        }
    }
}

