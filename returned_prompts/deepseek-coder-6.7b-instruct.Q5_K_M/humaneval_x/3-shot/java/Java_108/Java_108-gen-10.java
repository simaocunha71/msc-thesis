        int count = 0;

        for(Integer num : arr) {
            int sum = 0;
            String numStr = num.toString();

            for(char c : numStr.toCharArray()) {
                sum += Character.getNumericValue(c);
            }

            if(sum > 0) {
                count++;
            }
        }

        return count;
    }
}

