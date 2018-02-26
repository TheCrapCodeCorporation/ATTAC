import math as m

rightAngleAscii = '''
            z
          /|
         / |
   C    /  |    A
       /   |
      /    |
     /_____|
    x       y: 90
    
        B
'''

leftAngleAscii = '''
        z
        /\\ 
       /  \\
C     /    \\    A
     /      \\
    /        \\
   /__________\\
  x            y
    
        B
'''

angleList = []
sideList = []

sideA = None
sideB = None
sideC = None

angleX = None
angleY = None
angleZ = None


def pythagoras():
    # Find Sides with a^2 + b^2 = c^2 rule
    try: 
        if sideA == None and sideB != None and sideC != None:
            sideA = m.sqrt(sideC**2 - sideB**2)
            sideList.append('a')
    except UnboundLocalError: pass

    try: 
        if sideB == None and sideA != None and sideC != None:
            sideB = m.sqrt(sideC**2 - sideA**2)
            sideList.append('b')
    except UnboundLocalError: pass
    
    try: 
       if sideC == None and sideA != None and sideB != None:
            sideC = m.sqrt(sideB**2 + sideA**2)
            sideList.append('c')
    except UnboundLocalError: pass


def angles180():
    # Find angles with 180 rule
    try:
        if angleX == None and angleY != None and angleZ != None:
            angleX = 180 - (angleY + angleZ)
            angleList.append('x')
    except UnboundLocalError: pass

    try:
        if angleY == None and angleX != None and angleZ != None :
            angleY = 180 - (angleX + angleZ)
            angleList.append('y')
    except UnboundLocalError: pass
    
    try:
        if angleZ == None and angleY != None and angleX != None:
            angleZ = 180 - (angleY + angleX)
            angleList.append('z')
    except UnboundLocalError: pass

    

print('First, is your triangle right angled? Y/N')

rightAngle = input('> ').lower()

if rightAngle == 'y':
    angleY = '90'
    print(rightAngleAscii)
    angleList.append('y')
    
    print('Please input the sides you have')
    print('If you dont have that side, input a non-number and it will skip')
    
    try: 
        sideA = int(input('Side A: '))
        sideList.append('a')
    except ValueError: 
        sideA = None        
        pass
    try: 
        sideB = int(input('Side B: '))
        sideList.append('b')
    except ValueError: 
        sideB = None
        pass
    try: 
        sideC = int(input('Side C: '))
        sideList.append('c')
    except ValueError:
        sideC = None
        pass
    
    pythagoras()

    print('\nValues so far:')
    print('Side A: ' + str(sideA))
    print('Side B: ' + str(sideB))
    print('Side C: ' + str(sideC))

    print('Please input the angles')
    print('If you dont have that side, input a non-number and it will skip')

    try: 
        angleX = int(input('Angle X: '))
        angleList.append('x')
    except ValueError: 
        angleX = None
        pass
    try: 
        angleZ = int(input('Angle Z: '))
        angleList.append('z')
    except ValueError:
        angleZ = None
        pass
    
    angles180()
    
    if len(sideList) == 3:
        angleX = m.asin(sideA / sideC)
        angleZ = m.asin(sideB / sideC)

    if len(angleList) == 3:
        if 'a' in sideList:
            sideB = sideA / m.tan(angleX)
            sideC = sideA / m.sin(angleY)
        if 'b' in sideList:
            sideA = sideB / m.tan(angleZ)
            sideC = sideB / m.sin(angleY)
        if 'c' in sideList:
            sideA = m.sin(angleY) * sideC
            sideB = m.sin(angleZ) * sideC




    if len(sideList) == 1 and len(angleList) == 1:
        print('insufficent data')

print('Side A: ' + str(sideA))
print('Side B: ' + str(sideB))
print('Side C: ' + str(sideC))
print('Angle X: ' + str(angleX))
print('Angle Y: ' + str(angleY))
print('Angle Z: ' + str(angleZ))


if rightAngle == 'n':
    print(leftAngleAscii)
