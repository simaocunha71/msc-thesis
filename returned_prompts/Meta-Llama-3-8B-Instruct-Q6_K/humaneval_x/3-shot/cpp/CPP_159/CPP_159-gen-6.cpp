    int eaten=number+min(need,remaining);
    int left=remaining-eaten+number;
    return {eaten,left};
}