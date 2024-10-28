        if(a.length() != b.length()){
            return "Error: Lengths of both strings are not equal.";
        }
        int[] arr = new int[a.length()];
        int[] arr2 = new int[a.length()];
        for(int i = 0; i < a.length(); i++) {
            if(a.charAt(i) == '0' && b.charAt(i) == '0') {
                arr[i] = 0;
                arr2[i] = 0;
            }
            if(a.charAt(i) == '1' && b.charAt(i) == '1') {
                arr[i] = 1;
                arr2[i] = 1;
            }
            if(a.charAt(i) == '0' && b.charAt(i) == '1') {
                arr[i] = 1;
                arr2[i] = 0;
            }
            if(a.charAt(i) == '1' && b.charAt(i) == '0') {
                arr[i] = 0;
                arr2[i] = 1;
            }
        }
        StringBuilder sb = new StringBuilder("");
        for(int i = 0; i < arr.length; i++) {
            sb.append(arr[i] ^ arr2[i]);
        }
        return sb.toString();
    }
}



























































































































































