    string result="";
    while (number>0)
    {
        if (number>=1000){
            result+='m';
            number-=1000;
        }
        if (number>=900){
            result+='c';
            result+='m';
            number-=900;
        }
        if (number>=500){
            result+='d';
            number-=500;
        }
        if (number>=400){
            result+='c';
            result+='d';
            number-=400;
        }
        if (number>=100){
            result+='c';
            number-=100;
        }
        if (number>=90){
            result+='x';
            result+='c';
            number-=90;
        }
        if (number>=50){
            result+='l';
            number-=50;
        }
        if (number>=40){
            result+='x';
            result+='l';
            number-=40;
        }
        if (number>=10){
            result+='x';
            number-=10;
        }
        if (number>=9){
            result+='i';
            result+='x';
            number-=9;
        }
        if (number>=5){
            result+='v';
            number-=5;
        }
        if (number>=4){
            result+='i';
            result+='v';
            number-=4;
        }
        if (number>=1){
            result+='i';
            number-=1;
        }
    }
    return result;
}

