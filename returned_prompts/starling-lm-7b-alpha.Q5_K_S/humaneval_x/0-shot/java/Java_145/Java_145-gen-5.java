    List<Integer> result = new ArrayList<>();
    List<Integer> temp = new ArrayList<>();
    for(int i = 0; i < nums.size(); i++) {
        temp.add(nums.get(i));
    }

    Collections.sort(temp, (a, b) -> {
        int sumA = sumOfDigits(a);
        int sumB = sumOfDigits(b);
        if(sumA == sumB) {
            return Integer.compare(a, b);
        }
        return Integer.compare(sumA, sumB);
    });

    for(int i = 0; i < temp.size(); i++) {
        result.add(temp.get(i));
    }

    return result;
    }

    public int sumOfDigits(int i) {
        String s = String.valueOf(i);
        int sum = 0;
        for(int j = 0; j < s.length(); j++) {
            sum += Integer.parseInt(s.substring(j, j + 1));
        }
        return sum;
    }
}



















































































































































































































































