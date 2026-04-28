#In this calculator we have two types of mathematic: algebra and geometry
#If user choose algebra he will have 5 variants: plus, minus, multiply, divide, square root, power, remainder of divide.
#If user choose geometry he will have 2 variants: 2d figure or 3d figure. after he can choose figure type:
#2d figures: square, rectangle, triangle, circle, rhombus
#3d figures: cube, prism, sphere
#When user choose 2d figures he can choose calculate area or border figure
#When user choose 3d figures he can choose calculate area or border or volume figure
#In settings user can find out information about all information e.g. functions in 'algebra' or 'geometry'
#Also in settings user can on/off function to see not only answer but also formula

seeformula = '3 - See the formula you chose'

def MENU():
    print(' ') 
    print('MENU / Choose variant:')              #User must choose variant calculator or settings
    print('1 - Calculator')
    print('2 - Settings')
    print('3 - Exit')

def SETTINGS():
    print(' ')
    print('SETTINGS / Choose variant:')
    print('1 - Information about all function')
    print('2 - Go to calculator')
    print('0 - Exit')

def algebry():
    print(' ')
    print('1 - Plus')
    print('2 - Minus')
    print('3 - Multiply')
    print('4 - Divide')
    print('5 - Square root')
    print('6 - Power')
    print('7 - Remainder of divide')
    print('0 - Back to MENU')

def geometry2D():
    print(' ')
    print('1 - Square')
    print('2 - Rectangle')
    print('3 - Triangle')
    print('4 - Circle')
    print('5 - Rhombus')
    print('0 - Back to MENU')

def geometry3D():
    print(' ')
    print('1 - Cube')
    print('2 - Right Prism')
    print('3 - Sphere')
    print('0 - Back to MENU')


from random import randint        #Add module random
from math import sqrt, pi         #Add module math

print("Hello my friend, it is calculator")             #Greeting
print("by YP 'Witcher204'")                        #Production by...

MENU()
chose1 = int(input('Text variant: '))         #User text variant in terminal

if chose1 == 3:         #When user chose 3 he exit the calculator
    print('Bye')
    exit()

if chose1 == 2:                   #If user chose 2 calculator open settings
    while True:
            SETTINGS()
            print(seeformula)
            chose2 = int(input('Text variant: '))

            if chose2 == 1:
                print(' ')          #If user chose 1 settings open "Information about all function"
                print('Not yet')
            elif chose2 == 3:
                if len(seeformula) < 30:          #if seeformula ("See the formula you chose"):
                    seeformula = "3 - Don't see the formula you chose"
                    print("Success! Now you see the formula")
                else:
                    seeformula = '3 - See the formula you chose'    #Else (seeformula its "don't see")
                    print("Success! Now you don't see formula")
            elif chose2 == 2:
                chose1 = 1              #If user chose 2 he go to the calculator
                break
            elif chose2 == 0:          #If user chose 0 he leave the app
                print('See you after!')
                exit()



