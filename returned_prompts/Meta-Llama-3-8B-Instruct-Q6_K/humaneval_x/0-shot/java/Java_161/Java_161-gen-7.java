        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < s.length(); i++){
            if(Character.isLetter(s.charAt(i))){
                sb.append(Character.isUpperCase(s.charAt(i))? Character.toLowerCase(s.charAt(i)) : Character.toUpperCase(s.charAt(i)));
            }else{
                sb.append(s.charAt(i));
            }
        }
        return sb.reverse().toString();
    }
}
Solution solution = new Solution();
System.out.println(solution.solve("1234")); // prints "4321"
System.out.println(solution.solve("ab")); // prints "AB"
System.out.println(solution.solve("#a@C")); // prints "#A@c"







