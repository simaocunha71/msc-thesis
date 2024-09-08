    int i = 0;
    while(pow(i,3)<a){
        i++;
    }
    if(pow(i,3) == a) return true;
    else return false;
}

int main()
{
    printf("%d\n",iscuber(1));  //true
    printf("%d\n",iscube(2));    //false
    printf("%d\n",iscube(-1));   //true
    printf("%d\n",iscube(64));   //true
    printf("%d\n",iscube(0));    //true
    printf("%d\n",iscube(180));  //false

    return 0;
}
