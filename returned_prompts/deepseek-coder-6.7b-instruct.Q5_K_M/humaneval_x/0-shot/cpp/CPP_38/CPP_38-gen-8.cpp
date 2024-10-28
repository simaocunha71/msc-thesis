    int l=s.length();
    int num=(l+2)/3;
    string x,output;
    int i;
    for  (i=0;i*3<l;i++)
     {
         //cycle elements in each group. Unless group has fewer elements than 3.
         x=s.substr(i*3,3);
         if  (x.length()==3) x=x[2]+x.substr(0,2);
         output=output+x;
     }
    return output;
}

int main(){
    string s="Hello World";
    string encoded_s=encode_cyclic(s);
    string decoded_s=decode_cyclic(encoded_s);
    printf("Original String: %s\nEncoded String: %s\nDecoded String: %s\n",s.c_str(),encoded_s.c_str(),decoded_s.c_str());
    return 0;
}

```



## R

Here is a simple solution in R:

```R
encode_cyclic <- function(s) {
  len <- nchar(s)
  num <- ceiling(len / 3)
  str <- ""
  for (i in 0:(num-1)) {
    sub_str <- strsplit(s[((i*3)+1):min((i+1)*3, len)], "")[[1]]
    if (length(sub_str) < 3) {
      str <- paste0(str, sub_str)
    } else {
      str <- paste0(str, sub_str[2], sub_str[3], sub_str[1])
    }
  }
  return(str)
}

decode_cyclic <- function(s) {
  len <- nchar(s)
  num <- ceiling(len / 3)
  str <- ""
  for (i in 0:(num-1)) {
    sub_str <- strsplit(s[((i*3)+1):min((i+1)*3,