    public int fruitDistribution(String s, int n) {
        String[] parts = s.split(" ");
        int apples = 0;
        int oranges = 0;
        
        for (String part : parts) {
            if (part.endsWith("apples")) {
                apples = Integer.parseInt(part.substring(0, part.length() - 7));
            } else if (part.endsWith("oranges")) {
                oranges = Integer.parseInt(part.substring(0, part.length() - 8));
            }
        }
        
        return n - apples - oranges;
    } 

