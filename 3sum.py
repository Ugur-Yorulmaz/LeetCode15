# 15. 3Sum  Here is the two solution for Leetcode number 15
# Second solution is not accepted by LeetCode but works fine with PyCharm

# nums = [-1,0,1,2,-1,-4]
# nums = [-4,-9,-3,4,1,-4,1,-10,-9,2,9,8,1,-9,3,-7,-3,2,-9,-8,-1,-1,-7,-4]
nums=[-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
sNums=sorted(nums)
print(sNums)
tmp=None
res=[]
l=1
r=len(sNums)-1
for i in range(len(sNums)-2):
    print("i               :",i,"küme          :",tmp)
    print("sNums kümeye eşit mi",sNums[i]==tmp)
    if sNums[i] == tmp:
        continue
    else:
        tmp=sNums[i]
        l=i+1
        r=len(sNums)-1
    while l<r:
        # if r>l:
        # # l = i + 1
        # r = len(sNums) - 1

        print([sNums[i],sNums[l],sNums[r]])
        if sNums[i]+sNums[l]+sNums[r]==0:
            if [sNums[i],sNums[l],sNums[r]] not in res:
                print("Kümeye ekle",[sNums[i],sNums[l],sNums[r]])
                res.append([sNums[i],sNums[l],sNums[r]])
                r=r-1
            else:
                r=r-1
                # continue
        elif sNums[i]+sNums[l]+sNums[r]<0:
            l=l+1
        elif sNums[i]+sNums[l]+sNums[r]>0:
            r=r-1
print(res)


















import itertools
import time

# res=[]
# tic=time.time()
#
# liste=list(itertools.permutations(sNums,3))
# print(liste)
# print(len(liste))
# temp=[]
#
# for k in liste:
#     if k not in temp and sum(k)==0:
#         temp.append(sorted(list(k)))
# for l in temp:
#     if l not in res:
#         res.append(l)
# toc=time.time()
# print("süre",toc-tic)
# print(res)
# print(len(res))
#
#
# # Output: [[-1,-1,2],[-1,0,1]]
#
#
#
#
# # for i in sNums:
# #     num[i]=num.get(i,0)+1
# #     print(num)
# #
# # for j in range(len(num)):
# #
# # # a[i]=a.get(i,0)+1