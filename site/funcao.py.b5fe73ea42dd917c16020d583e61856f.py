      
def RollingHash(text, pattern):
    indexes = []
        
    m = len(text)
    n = len(pattern)

    text_value =0
    pattern_value = 0

    for i in range(len(pattern)):
        pattern_value+= ord(pattern[i])
        text_value += ord(text[i])
    if (text_value==pattern_value):
        indexes.append(i) 
    for i in range(n,len(text)):
        text_value = text_value + ord(text[i]) - ord(text[i-3])
        if (text_value==pattern_value):
            indexes.append(i)
    return indexes;

#print(RollingHash("O MARCELO HASHIMOTO ESTÁ INDO NA PADARIA PDCM, ALGÚEM QUER ALGO?", "HASH"))


def stringMatching(text, pattern):
    indexes = []
    for i in range(len(text)):
        if text[i:(len(pattern)+i)] == pattern:
            indexes.append(i)
    return indexes

#print(stringMatching("jdiofiajjajajanbuf", "ajjajaja"))

def stringSearchHash(text, pattern):
    indexes = []
    
    pattern_value= 0
    for character in pattern:
        pattern_value += ord(character)
    for i in range(len(text)):
        j=i
        text_value = 0
        if (i+len(pattern)>len(text)):
            break
        while(j<i+len(pattern)):
            text_value+=ord(text[j])
            j+=1
        if (text_value==pattern_value):
            indexes.append(i)
    
    return indexes

    print(stringSearchHash("sdaqwertyuiosad","qwert"))