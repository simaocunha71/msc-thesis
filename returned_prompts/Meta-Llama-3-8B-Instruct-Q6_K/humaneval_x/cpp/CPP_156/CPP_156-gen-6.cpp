    string result = "";

    if(number >= 1000){
        result += "m";
        number -= 1000;
    }
    if(number >= 900){
        result += "cm";
        number -= 900;
    }
    if(number >= 500){
        result += "d";
        number -= 500;
    }
    if(number >= 400){
        result += "cd";
        number -= 400;
    }
    if(number >= 100){
        switch(number/100){
            case 1:
                result += "c";
                break;
            case 2:
                result += "cc";
                break;
            case 3:
                result += "ccc";
                break;
        }
        number %= 100;
    }
    if(number >= 90){
        result += "xc";
        number -= 90;
    }
    if(number >= 50){
        switch(number/50){
            case 1:
                result += "l";
                break;
            case 2:
                result += "ll";
                break;
            case 3:
                result += "lxx";
                break;
        }
        number %= 50;
    }
    if(number >= 40){
        result += "xl";
        number -= 40;
    }
    if(number >= 10){
        switch(number/10){
            case 1:
                result += "x";
                break;
            case 2:
                result += "xx";
                break;
            case 3:
                result += "xxx";
                break;
        }
        number %= 10;
    }
    if(number >= 9){
        result += "ix";
        number -= 9;
    }
    if(number >= 5){
        switch(number/5){
            case 1:
                result += "v";
                break;
            case 2:
                result += "vv";
                break;
            case 3:
                result += "vxx";
                break;
        }
        number %= 5;
    }
    if(number >= 4){
        result += "iv";
        number -= 4;
    }
    if(number > 0){
        switch(number){
            case 1:
                result += "i";
                break;
            case 2:
                result += "ii";
                break;
            case 3:
                result += "iii";
                break;
        }
    }
    return result;
}

B:
    return result;
}

int main() {
    printf