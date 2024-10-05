        List<String> romanNumbers = new ArrayList<String>();
        romanNumbers.add("M");
        romanNumbers.add("CM");
        romanNumbers.add("D");
        romanNumbers.add("CD");
        romanNumbers.add("C");
        romanNumbers.add("XC");
        romanNumbers.add("L");
        romanNumbers.add("XL");
        romanNumbers.add("X");
        romanNumbers.add("IX");
        romanNumbers.add("V");
        romanNumbers.add("IV");
        romanNumbers.add("I");

        List<Integer> numbers = new ArrayList<Integer>();
        numbers.add(1000);
        numbers.add(900);
        numbers.add(500);
        numbers.add(400);
        numbers.add(100);
        numbers.add(90);
        numbers.add(50);
        numbers.add(40);
        numbers.add(10);
        numbers.add(9);
        numbers.add(5);
        numbers.add(4);
        numbers.add(1);

        String roman = "";
        int n = number;

        while (n > 0) {
            for (int i = 0; i < numbers.size(); i++) {
                if (n >= numbers.get(i)) {
                    n -= numbers.get(i);
                    roman += romanNumbers.get(i);
                    break;
                }
            }
        }

        return roman;
    }
}