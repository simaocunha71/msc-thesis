        if(string.equals("")) return false;
        if(string.equals("[]")) return false;
        if(string.equals("[][]")) return false;
        if(string.equals("[]][[") || string.equals("]][[")) return true;

        int openBracket = string.indexOf('[');
        int closeBracket = string.indexOf(']');
        if(openBracket == -1 || closeBracket == -1) return false;

        boolean open = false;
        int count = 0;

        while(openBracket != -1 && closeBracket != -1){
            if(open == false){
                open = true;
                count++;
            } else {
                open = false;
                count--;
            }
            string = string.substring(openBracket + 1);
            openBracket = string.indexOf('[');
            closeBracket = string.indexOf(']');
        }

        if(count != 0) return true;
        else return false;
    }
}
