    int matrix[n][n];
    int count = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            for (int k = j + 1; k < n; k++)
            {
                if(matrix[i][j] + matrix[j][k] + matrix[k][i] % 3 == 0){
                    count++;
                }
            }
        }
    }
    return count;
}
int main()
{
    int n = 5;
    printf("%d", get_matrix_triples(n));
    return 0;
}

