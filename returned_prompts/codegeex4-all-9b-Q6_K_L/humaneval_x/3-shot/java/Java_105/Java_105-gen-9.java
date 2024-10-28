        List<String> result = new ArrayList<>();
        List<String> digits = Arrays.asList("One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine");

        for (Integer i : arr) {
            if (i >= 1 && i <= 9) {
                result.add(digits.get(i - 1));
            }
        }

        Collections.sort(result, new Comparator<String>() {
            public int compare(String a, String b) {
                return b.length() - a.length();
            }
        });

        return result;
    }
}

