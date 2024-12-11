class Province:
    def __init__(self, pcode="", pname="", type_soilder=""):
        self.pcode = pcode
        self.pname = pname
        self.type_soilder = type_soilder
    
def R_Province(RP):
    fin = open(RP,'r')

    PMem = []
    l = 1
    with fin:
        for PRec in fin:
            pcode, pname, type_soilder = PRec.split()
            if l:
                PMem.append(Province(pcode, pname, type_soilder))
            l += 1
    
    return PMem

def W_Province(PMem, WP):
    fout = open(WP,'w')

    with fout:
        for PRec in PMem:
            fout.write(f'{PMem}\n')
    
    return

