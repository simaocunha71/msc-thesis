        String hex_digits = "2357BDF";
        int count = 0;

        for(char c : num.toCharArray()){
            if(hex_digits.contains(Character.toString(c))){
                count++;
            }
        }
        return count;
    }
}

