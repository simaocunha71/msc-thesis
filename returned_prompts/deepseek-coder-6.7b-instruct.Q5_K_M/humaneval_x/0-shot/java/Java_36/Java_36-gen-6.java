        int count = 0;
        for(int i = 11; i < n; i++){
            if(i % 11 == 0 || i % 13 == 0){
                count += countDigit(i, 7);
            }
        }
        return count;
    }

    public int countDigit(int number, int digit) {
        int counter = 0;
        String