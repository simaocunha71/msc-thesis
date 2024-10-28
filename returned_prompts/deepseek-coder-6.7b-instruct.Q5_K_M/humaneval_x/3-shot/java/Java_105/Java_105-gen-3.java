        List<String> names = new ArrayList<>();
        List<Integer> numbers = new ArrayList<>();

        for (Integer num : arr) {
            if (num >= 1 && num <= 9) {
                numbers.add(num);
            }
        }

        Collections.sort(numbers, Collections.reverseOrder());

        for (Integer num : numbers) {
            switch (num) {
                case 1:
                    names.add("One");
                    break;
                case 2:
                    names.add("Two");
                    break;
                case 3:
                    names.add("Three");
                    break;
                case 4:
                    names.add("Four");
                    break;
                case 5:
                    names.add("Five");
                    break;
                case 6:
                    names.add("Six");
                    break;
                case 7:
                    names.add("Seven");
                    break;
                case 8:
                    names.add("Eight");
                    break;
                case 9:
                    names.add("Nine");
                    break;
            }
        }
        return names;
    }
}

