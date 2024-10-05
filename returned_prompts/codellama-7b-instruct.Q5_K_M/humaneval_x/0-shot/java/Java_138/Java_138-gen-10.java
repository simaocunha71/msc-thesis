        int n1=n;
        int n2=n;
        int n3=n;
        int n4=n;
        if(n1%2==0){
            n1=n1/2;
            n2=n2/2;
            n3=n3/2;
            n4=n4/2;
            if(n1+n2+n3+n4==n){
                return true;
            }
        }
        else if(n2%2==0){
            n2=n2/2;
            n3=n3/2;
            n4=n4/2;
            if(n1+n2+n3+n4==n){
                return true;
            }
        }
        else if(n3%2==0){
            n3=n3/2;
            n4=n4/2;
            if(n1+n2+n3+n4==n){
                return true;
            }
        }
        else if(n4%2==0){
            n4=n4/2;
            if(n1+n2+n3+n4==n){
                return true;
            }
        }
        return false;
    }
}
