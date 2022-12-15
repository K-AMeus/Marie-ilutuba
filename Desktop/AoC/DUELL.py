# f = open("kalorid.txt", "r")
# 
# 
# 
# 
# päkapiku_nr = 1
# suurim_kalor = 0
# praegune_kalor = 0
# 
# ls = []
# while True:
#     loe_rida = f.readline().strip()
#     if loe_rida == "STOP":
#         break
#     elif loe_rida == "":
#         if praegune_kalor > suurim_kalor:
#             suurim_kalor = praegune_kalor
#             print(päkapiku_nr)
#         ls += [praegune_kalor]
#         praegune_kalor = 0
#         päkapiku_nr += 1
#         continue
#     try:
#         praegune_kalor += int(loe_rida)
#     except:
#         continue
#     
# 
# kalorid_kokku = 0
# print(max(ls))
# print(ls.index(69836))
# for i in range(3):
#     kalorid_kokku += max(ls)
#     ls.pop(ls.index(max(ls)))
# print(kalorid_kokku)

#kivi = 1
#paber = 2
#käärid = 3
#viik = 3
#võit = 6
#kaotus = 0
#A = KIVI
#B = PABER
#C = KÄÄRID
#X = KIVI
#Y = PABER
#Z = KÄÄRID

#X - PEAD KAOTAMA
#Y - PEAD VIIKI MÄNGIMA
#Z - PEAD VÕITMA



# kokku = 0
# f = open("mäng.txt", "r")
# 
# for i in f:
#     i = i.strip().split(" ")
#     if i[0] == "B": #PABER
#         if i[1] == "X":
#             kokku += 1
#         elif i[1] == "Y":
#             kokku += 5
#         else:
#             kokku += 9
#     elif i[0] == "A": #kivi
#         if i[1] == "X":
#             kokku += 3
#         elif i[1] == "Y":
#             kokku += 4
#         else:
#             kokku += 8
#     else: #käärid
#         if i[1] == "X":
#             kokku += 2
#         elif i[1] == "Y":
#             kokku += 6
#         else:
#             kokku += 7
# print(kokku)

# import string
# f = open("asjad.txt","r")
# 
# 
# 
# ls = []
# while True:
#     esimene = f.readline().strip()
#     if esimene == "":
#         break
#     teine = f.readline().strip()
#     kolmas = f.readline().strip()
#     for i in esimene:
#         if i in teine:
#             if i in kolmas:
#                 ls += [i]
#                 break
#             
#                 
# print(ls)
# 
# väiketähed_järjend = []
# väiketähed = string.ascii_lowercase
# for i in väiketähed:
#     väiketähed_järjend += [i]
#     
# suurtähed_järjend = []
# suurtähed = string.ascii_uppercase
# for j in suurtähed:
#     suurtähed_järjend += [j]
#     

    
    
# tähed = []
# tähtsad_tähed = []
# for rida in f:
#     rida = rida.strip()
#     rea_pikkus = len(rida) #16
#     esimene = rida[0:int(rea_pikkus / 2)]
#     teine = rida[int(rea_pikkus / 2):]
#     for i in esimene:
#         tähed += [i]
#     for j in teine:
#         if j in tähed:
#             tähtsad_tähed += [j]
#             break
#     tähed = []
# 
# 
# 
# kokku = 0
# for i in ls:
#     if i in väiketähed:
#         kokku += väiketähed.index(i) + 1
#     else:
#         kokku += suurtähed.index(i) + 27
# # print(string.ascii_uppercase)
# print(kokku)
# # print(tähtsad_tähed)

# 5 ja 10
# 4 ja 7

f = open("id.txt", "r")

kokku = 0
ls = []
for rida in f:
    rida = rida.strip()
    esimene = rida.split(",")[0]
    teine = rida.split(",")[1]
    esimene_split2 = esimene.split("-")
    teine_split2 = teine.split("-")
    for i in range(int(esimene_split2[0]), int(esimene_split2[1]) + 1):
        ls += [i]
    for j in range(int(teine_split2[0]), int(teine_split2[1]) + 1):
        if j not in ls:
            kokku -= 1
            break
    ls = []
        
    for j in range(int(teine_split2[0]), int(teine_split2[1]) + 1):
        ls += [j]
    for i in range(int(esimene_split2[0]), int(esimene_split2[1]) + 1):
        if i not in ls:
            kokku -= 1
            break


    kokku += 1
    ls = []
    
    

print(kokku)
        



            
            
                    
        
            






    
