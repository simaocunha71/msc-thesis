        StringBuilder sb = new StringBuilder();

        for(int i = 0; i < a.length(); i++) {
            if(a.charAt(i) == b.charAt(i)) {
                sb.append('0');
            } else {
                sb.append('1');
            }
        }

        return sb.toString();
    }

}

The solution to this problem is to iterate through each index of the input strings. If the corresponding character of both strings are the same, append 0 to the StringBuilder. If they are not the same, append 1 to the StringBuilder.

After going through all the characters in the input strings, return the result as a string.
*/


/*
