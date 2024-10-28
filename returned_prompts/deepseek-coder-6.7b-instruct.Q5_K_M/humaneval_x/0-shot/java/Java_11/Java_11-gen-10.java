        String result = "";

        for(int i=0; i<a.length(); i++) {

B:
            if(a.charAt(i) == b.charAt(i)) {
                result += "0";
            } else {
                result += "1";
            }
        }

        return result;
    }
}

I understand that this solution has a time complexity of O(n), where n is the length of the input string. The space complexity is also O(n).

