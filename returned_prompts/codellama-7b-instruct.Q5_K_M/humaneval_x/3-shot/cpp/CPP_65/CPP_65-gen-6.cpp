    int original_x;
    int reverse_x;
    int temp;
    string original_string;
    string reverse_string;
    string final_string;
    original_x=x;
    reverse_x=0;
    original_string="";
    reverse_string="";
    final_string="";
    while (original_x>0){
        temp=original_x%10;
        original_string=to_string(temp)+original_string;
        original_x=original_x/10;
    }
    while (reverse_x<x){
        reverse_x=reverse_x*10+x%10;
        x=x/10;
    }
    while (reverse_x>0){
        temp=reverse_x%10;
        reverse_string=to_string(temp)+reverse_string;
        reverse_x=reverse_x/10;
    }
    if (shift>original_string.length()){
        reverse_string=reverse_string+original_string;
    }
    else {
        for (int i=0;i<original_string.length()-shift;i++){
            final_string+=original_string[i];
        }
        for (int i=0;i<shift;i++){
            final_string+=reverse_string[i];
        }
    }
    return final_string;
}


