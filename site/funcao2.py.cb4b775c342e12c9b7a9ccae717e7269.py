def rabinKarp(text, pattern):
    indexes = []

    n = len(pattern)
    m = len(text)

    pattern_value= 0
    text_value = 0
    r = 256**(n-1)
    for i in range(n):
        pattern_value +=  ord(pattern[i]) * r
        text_value +=  ord(text[i]) * r
        r/=256
    if (text_value==pattern_value):
        indexes.append(i-(n-1))   
    for i in range(n,len(text)):
        text_value = (text_value  - ord(text[i-n]) * 256**(n-1) )*256 + ord(text[i])

        if (text_value==pattern_value):
            indexes.append(i-(n-1))  
    
    return indexes
    
