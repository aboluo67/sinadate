# a = [1,2,3,4,5,6,7,8,9,10,11]
# step = 3
# b = [a[i:i+step] for i in range(0,len(a),step)]
# print(b)

a=[1,2,3,33,2,2,3,4,5,6,7,8,89,9,]
for x in range(0,len(a),3):
    # str1=''.join(str(i) for i in a[x:x+3])
    str1= (str(i) for i in a[x:x+3])
    print(str1)