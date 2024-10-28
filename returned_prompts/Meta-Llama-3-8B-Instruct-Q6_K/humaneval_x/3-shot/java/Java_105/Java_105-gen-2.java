        List<String> result = new ArrayList<>();
        List<Integer> sorted = new ArrayList<>();
        for (int i : arr) {
            if (i >= 1 && i <= 9) {
                sorted.add(i);
            }
        }
        Collections.sort(sorted);
        for (int i = 0; i < sorted.size(); i++) {
            result.add(String.valueOf(sorted.get(sorted.size() - 1 - i)));
        }
        for (String s : result) {
            switch (Integer.parseInt(s)) {
                case 1:
                    result.set(result.indexOf(s), "One");
                    break;
                case 2:
                    result.set(result.indexOf(s), "Two");
                    break;
                case 3:
                    result.set(result.indexOf(s), "Three");
                    break;
                case 4:
                    result.set(result.indexOf(s), "Four");
                    break;
                case 5:
                    result.set(result.indexOf(s), "Five");
                    break;
                case 6:
                    result.set(result.indexOf(s), "Six");
                    break;
                case 7:
                    result.set(result.indexOf(s), "Seven");
                    break;
                case 8:
                    result.set(result.indexOf(s), "Eight");
                    break;
                case 9:
                    result.set(result.indexOf(s), "Nine");
                    break;
            }
        }
        return result;
    }
}