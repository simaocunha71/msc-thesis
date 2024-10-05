    string encrypted = "";
    for(int i=0; i<s.length(); i++){
        char c = s[i];
        if(c >= 'a' && c <= 'z'){
            c = (c - 'a' + 2*2) % 26 + 'a';
        }else if(c >= 'A' && c <= 'Z'){
            c = (c - 'A' + 2*2) % 26 + 'A';
        }
        encrypted += c;
    }
    return encrypted;
}  // This function takes a string, iterates over each character, 
   // and checks if it's a lowercase or uppercase letter. 
   // If it's a letter, it shifts it down by 2 times 2 (which is 8) places. 
   // The result is added to a new string, which is then returned.  // This function takes a string, iterates over each character, 
   // and checks if it's a lowercase or uppercase letter. 
   // If it's a letter, it shifts it down by 2 times 2 (which is 8) places. 
   // The result is added to a new string, which is then returned.  // This function takes a string, iterates over each character, 
   // and checks if it's a lowercase or uppercase letter. 
   // If it's a letter, it shifts it down by 2 times 2 (which is 8) places. 
   // The result is added to a new string, which is then returned.  // This function takes a string, iterates over each character, 
   // and checks if it's a lowercase or uppercase letter. 
   // If it's a letter, it shifts it down by 2 times 2 (which is 8) places. 
   // The result is added to a new string, which is then returned.  // This function takes a string, iterates over each character, 
   // and checks if it's a lowercase or uppercase letter. 
   // If it's a letter, it shifts it down by 2 times 2 (which is 8) places. 
   // The result is added to a new string, which is then returned.  // This function takes a string, iterates over each character, 
   // and checks if it's a lowercase or uppercase letter. 
   // If it's a letter, it shifts it down