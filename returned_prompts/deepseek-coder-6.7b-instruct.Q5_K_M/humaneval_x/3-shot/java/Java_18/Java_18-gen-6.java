        int count = 0;
        int idx = 0;

        while (idx < string.length()) {
            idx = string.indexOf(substring, idx);
            if (idx != -1) {
                count ++;
                idx += substring.length();
            } else {
                break;
            }
        }

        return count;
     }
}

