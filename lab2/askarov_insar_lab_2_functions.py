import math

# exercise 1
print("exercise 1")

height =int(input("Enter height of a rectangle: "))
width = int(input("Enter width of a rectangle: "))

def areaRect(height, width):
  return height * width

def perimeterRect(height, width):
  return 2 * (height + width)

print(f"The area of a rectangle with height {height} and wodth {width} is ", areaRect(height, width))
print(f"The permeter of a rectangle with height {height} and wodth {width} is ", perimeterRect(height, width))

radius = float(input("Enter the radius of a circle: "))

def areaCircle(radius):
  return math.pi * radius**2

def circumference(radius):
  return 2 * math.pi * radius 

print(f"The area of a circle with radius {radius} is ", areaCircle(radius))
print(f"The circumference of a citcle with radius {radius} is ", circumference(radius))

def areaRightTr(height, base):
  return 1/2 * height * base

def perimeterRightTr(height, base):
  hyp = math.sqrt(base**2 + height**2)
  return hyp + base + height

height = float(input("Enter the height of a right triangle: "))
base = float(input("Enter the base of a right triangle: "))

print(f"The area of a right triangle with height {height} and base {base} is ", areaRightTr(height, base))
print(f"The perimeter of a right triangle with height {height} and base {base} is ", perimeterRightTr(height, base))

while True:
  sides = float(input("Enter the number of sides of a regular polygon: "))
  if (sides < 3):
      sides = float(input("Enter the number of sides of a regular polygon: "))
  else: break
length = float(input("Enter the length of side of a regular polygon: "))

def angles(sides, length):
  exterior = 360 / sides
  interiors = 180 * (sides - 2)
  interior = interiors / sides
  area = ((length**2) * sides) / (4 * math.tan(180/sides))
  return exterior, interiors, interior, area

exterior, interiors, interior, area = angles(sides, length)
print(f"The exterior angle of a regular polygon with {sides} sides is {exterior} degrees")
print(f"The interior angles of a regular polygon with {sides} sides sum to {interiors} degrees") 
print(f"Each interior a regular polygon with {sides} sides is {interior} degrees")
print(f"The area of regular polygon with {sides} sides each {length} long is {area}")

# exercise 2
print("exercise 2")

number = int(input("Enter value you want to charge "))

def charge(v):
  if (v < 10):
    charge = v 
  elif (10 <= v < 25):
    charge = v + 3
  elif(25 <= v < 50):
    charge = v + 8
  elif (50 <= v < 100):
    charge = v + 20
  elif v >= 100:
    charge = v + 25      
  return f"{charge} were added to ur bank account"
  
print(charge(number))

# exercise 3
print("exercise 3")

def multiply_recursive(x, y):
    if x == 0:
        return 0
    if x % 2 != 0:
        return y + multiply_recursive(x // 2, y * 2)
    return multiply_recursive(x // 2, y * 2)

x = 8
y = 38
print(f"{x} * {y} = {multiply_recursive(x, y)}")
