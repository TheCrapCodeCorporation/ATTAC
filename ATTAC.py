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
    
    print('Please input the sides you have, if you dont have that side')
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

    print(sideA)
    print(sideB)
    print(sideC)
    

    
if rightAngle == 'n':
    print(leftAngleAscii)
