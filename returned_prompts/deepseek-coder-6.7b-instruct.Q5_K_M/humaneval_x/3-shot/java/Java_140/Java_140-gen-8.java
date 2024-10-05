        StringBuilder result = new StringBuilder();
        int consecutiveSpaces = 0;
        for(char c : text.toCharArray()) {
            if(c == ' ') {
                consecutiveSpaces++;
                if(consecutiveSpaces == 2) {
                    result.append('-');
                    consecutiveSpaces = 1;
                }
            } else {
                if(consecutiveSpaces == 2) {
                    result.append('-');
                    consecutiveSpaces = 0;
                } else if(consecutiveSpaces == 1) {
                    result.append('_');
                    consecutiveSpaces = 0;
                }
                result.append(c);
            }
        }

        if(consecutiveSpaces == 2) {
            result.append('-');
        } else if(consecutiveSpaces == 1) {
            result.append('_');
        }

        return result.toString();
     }
}

