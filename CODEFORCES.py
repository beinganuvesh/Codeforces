#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install jupyterthemes


# In[5]:


sudo -H python3 -m pip install jupyterthemes


# In[ ]:


#PYTHON-2
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(Unique(arr))


# In[ ]:


#PYTHON-3
t=int(input())
for _ in range(t):
    n=int(input())
    arr=[int(i) for i in input().split()]
    print(Unique(arr))


# In[ ]:





# In[ ]:





# In[ ]:


def Square(a, b):
    a=sorted(a)
    b=sorted(b)
    if a[-1]==b[-1]:
        return a[0]+b[0]==a[-1]


# In[ ]:


a=[2,3]
b=[3,1]
Square(a,b)


# In[ ]:





# In[ ]:





# In[ ]:


def Strange(n):
    s=str(n)
    k=len(s)
    return k


# In[ ]:


Strange(37)


# In[ ]:





# In[ ]:


def Unique(arr):
    freq_dic={}
    index_dic={}
    for i, val in enumerate(arr):
        freq_dic[val]=freq_dic.get(val,0)+1
        index_dic[val]=i
        
    ans=sys.maxsize
    for i in index_dic:
        if freq_dic[i]==1:
            ans=min(ans, i)
            index=index_dic[ans]
    if ans==sys.maxsize:
        return -1
    else:
        return index+1
    


# In[ ]:


Unique([2,1,3])


# In[ ]:





# In[ ]:


def SpecialPermutations(n):
    for i in range(n):
        print((i+1)%n+1, end=" ")


# In[ ]:


SpecialPermutations(2)


# In[ ]:





# In[ ]:


def Trains(hor, vert):
    c,d=0,{}
    for i in hor:
        d[i]=True
    for i in vert:
        if i in d:
            c+=1
    return c


# In[ ]:





# In[ ]:





# In[ ]:


def RBS(s):
    o,c="",""
    l1,l2=[],[]
    count=0
    for ch in s:
        if ch=='(' or ch==')':
            o=o+ch
        elif ch=='[' or ch==']':
            c=c+ch
            
    for ch in o:
        if ch=='(':
            l1.append(ch)
        else:
            if len(l1)==0:
                continue
            if l1[-1]=='(':
                count+=1
                l1.pop(-1)
    for ch in c:
        if ch=='[':
            l2.append(ch)
        else:
            if len(l2)==0:
                continue
            if l2[-1]=='[':
                count+=1
                l2.pop(-1)
    return count


# In[ ]:


s='())('
RBS(s)


# In[ ]:





# In[ ]:





# In[ ]:


import sys
def ROBOT(x, y):
    if x==y:
        return x+y
    else:
        return 2*max(x,y)-1


# In[ ]:


ROBOT(7, 1)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


s='1111'
Subsequences(s, 2, 3)


# In[ ]:





# In[ ]:





# In[ ]:


