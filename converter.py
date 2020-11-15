assembly_code = open("InlineConvAndMaxPool.txt", "r")
#Read assembly code
assembly_text = assembly_code.read()
assembly_list = assembly_text.split('\n')
assembly_code.close()
#print (assembly_list)
instruction_list=[]
error_lst=[]
asm="asm(\""
count=0
for i in range(len(assembly_list)):
    k=assembly_list[i]
    if "//" in k:
        #print (k)
        ll=False
        for j in range(len(k)):
            #print (k[j])
            if k[j]!=" " and k[j]!="/":
                ll=True
            if k[j]=="/":
                k=k[0:j]
                break
    if ";" in k:
        asm=asm+" "+k
        count+=1
    else:
        if len(k)>2:
            k="Expected ;  < "+k+" > line no "+str(i)+" "
            error_lst.append(k)

asm=asm+"\");"
print (asm)
print("\n\n")
print("No of Instructions :",count)
print ("No of errors ",len(error_lst))
if len(error_lst)>0:
    print ("Errors -> ")
for i in error_lst:
    print (i)
