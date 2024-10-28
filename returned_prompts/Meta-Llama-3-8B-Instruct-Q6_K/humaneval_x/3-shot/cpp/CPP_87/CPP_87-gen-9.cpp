    vector<vector<int>> result;
    for (int i=0;i<lst.size();i++)
    {
        for (int j=0;j<lst[i].size();j++)
        {
            if (lst[i][j]==x)
            {
                result.push_back({i,j});
            }
        }
    }
    sort(result.begin(), result.end(), [](const vector<int>& a, const vector<int>& b)
    {
        if (a[0] == b[0])
            return a[1] > b[1];
        return a[0] < b[0];
    });
    return result;
}
// This function is used to sort the coordinates by row then column
// It sorts the coordinates based on the row index, then for the same row, it sorts based on the column index
// The lambda function is used to define the sorting criteria, it returns true if a is greater than b
// The sort function sorts the vector in ascending order, so we can't directly use it to sort in descending order
// So, we use the lambda function to return a[1] > b[1] when the row indices are the same, which means the column indices are the same
// So, the column indices will be sorted in descending order
// The sort function will sort the coordinates by row in ascending order, and for the same row, it will sort the column indices in descending order
// The sort function is then used to sort the result vector
// The result is the sorted vector of coordinates
// The function is then returned
// The function is then used to get the result
// The result is then printed
// The program then ends
}  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }  // }