        char[] ch = s.toCharArray();
        for(int i = 0; i < ch.length; i++){
            if(Character.isLetter(ch[i])){
                if(Character.isLowerCase(ch[i])){
                    ch[i] = Character.toUpperCase(ch[i]);
                }
                else{
                    ch[i] = Character.toLowerCase(ch[i]);
                }
            }
        }
        return new String(ch);
    }
}

This is a solution to the problem. It checks each character in the string. If it is a letter, it changes its case. If it is not a letter, it leaves it as is.

