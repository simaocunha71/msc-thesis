        int evenCount = 0;
        int oddCount = 0;
        String numStr = String.valueOf(Math.abs(num));
        for (int i = 0; i < numStr.length(); i++) {
            int n = Integer.parseInt(String.valueOf(numStr.charAt(i)));
            if (n % 2 == 0) {
                evenCount++;
            } else {
                oddCount++;
            }
        }
        List<Integer> result = new ArrayList<>();
        result.add(evenCount);
        result.add(oddCount);
        return result;
    }
}

