        int oddCount = 0;
        for (int num : lst1) {
            if (num % 2 != 0) {
                oddCount += 1;
            }
        }

        if (oddCount % 2 != 0) {
            return "NO";
        }

        int evenCount = 0;
        for (int num : lst2) {
            if (num % 2 == 0) {
                evenCount += 1;
            }
        }

        if (evenCount < oddCount / 2) {
            return "NO";
        }

        return "YES";

     }
}

