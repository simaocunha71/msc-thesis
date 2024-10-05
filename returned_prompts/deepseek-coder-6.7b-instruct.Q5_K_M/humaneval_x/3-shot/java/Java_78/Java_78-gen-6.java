        String primeHex = "2357BCDF";
        int count = 0;
        for (char c : num.toCharArray()) {
            if (primeHex.indexOf(c) != -1) {
                count++;
            }
        }
        return count;
    }
}

