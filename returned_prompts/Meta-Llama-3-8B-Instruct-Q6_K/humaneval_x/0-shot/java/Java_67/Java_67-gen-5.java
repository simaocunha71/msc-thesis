    public int fruitDistribution(String s, int n) {
        String[] arr = s.split(" ");
        int apples = 0, oranges = 0;
        for (String str : arr) {
            if (str.endsWith("apples")) {
                apples = Integer.parseInt(str.substring(0, str.length() - 7));
            } else if (str.endsWith("oranges")) {
                oranges = Integer.parseInt(str.substring(0, str.length() - 8));
            }
        }
        return n - apples - oranges;
    }  