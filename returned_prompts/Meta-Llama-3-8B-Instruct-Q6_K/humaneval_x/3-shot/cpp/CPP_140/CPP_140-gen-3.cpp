    string result;
    for (int i=0;i<text.length();i++)
    {
        if (text[i]==' ')
        {
            if (result.length()>0 && result[result.length()-1]==' ')
            {
                if (result.length()>1 && result[result.length()-2]==' ')
                {
                    result=result.substr(0,result.length()-1);
                    result+="-";
                }
                else
                    result+="-";
            }
            else
                result+="_";
        }
        else
            result+=text[i];
    }
    return result;
}  // This code is not working properly. It's not checking for consecutive spaces correctly.  //


