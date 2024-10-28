    sort(l.begin(), l.end());
    int len = l.size();
    if(len % 2 == 0){
        return (l[len/2 - 1] + l[len/2]) / 2;
    }else{
        return l[len/2];
    }
}

int main(){
    vector<float> l1 = {3, 1, 2, 4, 5};
    vector<float> l2 = {-10, 4, 6, 1000, 10, 20};
    printf("Median of l1: %f\n", median(l1));
    printf("Median of l2: %f\n", median(l2));
    return 0;
}

*/

