def pochodna_mniejsza(x,y,a,b):
    return float(y[b]-y[a]) / float(x[b]-x[a]) 

def mnozenie_nawiasow(pierwiastki):
    wielomian = [1]
    
    for r in pierwiastki:
        nowy_nawias = [-r, 1]
        wielomian = mnoz_wielomiany(wielomian, nowy_nawias)

    return wielomian[::-1]  

def mnoz_wielomiany(w1, w2):
    wynik = [0] * (len(w1) + len(w2) - 1)
    for i in range(len(w1)):
        for j in range(len(w2)):
            wynik[i + j] += w1[i] * w2[j]
    return wynik


    


def pochodna_wieksza(*args):
    tablica = args[2]
    x = args[0]
    y = args[1]

    if (len(tablica)==2):
        a = tablica[0]
        b = tablica[1]

        return float(y[b]-y[a]) / float(x[b]-x[a])  
    
    else:
        tab1 = []
        for i in range(1,len(tablica)):
            tab1.append(tablica[i])

        tab2 = []
        for i in range(0,len(tablica)-1):
            tab2.append(tablica[i])

        mianownik = x[-1] - x[0]
        licznik =  pochodna_wieksza(x,y,tab1) - pochodna_wieksza(x,y,tab2)
        return float(licznik) / float(mianownik)
    


x = [-2,1,4]
y = [5,3,7]

'''
print(pochodna_wieksza(x,y,[0,1]))
print(pochodna_wieksza(x,y,[1,2]))
print(pochodna_wieksza(x,y,[0,1,2]))
'''

def newton(x,y):
    n = len(x)
    #print(n)
    a = [0] * n
    a[0] = y[0]

    for k in range(1,n):
        tab = []
        for j in range(k+1):
            tab.append(j)
        a[k] = pochodna_wieksza(x,y,tab)


    tab = [0] * n

    for i in range(n-1,-1,-1):
        if i >= 2:
            miejsca_zerowe = [0] * (i)
            for j in range(0, i):
                miejsca_zerowe[j] = x[j]

            z = mnozenie_nawiasow(miejsca_zerowe)
            h = len(z) - 1
            for k in range(len(z)):
                tab[h] += float(z[k]*a[i])
                h -= 1
        
        if i==1:
            wolne = float(-a[1]*x[0]) 
            tab[0] += float(wolne)
            tab[1] += float(a[1])

        if i==0:
            tab[0] += float(a[0])

            
            
    return tab
        
   
            
            

#print(mnozenie_nawiasow([2, 3]))        
#print(mnozenie_nawiasow([1, 2, 3])) 

print(newton(x,y))

x= [-23,45,67,89,90,-44,-23,0,1,2,3]
y= [5,3,7,8,9,0,1,2,3,4,5]

print(newton(x,y))