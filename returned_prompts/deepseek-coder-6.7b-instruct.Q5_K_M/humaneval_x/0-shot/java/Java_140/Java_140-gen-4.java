        StringBuilder str = new StringBuilder();
        int count = 0;
        for(int i=0; i<text.length(); i++){
            if(text.charAt(i) == ' '){
                count++;
                if(count == 1) str.append('_');
                if(count > 1 && i+1<text.length() && text.charAt(i+1) == ' ') str.append('-');
            }
            else{
                if(count > 0){
                    while(count > 0){
                        str.append('_');
                        count--;
                    }
                    count = 0;
                }
                str.append(text.charAt(i));
            }
        }
        while(count > 0){
            str.append('_');
            count--;
        }
        return str.toString();
    }
}


A: The problem with your solution is that you are checking the next character even if it's beyond the length of the string. 
Here's the corrected code:
public String fixSpaces(String text) {
    StringBuilder str = new StringBuilder();
    int count = 0;
    for(int i=0; i<text.length(); i++){
        if(text.charAt(i) == ' '){
            count++;
            if(count == 1) str.append('_');
            if(count > 1 && (i+1<text.length() && text.charAt(i+1) == ' ')) str.append('-');
        }
        else{
            if(count > 0){
                while(count > 0){
                    str.append('_');
                    count--;
                }
                count = 0;
            }
            str.append(text.charAt(i));
        }
    }
    return str.toString();
}

This code works by iterating through each character in the string. If it encounters a space, it increments a count and appends either an underscore or a hyphen to the string builder depending on the count. If it encounters a non-space character, it appends the underscores from the count to the string builder and res