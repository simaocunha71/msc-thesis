        List<String> words = new ArrayList<>();
        List<Integer> validNums = new ArrayList<>();
        String[] names = {"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};

        for(int num : arr) {
            if(num>=1 && num<=9) {
                validNums.add(num);
            }
        }

        Collections.sort(validNums, Collections.reverseOrder());

        for(int num : validNums) {
            words.add(names[num]);
        }

        return words;

     }
}

