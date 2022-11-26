n=int(input())

def latex(n,counter):
    counter=counter-1
    if(counter==0):
        return 1
    elif(counter==1 ):
        return str(n)+"+"+"\\"+"frac"+"{"+str(2*n)+"}"+"{"+str(2*n+1)+"}"
    else:
        return str(n)+"+"+"\\"+"frac"+"{"+str(latex(2*n,counter))+"}"+"{"+str(latex(2*n+1,counter))+"}"
    
latex(1,n)