#Recursion!
import sys    
def Reduce_Memo(n, dp):
    x,y=sys.maxsize,sys.maxsize
    #Base Case!
    if n==1 or n==2 or n==3:
        return n-1
        
    for i in range(n-1, 1, -1):
        if n%i==0:
            if dp[n//i]==-1:
                x=Reduce_Memo(n//i, dp)
            else:
                x=dp[n//i]
            break
            
    if dp[n-1]==-1:
        y=Reduce_Memo(n-1, dp)
    else:
        y=dp[n-1]
    
    return min(y+1,x+1)
    


# In[ ]:


def Reduce(n):
    if n==1 or n==2 or n==3:
        return n-1
    elif n%2==0:
        return 2
    else:
        return 3


# In[ ]:


Reduce(500)


# In[ ]:





# In[ ]:





# In[ ]:


def Arrangement(n, a, b, x):
    a=sorted(a)
    b=sorted(b, reverse=True)
    for i in range(n):
        if a[i]+b[i]>x:
            return False
    return True


# In[ ]:





# In[ ]:





# In[ ]:


def Possible(n):
    for k in range(2, n):
        val=(2**k)-1
        if n%val==0:
            return n//val


# In[ ]:


Possible(999999999)


# In[ ]:





# In[ ]:





# In[ ]:


def Valerii_Time(n, b):
    arr=[]
    for i in range(n):
        arr[i]=2**b[i]
        
    csum=arr[-1]
    for i in range(n-2, -1, -1):
        if arr[i]==csum:
            return True
        csum+=arr[i]
    return False


# In[ ]:


def Valerii(n, b):
    d={}
    for i in b:
        d[i]=d.get(i,0)+1
    for i in d:
        if d[i]>1:
            return True
    return False


# In[ ]:


b=[4, 3, 0, 1, 2, 0]
c=[2,5]
Valerii(len(c), c)


# In[ ]:





# In[ ]:





# In[ ]:


def PolyCarp(n):
    ans=0
    b=0
    for length in range(1, 9):
        b=(b*10+1)
        for m in range(1, 10):
            if (b*m<=n):
                ans+=1
    return ans


# In[ ]:


PolyCarp(33)


# In[ ]:





# In[ ]:





# In[ ]:


import sys
def Sum(arr):
    s=0
    mini=sys.maxsize
    p,n,z=0,0,0
    
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            s+=abs(arr[i][j])
            mini=min(abs(arr[i][j]), mini)
            if arr[i][j]==0:
                z+=1
            elif arr[i][j]<0:
                n+=1
            else:
                p+=1
    if z==1:
        return s
    elif n%2==0:
        return s
    elif n%2==1:
        return s-(2*mini)


# In[ ]:


arr=[[-1, 1], [1, 1]]
Sum(arr)


# In[ ]:





# In[ ]:





# In[ ]:


def Barrel(n, arr, k):
    arr=sorted(arr, reverse=True)
    j=1
    c=0
    while c<k:
        arr[0]+=arr[j]
        arr[j]=0
        j+=1
        c+=1
    return arr[0]-0


# In[ ]:


n=4
k=1
arr=[56,92,65,45]
Barrel(n, arr, k)


# In[ ]:





# In[ ]:





# In[ ]:


#Three Pointers!
def Piranah_1(n, arr):
    k=-1
    i=0
    j=1
    while (k>=0 or j<n) and i<n:
        if k>=0 and arr[i]>arr[k]:
            k-=1
            arr[i]+=1
        elif j<n and arr[i]>arr[j]:
            j+=1
            arr[i]+=1
        else:
            i+=1
            j+=1
            k+=1
    if k<0 and j>=n:
        return i+1
    else:
        return -1


# In[ ]:


def Piranah_2(n, arr):
    m=max(arr)
    idx=0
    for i in range(0, n):
        if i>0 and (arr[i]>arr[i-1] and arr[i]==m):
            idx=i+1
            break
        elif (i<n-1) and (arr[i]>arr[i+1] and arr[i]==m):
            idx=i+1
            break
    if idx>0:
        return idx
    else:
        return -1


# In[ ]:


n=3
arr=[1,1,1]
Piranah_2(n, arr)


# In[ ]:





# In[ ]:





# In[ ]:


def Granny(n, arr):
    arr=sorted(arr)
    j=n-1
    while j>=0:
        if j+1>=arr[j]:
            return j+1+1
        j-=1
    return 1


# In[ ]:





# In[ ]:





# In[ ]:


def Robots(n, a, b):
    x,y=0,0
    for i in range(n):
        if a[i]==1 and b[i]==0:
            x+=1
        elif b[i]==1 and a[i]==0:
            y+=1
            
    if x==0:
        return -1
    else:
        c=y+1
        if c%x==0:
            return c//x
        else:
            return (c//x)+1


# In[ ]:


n=1
a=[0]
b=[1]
Robots(n, a, b)


# In[ ]:





# In[ ]:





# In[ ]:


def Windows(n):
    if n==1 or n==2 or n==4:
        return -1
    if n%3==0:
        print(n//3, 0, 0)
    elif n%3==1:
        print((n-7)//3, 0, 1)
    else:
        print((n-5)//3, 1, 0)
    


# In[ ]:


Windows(67)


# In[ ]:





# In[ ]:





# In[ ]:


def Indices(n, arr):
    for i in range(1, n-1):
        if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
            print('YES')
            print(i, i+1, i+2)
            return 
    print('NO')


# In[ ]:


n=4
a=[1,2,4,3]
Indices(n, a)


# In[ ]:





# In[ ]:





# In[ ]:


def Sets(n, arr):
    count=[0 for i in range(101)]
    for k in arr:
        count[k]+=1
    for i in range(len(count)):
        if count[i]==0:
            x=i
            count[i]=-1
            break
    for i in range(len(count)):
        if count[i]<=1:
            y=i
            break
    return x+y


# In[ ]:


n=6
a=[0, 2, 1, 5, 0, 1]
Sets(n, a)


# In[ ]:





# In[ ]:





# In[ ]:


def Birthday(n, arr):
    arr=sorted(arr)
    l=[]
    mid=n//2
    i, j = 0, mid
    
    while j<n:
        l.append(arr[j])
        if i<mid:
            l.append(arr[i])
        i+=1
        j+=1
    c=0
    for i in range(1, n-1):
        if l[i]<l[i-1] and l[i]<l[i+1]:
            c+=1
    return l, c


# In[ ]:


n=6
arr=[1,2,3,4,5,6]
Birthday(n, arr)


# In[ ]:





# In[ ]:





# In[ ]:


def ebne(n):
    l=[]
    c=0
    while n!=0:
        r=n%10
        if r%2==1:
            l.append(r)
            c+=1
        n=n//10
    if c<=1:
        return -1
    else:
        return str(l[-1])+str(l[-2])
        


# In[ ]:





# In[ ]:





# In[ ]:


def Ugly(n):
    if n==1:
        return -1
    s=""
    for i in range(1, n+1):
        if i==1:
            s=s+str(2)
        else:
            s=s+str(3)
    return int(s)
            


# In[ ]:


Ugly(10)


# In[ ]:





# In[ ]:





# In[ ]:


def BogoSort(n, arr):
    return sorted(arr, reverse=True)


# In[ ]:





# In[ ]:


def Malfunctioned(s):
    l=len(s)
    b=[False for i in range(26)]
    i=0
    
    while i<l:
        j=i+1
        
        while j<l:
            if s[i]==s[j]:
                j+=1
            else:
                break
        if (j-i)%2==1:
            b[ord(s[i])-ord('a')]=True
        
        i=j
        
    for i in range(len(b)):
        if b[i]:
            print(chr(97+i), end='')
                    


# In[ ]:


s='zzzaaz'
Malfunctioned(s)


# In[ ]:





# In[ ]:





# In[ ]:


def Donuts(a, b, c):
    if a<c:
        print(1, end=' ')
    else:
        print(-1, end=' ')
    
    if a*b>c:
        print(b, end=' ')
    else:
        print(-1, end=' ')


# In[ ]:


a,b,c=1000000000, 1000000000, 1000000000
Donuts(a, b, c)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


def Tiles(arr, row, col, x, y):
    cost=0
    for i in range(row):
        for j in range(col):
            if arr[i][j]=='.':
                if j<col-1 and arr[i][j+1]=='.' and (2*x>y):
                    cost+=y
                    arr[i][j]='*'
                    arr[i][j+1]='*'
                else:
                    cost+=x
                    arr[i][j]='*'
    return cost
            


# In[ ]:


x='abc'
list(x)


# In[ ]:





# In[ ]:





# In[ ]:


import sys
def IandC(n):
    ans=sys.maxsize
    i=1
    while i*i<=n:
        x=i-1
        x=x+n//i
        if n%i==0:
            x-=1
        ans=min(ans, x)
        i+=1
        
    return ans


# In[ ]:


IandC(5)


# In[ ]:





# In[ ]:





# In[ ]:


def Bomb_Brute_Force(s):
    if ('AB' not in s) and ('BB' not in s):
        return len(s)
    i=0
    count=0
    while True:
        if 'AB' in s:
            i=s.find('AB')
            s=s[:i]+s[i+2:]
        elif 'BB' in s:
            i=s.find('BB')
            s=s[:i]+s[i+2:]
        else:
            break
    return len(s)


# In[ ]:


def Bomb_Stack(s):
    l=[]
    count=0
    for i in range(len(s)):
        if s[i]=='A':
            l.append(s[i])
        else:
            if len(l)==0:
                l.append(s[i])
            elif l[-1]=='A':
                l.pop(-1)
                count+=1
            else:
                l.pop(-1)
                count+=1
                
    return len(s)-(2*count)    


# In[ ]:


x='AAA'
Bomb_Stack(x)


# In[ ]:





# In[ ]:





# In[10]:


def TwoArray(n, arr, t):
    cnt=0
    # If t is even!
    if t%2==0:
        mid=t//2
        for i in range(n):
            if arr[i]<mid:
                print(0, end=" ")
            elif arr[i]>mid:
                print(1, end=" ")
            else:
                if cnt%2==0:
                    print(0, end=" ")
                else:
                    print(1, end=" ")
                cnt+=1  
    # If t is Odd!
    else:
        for i in range(n):
            if arr[i]%2==0:
                print(0, end=" ")
            else:
                print(1, end=" ")
            
    


# In[11]:


n=3
arr=[3,3,3]
t=6
TwoArray(n, arr, t)


# In[ ]:





# In[ ]:





# In[ ]:


def Sequence(arr):
    i=0
    j=len(arr)-1
    res=[]
    while i<j:
        res.append(arr[i])
        res.append(arr[j])
        i+=1
        j-=1
    if len(arr)%2!=0:
        res.append(arr[i])
        
    return res
        


# In[ ]:


a=[42]
Sequence(a)


# In[ ]:





# In[ ]:





# In[ ]:


def Year(s):
    if (s[-4]=='2') and (s[-3]=='0') and (s[-2]=='2') and (s[-1]=='0'):
        return 'YES'
    elif (s[0]=='2') and (s[-3]=='0') and (s[-2]=='2') and (s[-1]=='0'):
            return 'YES'
    elif (s[0]=='2') and (s[1]=='0') and (s[-2]=='2') and (s[-1]=='0'):
            return 'YES'
    elif (s[0]=='2') and (s[1]=='0') and (s[2]=='2') and (s[-1]=='0'):
        return 'YES'
    elif (s[0]=='2') and (s[1]=='0') and (s[2]=='2') and (s[3]=='0'):
        return 'YES'
    else:
        return 'NO'


# In[ ]:


s='20200'
Year(s)


# In[ ]:





# In[ ]:





# In[ ]:


def Unique(x):
    if x<10:
        return x
    elif x<18:
        return str(x-9)+'9'
    elif x<25:
        return str(x-17)+'89'
    elif x<31:
        return str(x-24)+'789'
    elif x<36:
        return str(x-30)+'6789'
    elif x<40:
        return str(x-35)+'56789'
    elif x<43:
        return str(x-39)+'456789'
    elif x<45:
        return str(x-42)+'3456789'
    elif x==45:
        return 123456789
    elif x>45:
        return -1


# In[ ]:


int(Unique(45))


# In[ ]:





# In[ ]:





# In[ ]:


def AvoidZeros(n, arr):
    s=sum(arr)
    if s==0:
        print('NO')
    else:
        print('YES')
        arr=sorted(arr)
        if s<0:
            for i in range(n):
                print(arr[i], end=" ")
        else:
            for i in range(n-1, -1, -1):
                print(arr[i], end=" ")
            


# In[ ]:


s='591'
sorted(s)


# In[ ]:





# In[ ]:


def Prob(n, sr, sb):
    cr, cb = 0, 0
    for i in range(n):
        if sr[i]>sb[i]:
            cr+=1
        elif sr[i]<sb[i]:
            cb+=1
    if cr>cb:
        print('RED')
    elif cb>cr:
        print('BLUE')
    else:
        print('EQUAL')


# In[ ]:


Prob(3, '314', '159')


# In[ ]:





# In[ ]:





# In[ ]:


def Robot(n):
    dp=[0 for i in range(n+1)]
    dp[1]=4
    
    for i in range(2, n+1):
        if i%2==0:
            dp[i]=(i//2+1)*(i//2+1)
        else:
            dp[i]=2*(i//2+1)*(i//2+2)
    return dp[n]


# In[ ]:


Robot(5)


# In[ ]:





# In[ ]:





# In[ ]:


def Dungeon(a, b, c):
    if (a+b+c)%9==0:
        if min(a,b,c)>=(a+b+c)//9:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')


# In[ ]:


a=52953008 
b=41784347 
c=28668647
Dungeon(a, b, c)


# In[ ]:





# In[ ]:





# In[ ]:


def JumpGame(n):
    steps=0
    while (steps*(steps+1)<2*n):
        steps+=1
    if steps*(steps+1)//2 == n+1:
        steps+=1
    return steps
        


# In[ ]:


JumpGame(2)


# In[ ]:





# In[ ]:





# In[ ]:


import operator
def Transformation(n, arr):
    res=[]
    if n==1:
        res.append(arr[0])
    else:
        i,j=0,1
        while j<n:
            if arr[i]==arr[j]:
                i+=1
                j+=1
            else:
                res.append(arr[i])
                i+=1
                j+=1
        res.append(arr[i])
        
    d={}
    for i in res:
        d[i]=d.get(i,0)+1
    d[res[0]]-=1
    d[res[-1]]-=1
    
    x=sorted(d.items(), key=operator.itemgetter(1))
    return x[0][1]+1
        
            


# In[ ]:


n=11
l=[2, 2, 1, 2, 3, 2, 1, 2, 3, 1, 2]
Transformation(n, l)


# In[ ]:





# In[ ]:





# In[6]:


for _ in range(int(input())):
    li=[]
    n = int(input())
    for _ in range(n):
        li.append(list(input()))

    a=li[0][1]
    b=li[1][0]
    c=li[n-2][n-1]
    d=li[n-1][n-2]

    if a==b and a==c and a==d:
        print("2")
        print(n-1,n)
        print(n,n-1)
    elif a==b and a!=c and a==d:
        print("1")
        print(n,n-1)
    elif a==b and a==c and a!=d:
        print("1")
        print(n-1,n)
    elif a==b and a!=c and a!=d:
        print("0")
    elif a!=b and a==c and a==d:
        print("1")
        print("1","2")
    elif a!=b and b==c and b==d:
        print("1")
        print("2","1")

    elif a!=b and a!=c and a==d:
        print("2")
        print("1","2")
        print(n-1,n)
    elif a!=b and b!=c and b==d:
        print("2")
        print("1","2")
        print(n,n-1)



# In[ ]:





# In[ ]:





# In[18]:


def Districts(n, arr):
    x=sorted(arr)
    if x[0]==x[-1]:
        print('NO')
        return 
    
    l=[]
    print('YES')
    for i in range(1, n):
        if arr[0]!=arr[i]:
            print(0+1, i+1)
        else:
            l.append(i)
            
    for i in range(1, n):
        if arr[i]!=arr[0]:
            break
    r=i
    for i in l:
        print(r+1, i+1)


# In[19]:


n=4
arr=[1, 2, 3, 4]
Districts(n, arr)


# In[ ]:





# In[ ]:





# In[21]:


def Snakes(l, s):
    #Special Case, one big round!
    hasCW=False
    hasCCW=False
    
    for i in range(l):
        if s[i]=='>':
            hasCW=True
        elif s[i]='<':
            hasCCW=True
        
    if hasCW and hasCCW:
        s=s+s[0]
        ans=0
        for i in range(l):
            if s[i]=='-' or s[i+1]=='-':
                ans+=1
        return ans
    else:
        return l


# In[ ]:





# In[ ]:





# In[ ]:


t=int(input())
for _ in range(t):
    l=[int(i) for i in input().split()]
    n,k=l[0],l[1]
    arr=[]
    for j in range(n):
        new_row=[int(i) for i in input().split()]
        arr.append(new_row)
    print(Points(n, arr, k))


# In[ ]:


def Points(n, arr, k):
    for i in range(n):
        count=0
        for j in range(n):
            if (abs(arr[i][0]-arr[j][0])+abs(arr[i][1]-arr[j][1]))<=k:
                count+=1
        if count==n:
            found=True
            break
    if found:
        return 1
    else:
        return -1


# In[ ]:





# In[ ]:





# In[13]:


import sys
def MinimumProduct(a, b, x, y, n):
    if (a-x)<=n:
        a1=x*max(b - (n-(a-x)), y)
    else:
        a1=max(a-n, x)*b
        
    if (b-y)<=n:
        a2=y*max(a-(n-(b-y)), x)
    else:
        a2=max(b-n, y)*a
        
    return min(a1,a2)
              


# In[14]:


a=10
b=10
x=8
y=5
n=3
MinimumProduct(a, b, x, y, n)


# In[ ]:





# In[ ]:





# In[62]:


def Trader(x, y, k):
    sticks=(y*k+k-1)
    if sticks%(x-1)==0:
        return (sticks//(x-1))+k
    else:
        return sticks//(x-1)+k+1


# In[63]:


x=2 
y=1000000000 
k=1000000000
Trader(x,y,k)

