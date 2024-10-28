    vector<vector<int>> coordinates;
    for (int i=0;i<lst.size();i++)
    for (int j=0;j<lst[i].size();j++)
    {
        if (lst[i][j]==x)
        {
            vector<int> coordinate;
            coordinate.push_back(i);
            coordinate.push_back(j);
            coordinates.push_back(coordinate);
        }
    }

    for (int i=0;i<coordinates.size();i++)
    for (int j=0;j<coordinates.size();j++)
    {
        if (coordinates[i][0]<coordinates[j][0])
        {
            vector<int> temp=coordinates[i];
            coordinates[i]=coordinates[j];
            coordinates[j]=temp;
        }
    }

    for (int i=0;i<coordinates.size();i++)
    for (int j=0;j<coordinates.size();j++)
    {
        if (coordinates[i][0]==coordinates[j][0])
        {
            if (coordinates[i][1]>coordinates[j][1])
            {
                vector<int> temp=coordinates[i];
                coordinates[i]=coordinates[j];
                coordinates[j]=temp;
            }
        }
    }

    return coordinates;
}

