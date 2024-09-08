    // Convert all the spaces to underscores
    for(int i=0; i<text.length(); i++){
        if(text[i] == ' '){
            text[i] = '_';
        }
    }
    // Check for more than 2 consecutive spaces and replace with -
    for(int i=0; i<text.length(); i++){
        if(text[i] == ' ' && i+1 < text.length() && text[i+1] == ' '){
            if(i+2 < text.length() && text[i+2] == ' '){
                // Replace all consecutive spaces with -
                text.replace(i, 3, "-");
            }
            else{
                // Replace all consecutive spaces with -
                text.replace(i, 2, "-");
            }
        }
    }
    return text;
}