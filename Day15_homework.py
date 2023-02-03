friends=[['피카츄',200],['라이츄',150],['파이리',90],['꼬부기',30],['이상해씨',15]]
def add_data():
    friend = input("추가할 포켓몬 -->")
    friend_2=int(input("체력 -->"))
    return [friend,friend_2]

def linear_add(*args):
    for i in range(0,len(friends)):
        if friends[i+1][1]<args[0][1]< friends[i][1]:
            friends.insert(i+1,args[0])
            break
        elif friends[i][1] == args[0][1]:
            friends.insert(i,args[0])
            break
        elif friends[i][1]<args[0][1]:
            friends.insert(i, args[0])
            break

a=add_data()
linear_add(a)
print(friends)


