    string result;
    int units=number%10;
    int tens=(number/10)%10;
    int hundreds=(number/100)%10;
    int thousands=number/1000;
    switch(thousands)
    {
        case 1: result+="m";break;
        case 2: result+="mm";break;
        case 3: result+="mmm";break;
    }
    switch(hundreds)
    {
        case 1: result+="c";break;
        case 2: result+="cc";break;
        case 3: result+="ccc";break;
        case 4: result+="cd";break;
        case 5: result+="d";break;
        case 6: result+="dc";break;
        case 7: result+="dcc";break;
        case 8: result+="dccc";break;
        case 9: result+="cm";break;
    }
    switch(tens)
    {
        case 1: result+="x";break;
        case 2: result+="xx";break;
        case 3: result+="xxx";break;
        case 4: result+="xl";break;
        case 5: result+="l";break;
        case 6: result+="lx";break;
        case 7: result+="lxx";break;
        case 8: result+="lxxx";break;
        case 9: result+="xc";break;
    }
    switch(units)
    {
        case 1: result+="i";break;
        case 2: result+="ii";break;
        case 3: result+="iii";break;
        case 4: result+="iv";break;
        case 5: result+="v";break;
        case 6: result+="vi";break;
        case 7: result+="vii";break;
        case 8: result+="viii";break;
        case 9: result+="ix";break;
    }
    return result;
}

