    List<Object> result = new ArrayList<>();
    StringBuilder sb = new StringBuilder(s);
    for(int i=0;i<c.length();i++) {
        for(int j=sb.length()-1;j>=0;j--) {
            if(sb.charAt(j)==c.charAt(i)) {
                sb.deleteCharAt(j);
            }
        }
    }
    result.add(sb.toString());
    result.add(isPalindrome(sb.toString()));
    return result;
}
    public boolean isPalindrome(String str) {
    int n = str.length();
    for(int i=0;i<n/2;i++) {
        if(str.charAt(i)!=str.charAt(n-i-1)) {
            return false;
        }
    }
    return true;
}
}






































```