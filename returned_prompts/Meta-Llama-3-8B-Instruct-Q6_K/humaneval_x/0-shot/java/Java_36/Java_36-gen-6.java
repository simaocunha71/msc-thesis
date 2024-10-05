int count = 0;
int num = 11;
while(num < n) {
    if(num % 11 == 0 || num % 13 == 0) {
        String str = String.valueOf(num);
        if(str.contains("7")) {
            count++;
        }
    }
    num++;
}
return count;
}
}
