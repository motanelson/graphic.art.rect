#change next 2 lines
winas="c:\\MinGW\\bin\\as.exe"
winobj="c:\\MinGW\\bin\\objdump.exe"
import os
def spt(s):
    r=s.split(" ")
    rr=[]
    for a in range(len(r)):
        
        if r[a].strip()!= "":
            rr.append(r[a])
    return rr
print("give me the .o object file name ? ")
a=input().strip()
os.system(winobj+" -x "+a+" > out.txt")
f1=open(a,"rb")
btxt=f1.read()
f1.close()
ta=0
tb=0
f1=open("out.txt","r")
txt=f1.read()
f1.close()
txts=txt.split("\n")
t=False
print("\033c")
t=False
for a in txts:
    aa=spt(a)
    if len(aa)>0:
        if t:
            if len(aa)>1:
                
                if aa[1].strip()==".text":
                    if len(aa)>5:
                           
                        ta=int(aa[5],16)
                           
                        tb=int(aa[2],16)
                        tb=tb+ta

        if a.strip()=="SYMBOL TABLE:":
             t=False
        if a.strip()=="Sections:":
             t=True
t=False
for a in txts:
    aa=spt(a)
    if len(aa)>0:
        if t:
            if len(aa)>8:
                print(aa[9])
        if a.strip()=="SYMBOL TABLE:":
             t=True
print("give me the .o symbol name to display? ")
b=input().strip()
t=False
for a in txts:
    aa=spt(a)
    if len(aa)>0:
        if t:
            if len(aa)>8:
                if aa[9].strip()==b:
                    td=int(aa[8],16)
                
                    tb=ta+td
        if a.strip()=="SYMBOL TABLE:":
             t=True
tc=ta+td
print("\033c")
while 1:
   if btxt[tc]==0:
       break
   if tb>tc:
      break
   print(chr(btxt[tc]),end="")
   
   tc=tc+1
print("")
   