        List<String> result = new ArrayList<>();
        List<Integer> validNums = new ArrayList<>();
        String[] names = {"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};

        for (int num : arr) {
            if (num >= 1 && num <= 9) {
                validNums.add(num);
            }
        }

        validNums.sort(Collections.reverseOrder());

        for (int num : validNums) {
            result.add(names[num - 1]);
        }

        return result;
    }
}

