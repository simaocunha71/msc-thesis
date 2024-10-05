        String[] num = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        int[] num2 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

        String[] str = numbers.split(" ");
        int[] num3 = new int[str.length];
        for (int i = 0; i < str.length; i++) {
            for (int j = 0; j < num.length; j++) {
                if (num[j].equals(str[i])) {
                    num3[i] = num2[j];
                    break;
                }
            }
        }
        for (int i = 0; i < num3.length - 1; i++) {
            for (int j = 0; j < num3.length - i - 1; j++) {
                if (num3[j] > num3[j + 1]) {
                    int temp = num3[j];
                    num3[j] = num3[j + 1];
                    num3[j + 1] = temp;
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < num3.length; i++) {
            sb.append(num[num3[i]]);
            if (i != num3.length - 1) {
                sb.append(" ");
            }
        }
        return sb.toString();
    }
}

