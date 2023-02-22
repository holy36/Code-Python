# a=type(b)  gan a bang kieu gia tri cua bien b
# Khai bao thu vien :
from tenthuvien import* , co * dee import het tat ca phuong thuc trong thu vien vao
from tenthuvien import phuongthuc , import 1 phuong thuc bat ky trong thu vien
import tenthuvien , muon su dung 1 phuong thuc trong thu vien thi phai tenthuvien.phuongthuc
# Thu vien decimal
Binh thuong python se lay 15 chu so sau phan thap phan cua 1 so 
getcontext().prec=k   lay k chu so sau phan thap phan
Rei : Decimal(k), Decimal(a)/b ...
# Thu vien fractions
Fraction(a,b) , tao mot phan so a/b
# complex(a,b) , tao so phuc a+bi
# Thu vien math
trunc(x) tra ve so nguyen
floor(x) lam tron xuong
ceil(x) lam tron len
fabs(x) tri tuyet doi
sqrt(x) can
gcd(x,y,z) uoc chung lon nhat
lcm(x,y,z) boi chung nho nhat
# 1 so phuong thuc chuoi
b=a.capitalize() gan b bang 1 chuoi co chu cai dau tien cua a viet hoa
a.upper() viet hoa het chu cai trong chuoi
a.lower() doi het chu hoa thanh chu thuong
a.swapcase() doi chu hoa thanh chu thuong , chu thuong thanh chu hoa
a.title() viet hoa het chu cai dau tien
a.center(k,'xy') can giua chuoi a voi tong chieu dai k , can bang ky tu xy
a.rjust() can phai , a.ljust() can trai
a.join() gop 1 mang string voi ky tu giua la a
Rei : a.join(["2","5","t"]) -> 2a5at
a.replace("a","b",k) thay ky tu a vao b , thay k lan
a.strip() , xoa ky tu o dau 2 ben
a.lstrip() xoa ben trai , a.rstrip() xoa ben phai
a.split("k") cu co k la cat thanh chuoi moi
a.rsplit("") cat tu ben phai qua
a.partition("") cat chuoi thanh 3 chuoi nho  , a.rpartiton
a.count("k",a,b) dem ky tu k tu theo thu tu a den b
a.startswith("k") kiem tra chuoi co bat dau bang k khong , a.endwith
a.find("k"), a.rfind("")  tim ky tu
a.isupper() , a.islower() , a.isdigit() , a.isspace() 
# a[,,-1] dao nguoc chuoi bat ky
# List
a=[i for i in range(x,y)] tao mot list tu x->y-1
Rei : a=[[n,n+1,n+2] for n in range(14)]
b=k in a kiem tra xem b co o trong a khong 
a.copy() gan gia tr list a cho list b
a.clear() xoa list
a.append(k) them k vao cuoi list a
a.insert(x,y) them y vao list tai vi tri x
b=a.pop(k)  bo phan tu thu k cua list a , gan phan tu do cho b
a.remove(k) xoa phan tu co gia tri k , xoa theo thu tu trai sang phai
a.reverse() dao nguoc list
a.sort() sap xep nho den lon
a.sort(reverse=True) sap xep lon den nho 
len(a)lay chieu dai cua list a
# Dict
myinfo =  {"Name": "Tran", "Age": 37, "Address" : "Vietnam"  } tao 1 dict
myinfo['Name']=x gan gia tri key Name bang x 
del myinfo['Name'] xoa key Name
m=myinfo.get('Name','ec o ec')  lay key Name tu dict va gan bang 'ec o ec' 
myinfo.clear()  clear dict 
k=('a','b')-> h=dict.fromkeys(k)  tao 1 dict gom 2 key la a va b deu bang none
m=myinfo.items()
myinfo.update() 
# File
k=open('ten file') mo file
h=k.read(n) doc n ky tu trong file k
k.close() dong file k
h=k.readlines() doc tung dong , moi dong la 1 phan tu cua 1 list
hoac co the dung h=list(k) , tupple cung duoc =))
h=k.write('chuoi')
k=open('ten file',mode='w')   h=k.write('chuoi')
k.seek(n) dua con tro toi ky tu so n 
