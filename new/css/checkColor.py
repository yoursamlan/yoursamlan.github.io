f = open("style.css", "r")
x = f.readlines()
cpal = []
cpal0 = []
cpal1 = []
for i in range(0,len(x)):
    line = x[i]
    line = line.replace("\n","")
    if "#" in line:
        l = line.split(" ")
        for w in l:
            if "#" in w and "{" not in w and "," not in w:
                w = w.replace("background-color:","")
                w = w.replace("background:","")
                w = w.replace("color:","")
                w = w.replace(";","")
                if len(w)==4:
                    if w not in cpal1:
                        cpal1.append(w)
                        print(i,w)
                    w = '#{}'.format(''.join(2 * c for c in w.lstrip('#')))
                if w not in cpal:
                    cpal.append(w)
                    cpal0.append(int(w.replace("#",""), 16))  


cpal.sort()
cpal0.sort()

print(":root {")
for i in range(0,len(cpal)):
    print("\t--col"+str(i)+": "+cpal[i]+";")
print("}")  
print(len(cpal))
