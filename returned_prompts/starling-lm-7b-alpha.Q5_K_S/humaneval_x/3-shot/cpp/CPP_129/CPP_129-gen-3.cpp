    int i,j,n=grid.size();
    vector<vector<pair<int,int>>> directions={{1,0},{0,1},{-1,0},{0,-1}};
    vector<vector<int>> visited(n,vector<int>(n,0));
    vector<vector<int>> q(n*n,vector<int>(k,0));
    vector<vector<int>> temp(n,vector<int>(n,0));
    vector<pair<int,int>> q_index(n*n,make_pair(0,0));
    int l=0;
    int r=0;
    int next_i,next_j;
    int temp_i,temp_j;
    int temp_k;
    vector<int> answer(k);
    int index=0;
    answer[0]=grid[0][0];
    visited[0][0]=1;
    q_index[index]=make_pair(0,0);
    r+=1;
    while (l<r){
        temp_i=q_index[l].first;
        temp_j=q_index[l].second;
        temp_k=q[temp_i][temp_j];
        if (temp_k==k-1)
        {
            index+=1;
            answer[temp_k]=grid[temp_i][temp_j];
            l+=1;
        }
        else
        {
        for (i=0;i<4;i++){
            next_i=temp_i+directions[i][0];
            next_j=temp_j+directions[i][1];
            if (next_i>=0 && next_j>=0 && next_i<n && next_j<n && visited[next_i][next_j]==0 && temp_k+1<k){
                temp[next_i][next_j]=grid[next_i][next_j];
                q[next_i][next_j]=temp_k+1;
                visited[next_i][next_j]=1;
                q_index[r]=make_pair(next_i