#Enter Python code here and hit the Run button.
LINE_LENGTH=40
lines=list()
line=[]
line_id=0;
paragraph="Peak: Secrets from the New Science of Expertise is a 2016 science book by psychologist K. Anders Ericsson and science writer Robert Pool. The book summarizes the findings of Ericsson's 30-year research into the general nature and acquisition of expertise"

words=paragraph.split(" ")
## print (words)
def get_line_length(line):
    sum=0
    for word in line:
        sum+=len(word)
    return (sum)

for word in words:
    if (get_line_length(line)+len(word)) < LINE_LENGTH-len(line):
        line.append(word)
        #print(f"{word} ")
        #print(line)
    else:    
        lines.append(line)
        line=[]
        
for print_line in lines:
    print(f'{get_line_length(print_line)}|{" ".join(print_line)}')
