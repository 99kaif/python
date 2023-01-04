def newgame():
    que_num=1
    for key in que:
        print(key)
        print(option[que_num-1])
        que_num+=1
        a=str(input("ans (A,B,C,D)::")).upper()
        ans.append(a)
    result()
def result():
    score=0
    i=0
    for key in que:
        if que[key]==ans[i]:
            score+=1
        i+=1
    print("-------------------------------------")
    print(score)
que = {
    1 : 'A',
    2 : 'B',
    3 : 'C'
}
ans=[]
option = [['A','B','C','D'],
          ['A','B','C','D'],
          ['A','B','C','D']]
newgame()