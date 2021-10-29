def addsv(a):
    sv = {"Name":" ", "ID":""}
    print("Nhap ID Sinh Vien: ")
    id = input()
    while(True):
        if(Findsv(a,id) != False):
            print("ID da co trong he thong, nhap lai")
            id = input()
        else: break
    sv["ID"] = id
    print("Nhap Ten sv:")
    sv["Name"] = input()
    a.append(sv)

def Findsv(a,n):
    for i in range(0,len(a)):
        if(a[i]['ID'] == n): return[i, a[i]]
    return False
    

a = []
while True:
    try:
        n = int(input())
        break
    except:
        print("Nhap so nguyen: ")

for i in range(0,n+1):  
    addsv(a)

print("")