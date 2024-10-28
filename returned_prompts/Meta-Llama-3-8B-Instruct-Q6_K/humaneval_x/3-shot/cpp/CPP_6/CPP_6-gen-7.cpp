    vector<int> levels;
    int level=0;
    int i;
    for (i=0;i<paren_string.length();i++)
    {
        char chr=paren_string[i];
        if (chr=='(')
        {
            level+=1;
        }
        if (chr==')')
        {
            level-=1;
        }
        levels.push_back(level);
    }
    return levels;
}
} // namespace std;

int main() {
    printf("%d\n", has_close_elements({1.0, 2.0, 3.0}, 0.5));
    printf("%d\n", has_close_elements({1.0, 2.8, 3.0, 4.0, 5.0, 2.0}, 0.3));
    printf("%s\n", separate_paren_groups("( ) (( )) (( )( ))")[0].c_str());
    printf("%s\n", separate_paren_groups("( ) (( )) (( )( ))")[1].c_str());
    printf("%s\n", separate_paren_groups("( ) (( )) (( )( ))")[2].c_str());
    printf("%f\n", truncate_number(3.5));
    printf("%d\n", parse_nested_parens("(()()) ((())) () ((())()())")[0]);
    printf("%d\n", parse_nested_parens("(()()) ((())) () ((())()())")[1]);
    printf("%d\n", parse_nested_parens("(()()) ((())) () ((())()())")[2]);
    printf("%d\n", parse_nested_parens("(()()) ((())) () ((())()())")[3]);
    return 0;
} // int main() {
// }
} // namespace std;
} // namespace std;
} // namespace std; // end of namespace std;
} // end of namespace std;
} // end of namespace std;
} // end of namespace std; // end of namespace std;
} // end of namespace std;
} // end of namespace std; // end of namespace std;
} // end of namespace std; // end of namespace std;
} // end of namespace std; // end of namespace std;
} // end of namespace std; // end of namespace std;
} // end of namespace std; // end of namespace std;
} // end of namespace std; // end of namespace std;
} // end of namespace std; // end of namespace std;
} // end of namespace std; //