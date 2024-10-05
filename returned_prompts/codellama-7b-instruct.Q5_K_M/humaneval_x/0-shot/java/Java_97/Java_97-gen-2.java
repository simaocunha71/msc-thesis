        int result = 0;
        int temp = 0;
        while(a!=0 || b!=0){
            if(a%10!=0){
                temp = temp + a%10*b%10;
                result = result*10 + temp%10;
            }
            a = a/10;
            b = b/10;
            temp = temp/10;
        }
        return result;
    }
}

