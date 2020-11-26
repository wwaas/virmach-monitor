import os
import re

# os.system('grep "^IP"  virmach.txt >ip')
# os.system('grep "^价格"  virmach.txt >price')
# os.system('grep "^CPU"  virmach.txt >cpu')
# os.system('grep "^硬盘"  virmach.txt >disk')
# os.system('grep "^流量"  virmach.txt >band')
# os.system('grep "^内存"  virmach.txt >mem')
# os.system('grep "^位置"  virmach.txt >locate')
#os.system('grep "^构架"  virmach.txt >kvm')

pricep = r"(\d+.\d+)"
locatep = r"(.+)"
#kvmp = r"构架: (.+)"
diskp = r"(\d+)"
cpup = r"\d+"
ipp = r"\d+"
memp = r"\d+"
bandp = r"\d+"

price = re.findall(pricep, open("price").read())
locate = re.findall(locatep, open("locate").read())
#kvm = re.findall(kvmp,open("kvm").read())
disk = re.findall(diskp, open("disk").read())
cpu = re.findall(cpup, open("cpu").read())
ip = re.findall(ipp, open("ip").read())
mem = re.findall(memp, open("mem").read())
band = re.findall(bandp, open("band").read())
print(len(price))
print(len(locate))
print(len(disk))
print(len(cpu))
print(len(ip))
print(len(mem))
print(len(band))


fw = open("hei2019.csv", 'w')
fw.write("price\tlocate\tdisk\tcpu\tip\tmemory\tband")
# fw.write("price\tlocate\tkvm\tdisk\tcpu\tip\tmemory\tband")
for i in range(len(price)):
    fw.write("\n"+"\t".join([price[i], locate[i],
                             disk[i], cpu[i], ip[i], mem[i], band[i]]))

fw.close()
