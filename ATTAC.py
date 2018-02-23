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

print('First, is your triangle right angled? Y/N')

rightAngle = input('> ').lower()

if rightAngle == 'y':
    angleY = '90'
    print(rightAngleAscii)
    
    print('Please input the sides you have')
    print('If you dont have that side, input a non-number and it will skip')
    
    try: sideA = int(input('Side A: '))
    except ValueError: 
        sideA = None        
        pass
    try: sideB = int(input('Side B: '))
    except ValueError: 
        sideB = None
        pass
    try: sideC = int(input('Side C: '))
    except ValueError:
        sideC = None
        pass
    
    # Find Sides with a^2 + b^2 = c^2 rule
    if sideA == None and sideB != None and sideC != None:
        sideA = m.sqrt(sideC**2 - sideB**2)
    if sideB == None and sideA != None and sideC != None:
        sideB = m.sqrt(sideC**2 - sideA**2)
    if sideC == None and sideA != None and sideB != None:
       sideC = m.sqrt(sideB**2 + sideA**2)

    print('\nValues so far:')
    print('Side A: ' + str(sideA))
    print('Side B: ' + str(sideB))
    print('Side C: ' + str(sideC))

    print('Please input the angles')
    print('If you dont have that side, input a non-number and it will skip')

    try: angleX = int(input('Angle X: '))
    except ValueError: 
        angleX = None
        pass
    try: angleZ = int(input('Angle Z: '))
    except ValueError:
        angleZ = None
        pass

    # Find angles with 180 rule
    if angleX == None and angleY != None and angleZ != None:
        angleX = 180 - (angleY + angleZ)
    if angleZ == None and angleY != None and angleX != None:
        angleZ = 180 - (angleY + angleX)
    if angleY == None:
        print('Something is very wrong, panic')

if rightAngle == 'n':
    print(leftAngleAscii)
