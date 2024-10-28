    vector<int> answer;
    int smallest = 0;
    int largest = 0;
    for(int i = 0; i < lst.size(); i++){
        if(lst[i] < 0 && largest < lst[i]){
            largest = lst[i];
        }
        else if(lst[i] > 0 && smallest > lst[i]){
            smallest = lst[i];
        }
    }
    if(largest < 0 && smallest < 0){
        smallest = 0;
        largest = 0;
    }
    answer.push_back(smallest);
    answer.push_back(largest);
    return answer;
}
int main(){
    vector<int> v{1, 2, 3, -4, -5, -6};
    vector<int> answer = largest_smallest_integers(v);
    printf("%d %d", answer[0], answer[1]);
    return 0;
}
