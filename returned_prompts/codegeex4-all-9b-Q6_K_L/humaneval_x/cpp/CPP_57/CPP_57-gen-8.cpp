bool isIncreasing = true;
bool isDecreasing = true;
for(int i=0; i<l.size()-1; i++){
    if(l[i]>l[i+1]){
        isIncreasing = false;
    }
    if(l[i]<l[i+1]){
        isDecreasing = false;
    }
}
return isIncreasing || isDecreasing;
}