    for (int i = 1; i <= 9; i++) {
        scanf("%d", &TL[i]);
        map_key[i] = TL[i];
    }

    printf("Press 0 to exit\n");
    while (true) {
        scanf("%d", &N);
        if (N == 0) {
            break;
        }

        printf("Enter a word: ");
        scanf("%s", word);

        int length = strlen(word);
        int code[length];

        for (int i = 0; i < length; i++) {
            for (int j = 1; j <= 9; j++) {
                if (key[j][word[i] - 'a'] == word[i]) {
                    code[i] = j;
                    break;
                }
            }
        }

        printf("Code: ");
        for (int i = 0; i < length; i++) {
            printf("%d ", code[i]);
        }
        printf("\n");
    }

