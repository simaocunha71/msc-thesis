        char[] arr = new char[a.length()];
        for(int i=0;i<a.length();i++) {
            if(a.charAt(i) == '0' && b.charAt(i) == '0') {
                arr[i] = '0';
            }
            else if(a.charAt(i) == '0' && b.charAt(i) == '1') {
                arr[i] = '1';
            }
            else if(a.charAt(i) == '1' && b.charAt(i) == '0') {
                arr[i] = '1';
            }
            else {
                arr[i] = '0';
            }
        }
        return String.valueOf(arr);
    }

    /**
    Input are two strings a and b consisting of uppercase letters A to Z.
    Perform a string XOR operation on these inputs and return result also as a string.
    >>> stringXor("ABC", "DEF")
    "GHI"
     */
    public String stringXor(String a, String b) {
        int[] arr = new int[a.length()];
        for(int i=0;i<a.length();i++) {
            arr[i] = a.charAt(i) ^ b.charAt(i);
        }
        return String.valueOf(arr);
    }
}









































































































































