if chose1 == 1:
    while True:
        print(' ')
        print('Chose type of mathematic: 1 - algebra, 2 - geometry, 3 - exit')       #User chose algebra/geometry/exit
        chose3 = int(input('Text variant: '))

        if chose3 == 1:         #If user chose algebra:
            algebry()
            chose4 = int(input('Text variant: '))
            if chose4 == 1:      #Plus
                a = int(input('Text first number: '))
                b = int(input('Text second number: '))
                if len(seeformula) > 30:
                    print(' ')
                    print(a, '+', b, '=', a+b)
                else:
                    print(a+b)
            if chose4 == 2:    #Minus
                a = int(input('Text first number: '))
                b = int(input('Text second number: '))
                if len(seeformula) > 30:
                    print(a, '-', b, '=', a-b)
                else:
                    print(a-b)
            if chose4 == 3:      #Multiply
                a = int(input('Text first number: '))
                b = int(input('Text second number: '))
                if len(seeformula) > 30:
                    print(a, '*', b, '=', a*b)
                else:
                    print(a*b)
            if chose4 == 4:        #Divide
                a = int(input('Text first number: '))
                b = int(input('Text second number: '))
                if len(seeformula) > 30:
                    print(a, '/', b, '=', a/b)
                else:
                    print(a/b)
            if chose4 == 5:        #Square root
                a = int(input('Text number: '))
                print('Square root of number', a, "it's", sqrt(a))
            if chose4 == 6:       #Power
                a = int(input('Text number: '))
                b = int(input('Text power number: '))
                if len(seeformula) > 30:
                    print(a, 'of power', b, '=', a**b)
                else:
                    print(a**b)
            if chose4 == 7:            #Remainder of divide
                a = int(input('Text first number: '))
                b = int(input('Text second number: '))
                if len(seeformula) > 30:
                    print('Ramainder of divide', a, '/', b, '=', a%b)
                else:
                    print(a%b)
            #chose4 have variant '0' for exit to menu algebra/geometry/exit but we dont have this point, btw user chose '0' he back to menu

        if chose3 == 3:           #if user chose3 chose 3 he leave the app
            print('Bye!')
            exit()

        if chose3 == 2:                #if user chose3 == 2(geometry) he have 2 variants, 2D or 3D geometry
            print(' ')
            print('1 - 2D geometry, 2 - 3D geometry')
            chose5 = int(input('Text variant: '))

            if chose5 == 1:      #If user chose 2D:
                geometry2D()
                chose2D = int(input('Text variant: '))

                if chose2D == 1:           #User chose square
                    a = int(input("Enter side of a square: "))
                    print("1 - Area of a square, 2 - Border of a square")
                    chose_square = int(input('Enter variant: '))       #user enter he want know area of a square or border
                    if chose_square == 1:     #Area
                        if len(seeformula) > 30:
                            print(a, '*', a, '=', a*a)
                            print("Area of a square =", a*a)
                        else:
                            print("Area of a square =", a*a)
                    if chose_square == 2:      #Border
                        if len(seeformula) > 30:
                            print(a, '+', a, '+', a, '+', a, '=', a*4)
                            print('Border of a square =', a*4)
                        else:
                            print('Border of a square =', a*4)

                if chose2D == 2:      #User chose rectangle
                    a = int(input('Enter first side of a rectangle: '))
                    b = int(input('Enter last side of a rectangle: '))
                    print("1 - Area of a rectangle, 2 - Border of a rectangle")
                    chose_rectangle = int(input('Enter variant: '))
                    if chose_rectangle == 1:     #If user chose area
                        if len(seeformula) > 30:
                            print(a, '*', b, '=', a*b)
                            print('Area of a rectangle =', a*b)
                        else:
                            print('Area of a rectangle =', a*b)
                    if chose_rectangle == 2:       #If user chose border
                        if len(seeformula) > 30:
                            print(a, '+', a, '+', b, '+', b, '=', a*2+b*2)
                            print("Border of a rectangle =", a*2+b*2)
                        else:
                            print("Border of a rectangle =", a*2+b*2)

                if chose2D == 3:      #User chose triangle
                    print(' ')
                    print('1 - equilateral triangle, 2 - isosceles triangle')
                    print('3 - scalene triangle, 4 - right triangle')
                    chose_triangle = int(input('Enter variant: '))       #User chose type of a triangle

                    if chose_triangle == 1:    #If user chose equilateral triangle
                        print(' ')
                        print("1 - Area of a  equilateral triangle, 2 - Border of a equilateral triangle")
                        chose_equilateral_triangle = int(input('Enter variant: '))         #User chose area or border
                        print(' ')
                        a = int(input("Enter 'a' side of a triangle: "))
                        if chose_equilateral_triangle == 1:     #If user chose area
                            if len(seeformula) > 30:
                                print(' ')
                                print('The square of', a, '*', 'square root of three and divided by four')
                                print('Area of a equilateral triangle =', (a**2 * sqrt(3)) / 4)
                            else:
                                print(' ')
                                print('Area of a equilateral triangle =', (a**2 * sqrt(3)) / 4)
                        if chose_equilateral_triangle == 2:       #If user chose border
                            if len(seeformula) > 30:
                                print(' ')
                                print(a, '* 3 =', a*3)
                                print('Border of a equilateral triangle =', a*3)
                            else:
                                print(' ')
                                print('Border of a equilateral triangle =', a*3)

                    if chose_triangle == 2:      #If user chose isosceles triangle:
                        print(' ')
                        print("1 - Area of a isosceles triangle, 2 - Border of a isosceles triangle")
                        chose_isosceles_triangle = int(input('Enter variant: '))
                        if chose_isosceles_triangle == 1:      #If user chose Area
                            print(' ')
                            b = int(input("Enter 'b' side: "))
                            h = int(input("Enter 'h' side: "))
                            if len(seeformula) > 30:
                                print(' ')
                                print('(', b, '*', h, ')', '/2 = ', b*h/2, sep='')
                                print('Area of a isosceles triangle =', b*h/2)
                            else:
                                print(' ')
                                print('Area of a isosceles triangle =', b*h/2)
                        if chose_isosceles_triangle == 2:         #If user chose Border
                            print(' ')
                            a = int(input("Enter 'a' side: "))
                            b = int(input("Enter 'b' side: "))
                            if len(seeformula) > 30:
                                print(' ')
                                print('2*', a, '+', b, ' = ', (2*a)+b, sep='')
                                print('Border of a isosceles triangle =', (2*a)+b)
                            else:
                                print(' ')
                                print('Border of a isosceles triangle =', (2*a)+b)

                    if chose_triangle == 3:        #If user chose scalene triangle
                        print(' ')
                        print("1 - Area of a scalene triangle, 2 - Border of a scalene triangle")
                        chose_scalene_triangle = int(input('Enter variant: '))
                        if chose_scalene_triangle == 1:            #User chose area
                            side_a = int(input("You know side 'a'? 1 - yes, 2 - no: "))
                            side_b = int(input("You know side 'b'? 1 - yes, 2 - no: "))
                            side_c = int(input("You know side 'c'? 1 - yes, 2 - no: "))
                            side_h = int(input("You know side 'h'? 1 - yes, 2 - no: "))
                            if side_b == 1 and side_h == 1:      #If user know b and h sides
                                b = int(input("Enter side 'b': "))
                                h = int(input("Enter side 'h': "))
                                if len(seeformula) > 30:
                                    print(' ')
                                    print('(', b, '*', h, '/2 = ', b*h/2, sep='')
                                    print('Area of a scalene triangle =', b*h/2)
                                else:
                                    print(' ')
                                    print('Area of a scalene triangle =', b*h/2)
                            elif side_a == 1 and side_b == 1 and side_c == 1:      #If user know a and b and c sides
                                a = int(input("Enter side 'a': "))
                                b = int(input("Enter side 'b': "))
                                c = int(input("Enter side 'c': "))
                                p = (a+b+c)/2
                                if len(seeformula) > 30:
                                    print('Area is the square root of the multipled a, b, c')
                                    print('Area of a scalene triangle =', sqrt(p*(p-a)*(p-b)*(p-c)))
                                else:
                                    print('Area of a scalene triangle =', sqrt(p*(p-a)*(p-b)*(p-c)))
                            else:
                                print('Sorry. We cant calculate area of your scalene triangle')
                        if chose_scalene_triangle == 2:         #User chose border
                            a = int(input("Enter side 'a': "))
                            b = int(input("Enter side 'b': "))
                            c = int(input("Enter side 'c': "))
                            if len(seeformula) > 30:
                                print(' ')
                                print(a, '+', b, '+', c, '=', a+b+c)
                                print('Border of a scalene triangle =', a+b+c)
                    
                    if chose_triangle == 4:         #User chose right triangle
                        print(' ')
                        print("1 - Area of a right triangle, 2 - Border of a right triangle")
                        chose_right_triangle = int(input('Enter variant: '))
                        if chose_right_triangle == 1:      #User chose area
                            a = int(input("Enter side 'a': "))
                            b = int(input("Enter side 'b': "))
                            if len(seeformula) > 30:
                                print(' ')
                                print(a, '*', b, '/ 2 =', a*b/2)
                                print("Area of a right triangle =", a*b/2)
                            else:
                                print("Area of a right triangle =", a*b/2)
                        if chose_right_triangle == 2:       #User chose border
                            a = int(input("Enter side 'a': "))
                            b = int(input("Enter side 'b': "))
                            c = int(input("Enter side 'c': "))
                            if len(seeformula) > 30:
                                print(' ')
                                print(a, '+', b, '+', c, '=', a+b+c)
                                print('Border of a right triangle =', a+b+c)

                if chose2D == 4:       #User chose circle
                    print(' ')
                    r = int(input("Enter 'r': "))
                    print("1 - Area of a circle, 2 - Border of a circle")
                    chose_circle = int(input('Enter variant: '))
                    if chose_circle == 1:        #user chose area
                        if len(seeformula) > 30:
                            print(' ')
                            print(r, '*', r, '* pi =', r*r*pi)
                            print('Area of a circle = ', r*r*pi, ' or ', r*r, 'pi', sep='')
                        else:
                            print('Area of a circle = ', r*r*pi, ' or ', r*r, 'pi', sep='')
                    if chose_circle == 2:       #user chose border
                        if len(seeformula) > 30:
                            print(' ')
                            print(r, '+', r, '* pi =', (r+r)*pi)
                            print('Border of a circle = ', (r+r)*pi, ' or ', r+r, 'pi', sep='')

                if chose2D == 5:     #User chose rhombus    
                    print(' ')
                    print("1 - Area of a rhombus, 2 - Border of a rhombus")
                    chose_rhombus = int(input('Enter variant: '))
                    if chose_rhombus == 1:         #User chose area
                        rhombus_d1_d2 = int(input("You know 'd1' and 'd2' of a rhombus? 1 - yes, 2 - no: ")) #User must know d1 and d2 or a and h
                        rhombus_a_h = int(input("You know 'a' and 'h' of a rhombus? 1 - yes, 2 - no: "))
                        if rhombus_d1_d2 == 1:     #If user know d1 and d2
                            d1 = int(input('Enter d1: '))
                            d2 = int(input('Enter d2: '))
                            if len(seeformula) > 30:
                                print(' ')
                                print(d1, '*', d2, '/2 =', d1*d2/2, sep='')
                                print('Area of a rhombus =', d1*d2/2)
                            else:
                                print('Area of a rhombus =', d1*d2/2)
                        elif rhombus_a_h == 1:    #If user know a and h
                            a = int(input("Enter 'a': "))
                            h = int(input("Enter 'h': "))
                            if len(seeformula) > 30:
                                print(' ')
                                print(a, '*', h, '=', a*h)
                                print('Area of a rhombus =', a*h)
                            else:
                                print('Area of a rhombus =', a*h)
                        else:      #If user doesn't know d1 and d2 or a and h
                            print('Sorry. We cant calculate area of your rhombus')
                    if chose_rhombus == 2:      #If user chose border
                        print(' ')
                        a = int(input("Enter 'a': "))
                        if len(seeformula) > 30:
                            print(' ')
                            print('4 * a =', 4*a)
                            print('Border of a rhombus =', 4*a)
                        else:
                            print('Border of a rhombus =', 4*a)

            if chose5 == 2:    #If user chose 3D geometry
                geometry3D()
                chose3D = int(input('Enter variant: '))

                if chose3D == 1:      #User chose cube
                    print(' ')
                    print("1 - Area of a cube, 2 - Border of a cube")
                    chose_cube = int(input('Enter variant: '))
                    if chose_cube == 1:     #User chose area
                        a = int(input("Enter side 'a': "))
                        if len(seeformula) > 30:
                            print(' ')
                            print(a, '*', a, '*', a, '=', a*a*a)
                            print('Area of a cube =', a*a*a)
                        else:
                            print('Area of a cube =', a*a*a)
                    if chose_cube == 2:      #User chose border
                        a = int(input("Enter side 'a': "))
                        if len(seeformula) > 30:
                            print(' ')
                            print(a, '*', a, '=', a*a)
                            print('Boared of a cube =', a*a)
                        else:
                            print('Boared of a cube =', a*a)

                if chose3D == 2:       #User chose prism
                    print(' ')
                    print("1 - Area of a right prism, 2 - Border of a right prism")
                    chose_prism = int(input('Enter variant: '))
                    if chose_prism == 1:     #User chose area
                        prism_a_h = int(input("You know 'a' and 'h' and 'h'?: "))
                        if prism_a_h == 1:     #If user know a and b and h
                            a = int(input("Enter side 'a': "))
                            b = int(input("Enter side 'b': "))
                            h = int(input("Enter side 'h': "))
                            if len(seeformula) > 30:
                                print(' ')
                                print("Area of a base it's ", a, '*', b, ' = ', a*b, sep='')
                                print('Area of a base =', a*b)
                                print(' ')
                                print("Area of side b|h it's ", b, '*', h, ' = ', b*h, sep='')
                                print('Area of b|h side =', b*h)
                                print(' ')
                                print("Area of side a|h it's ", a, '*', h, ' = ', a*h, sep='')
                                print('Area of a|h side =', a*h)
                                print("Area of prism it's (a|b + b|h + a|h)*2 =", (a*b+b*h+a*h)*2)
                            else:
                                print("Area of prism it's (a|b + b|h + a|h)*2 =", (a*b+b*h+a*h)*2)
                        else:
                            print("Sorry. We can't calculate your prism")

                    if chose_prism == 2:        #If user chose border
                        prism_a_b_h = int(input("You know 'a' and 'h' and 'h'?: "))
                        if prism_a_b_h == 1:      #if user know a and b and h
                            a = int(input("Enter side 'a': "))
                            b = int(input("Enter side 'b': "))
                            h = int(input("Enter side 'h': "))
                            if len(seeformula) > 30:
                                print(' ')
                                print('a*4 + b*4 + h*4 =', a*4+b*4+h*4)
                                print("Border of a prism =", a*4+b*4+h*4)
                            else:
                                print("Border of a prism =", a*4+b*4+h*4)
                        else:
                            print("Sorry. We can't calculate your prism")
                
                if chose3D == 3:
                    print(' ')
                    print("1 - Area of a right prism, 2 - Border of a right prism")









