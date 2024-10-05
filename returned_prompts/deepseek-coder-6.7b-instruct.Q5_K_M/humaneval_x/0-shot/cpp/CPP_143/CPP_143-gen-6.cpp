     int length = sentence.size();
     string words[length];
     string result = "";
     string temp = "";
     for(int i = 0; i < length; i++){
         if(sentence[i] != ' '){
             temp += sentence[i];
         }
         else{
             words[i] = temp;
             temp = "";
         }
     }
     words[length - 1] = temp;

     for(int i = 0; i < length; i++){
         int word_length = words[i].size();
         if(word_length > 1){
             int flag = 0;
             for(int j = 2; j*j <= word_length; j++){
                 if(word_