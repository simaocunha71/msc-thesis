        String result = "";
        for(int i = 0; i < string.length(); i++) {
            char c = string.charAt(i);
            if(Character.isLowerCase(c)) {
                result += Character.toUpperCase(c);
            } else {
                result += Character.toLowerCase(c);
            }
        }
        return result;
    }

public static void main(String[] args) {
    Solution solution = new Solution();
    System.out.println(solution.flipCase("Hello"));
}

}