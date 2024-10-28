        int result = 0;
        for (char c : num.toCharArray()) {
            if (c == '2' || c == '3' || c == '5' || c == '7' || c == 'B' || c == 'D' || c == 'F') {
                result += 1;
            }
        }
        return result;
    }
}



```