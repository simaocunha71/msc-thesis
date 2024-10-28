        List<String> result = new ArrayList<>();
        List<Integer> temp = new ArrayList<>();
        String[] names = {"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};

        for (int num : arr) {
            if (num >= 1 && num <= 9) {
                temp.add(num);
            }
        }

        Collections.sort(temp, Collections.reverseOrder());

        for (int num : temp) {
            result.add(names[num - 1]);
        }

        return result;
    }
}

