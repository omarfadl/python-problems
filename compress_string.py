word="aabbbbcdffll"
count=1
result=[]
i=0

while i<len(word)-1:
    if word[i]==word[i+1]:
        count+=1
    else:
        result.append(str(count)+word[i] if count>1 else word[i])
        count=1
    i+=1

# Append the last character correctly
result.append(str(count) + word[i] if count > 1 else word[i])


    
print("".join(result))
    

    
        
