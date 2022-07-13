def schedule(h1, h2, h3, h4):
    if (h1 <= h3 and h2 >= h3) or (h1 <= h4 and h2 >= h4) or (h1 >= h3 and h2 <= h4):
        return True
    else:
        return False

s1 = "RENE=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00"
s2 = "ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00"
x1 = s1.split("=")
x2 = x1[1].split(",")
y1 = s2.split("=")
y2 = y1[1].split(",")

cont = 0
for i in range(0, len(x2)):
    for j in range(0, len(y2)):
        st1 = x2[i]
        st2 = y2[j]
        if st1[0:2] == st2[0:2]:
            if schedule(st1[2:7], st1[8:13], st2[2:7], st2[8:13]) == True:
                cont+=1
print(x1[0] + "-" + y1[0] + ":" + str(cont))




