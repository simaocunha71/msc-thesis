    vector<int> res(2);
    int neg_max = 0;
    int pos_min = 0;
    int neg_count = 0;
    int pos_count = 0;
    for(int i = 0; i < lst.size(); i++) {
        if(lst[i] < 0 && neg_count == 0) {
            neg_max = lst[i];
            neg_count++;
        } else if(lst[i] < 0) {
            if(lst[i] > neg_max) {
                neg_max = lst[i];
            }
        }
        if(lst[i] > 0 && pos_count == 0) {
            pos_min = lst[i];
            pos_count++;
        } else if(lst[i] > 0) {
            if(lst[i] < pos_min) {
                pos_min = lst[i];
            }
        }
    }
    if(neg_count == 0 && pos_count == 0) {
        res[0] = 0;
        res[1] = 0;
    } else if(pos_count == 0) {
        res[0] = neg_max;
        res[1] = 0;
    } else if(neg_count == 0) {
        res[0] = 0;
        res[1] = pos_min;
    } else {
        res[0] = neg_max;
        res[1] = pos_min;
    }
    return res;
}

int main() {
    vector<int> lst = {2, 4, 1, 3, 5, 7};
    vector<int> res = largest_smallest_integers(lst);
    printf("%d %d", res[0], res[1]);
    return 0;
}



*/













































