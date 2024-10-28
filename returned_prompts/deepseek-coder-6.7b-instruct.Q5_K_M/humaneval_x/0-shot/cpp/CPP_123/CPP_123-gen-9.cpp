    vector<int> odd_nums;
    while(n != 1){
        if(n % 2 != 0)
            odd_nums.push_back(n);
        n = n % 2 ? n*3 + 1 : n / 2;
    }
    odd_nums.push_back(1);
    sort(odd_nums.begin(), odd_nums.end());
    return odd_nums;
}

int main(){
    vector<int> res = get_odd_collatz(5);
    for(int i=0; i<res.size(); i++)
        printf("%d ", res[i]);
    return 0;
}

This program creates the vector of odd numbers in the Collatz sequence for a given number n, sorts this vector and then returns it.

The while loop in function get_odd_collatz(int n) calculates the Collatz sequence for the given number n. If the current number is odd, it's added to the vector odd_nums. The current number is then set to the next number in the sequence. This process repeats until the number is 1. The final number 1 is always added to the vector.

Finally, the vector of odd numbers is sorted in increasing order using the sort() function and then returned.
*/
//E:
//}
//};
//E:
//}
//};
//E:
//}
//};
//E:
//}
//};
//E:
//}
//};
//E:
//}
//};
//E:
//}
//};
//E:
//}
//};
//E:
//}
//};
//E:
//}
//};
//E:
//}
//};
//E:
//}
//};
//E:
//}
//};
//E:
//}
//};
//E:
//}
//};
//E:
//}
//};
//E:
//}
//};
//E:
//}
//};
//E:
//}
//};
//E:
//}
//};
//E