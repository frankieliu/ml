import numpy as np

if False:
    a = np.array([10,20,30,40])
    b = a[[False, True, False, True]]
    print(b)

if False:
    a = np.random.randint(1, 100, (5,5))
    print(a.mean())
    print(a.std())

if False:
    a = np.eye(5,5) + 5
    b = np.random.randint(1, 10, (5,1))
    print(a)
    print(np.matmul(a,b))

if False:
    a = np.random.randint(1,100,(3,3))
    b = np.random.randint(1,100,(3,3))
    print(a)
    print(b)
    print(a*b)

if False:
    a = np.random.randint(1,1000,(1,1000))
    b = np.cumsum(a)
    print(b[[9,99,499]])

if False:
    a = np.random.randint(1,101, (10,10))
    print(np.min(a), np.unravel_index(np.argmin(a), a.shape))

if False:
    a = np.random.rand(5,5)
    print(a)
    a[np.unravel_index(np.argmax(a),a.shape)] = 0
    print(a)

if False:
    a = np.array([[1,2,3],[4,5,6],[7,8,9]])
    b = a[1:3, 0:2]
    print(b)
    b[0,0] = 100
    print(a)

if False:
    a = np.random.randint(1,101,(1,20))
    print(np.sum([a % 2 == 0]))
    print(np.sum([a % 2 == 1]))

if False:
    A = np.arange(1, 17).reshape(4, 4)
    B = A[:, ::-1]
    print(B)

if False:
    a = np.arange(1,65).reshape(8,8)
    a[:,0]=1
    a[0,:]=1
    a[:,-1]=1
    a[-1,:]=1
    a[1:-1,1:-1]=0
    print(a)
    
print("hello There")