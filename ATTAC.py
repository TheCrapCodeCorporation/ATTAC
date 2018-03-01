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

# Lists used to store discoved values
angleList = []
sideList = []

# Declaring variables to avoid UnboundLocalError
sideA = None
sideB = None
sideC = None
angleX = None
angleY = None
angleZ = None
area = None

# Use to find Sides with a^2 + b^2 = c^2 rule
def pythagoras():
	global sideA
	global sideB
	global sideC

	try:
		if sideA == None and sideB != None and sideC != None:
			sideA = m.sqrt(sideC ** 2 - sideB ** 2)
			sideList.append('a')
	except UnboundLocalError:
		pass

	try:
		if sideB == None and sideA != None and sideC != None:
			sideB = m.sqrt(sideC ** 2 - sideA ** 2)
			sideList.append('b')
	except UnboundLocalError:
		pass

	try:
		if sideC == None and sideA != None and sideB != None:
			sideC = m.sqrt(sideB ** 2 + sideA ** 2)
			sideList.append('c')
	except UnboundLocalError:
		pass

# Find angles with 180 rule
def angles180():
	global angleX
	global angleY
	global angleZ

	try:
		if 'x' not in angleList and 'y' in angleList and 'z' in angleList:
			angleX = 180 - (int(angleY) + int(angleZ))
			angleList.append('x')
	except UnboundLocalError:
		pass

	try:
		if 'y' not in angleList and 'x' in angleList and 'z' in angleList:
			angleY = 180 - (int(angleX) + int(angleZ))
			angleList.append('y')
	except UnboundLocalError:
		pass

	try:
		if 'z' not in angleList and 'y' in angleList and 'x' in angleList:
			angleZ = 180 - (int(angleY) + int(angleX))
			angleList.append('z')
	except UnboundLocalError: pass


print('First, is your triangle right angled? Y/N')
rightAngle = input('> ').lower()

if rightAngle == 'y':
	angleY = 90
	print(rightAngleAscii)
	angleList.append('y')

	print('Please input the sides you have')
	print('If you dont have that side, just press enter or input a non-number and it will skip')

	# Get sides the user already has
	try:
		sideA = float(input('Side A: '))
		sideList.append('a')
	except ValueError:
		sideA = None
		pass
	try:
		sideB = float(input('Side B: '))
		sideList.append('b')
	except ValueError:
		sideB = None
		pass
	try:
		sideC = float(input('Side C: '))
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
	print('If you dont have that side, just press enter or input a non-number and it will skip')

	# Get angles the user already has
	try:
		angleX = float(input('Angle X: '))
		angleList.append('x')
	except ValueError:
		angleX = None
		pass
	try:
		angleZ = float(input('Angle Z: '))
		angleList.append('z')
	except ValueError:
		angleZ = None
		pass

	angles180()
	pythagoras()

	print('\nValues so far:')
	print('Side A: ' + str(sideA))
	print('Side B: ' + str(sideB))
	print('Side C: ' + str(sideC))
	print('Angle X: ' + str(angleX))
	print('Angle Y: ' + str(angleY))
	print('Angle Z: ' + str(angleZ))

	# Calculate angles using sohcahtoa
	if len(sideList) == 3:
		angleX = m.asin(m.radians(sideA / sideC))
		angleZ = m.asin(m.radians(sideB / sideC))
		angleList.append('x', 'z')
	# Calculate sides using sohcahtoa
	if len(angleList) == 3:
		if 'a' in sideList:
			if sideB not in sideList:
				sideB = sideA / m.tan(m.radians(angleX))
				sideList.append('b')
			if sideC not in sideList:
				sideC = sideA / m.sin(m.radians(angleX))
				sideList.append('c')
		if 'b' in sideList:
			if sideA not in sideList:
				sideA = sideB * m.tan(m.radians(angleX))
				sideList.append('a')
			if sideC not in sideList:
				sideC = sideB / m.cos(m.radians(angleX))
				sideList.append('c')
		if 'c' in sideList:
			if sideA not in sideList:
				sideA = sideC * m.sin(m.radians(angleX))
				sideList.append('a')
			if sideB not in sideList:
				sideB = sideC * m.cos(m.radians(angleX))
				sideList.append('b')

	if 'a' in sideList and 'b' in sideList:
		area = (sideA * sideB) / 2

if rightAngle == 'n':
	print(leftAngleAscii)

# Print final value calculations
print('\nFinal Values:')
print('Side A: ' + str(sideA))
print('Side B: ' + str(sideB))
print('Side C: ' + str(sideC))
print('Angle X: ' + str(angleX))
print('Angle Y: ' + str(angleY))
print('Angle Z: ' + str(angleZ))
print('Area: ' + str(area))