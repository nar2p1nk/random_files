# result = 0
# arr1 = list(range(200))
# arr2 = list(range(200, 300))
# for x1,x2 in zip(arr1,arr2):
#     result += x1*x2
# result

# print(result)

import argparse

# parse = argparse.ArgumentParser()
# args = parse.parse_args()
# print(args.cubed**4)


# parser = argparse.ArgumentParser()
# parser.add_argument('volume_of_a_sphere', help='enter a radius to calculate volume',type=int)
# arguments = parser.parse_args()

# pi = 22/7

# print(4/3*pi*arguments.volume_of_a_sphere**3)



# parser = argparse.ArgumentParser()
# parser.add_argument('cubed', help='display the cube of a given number',type=int)

# parser.add_argument('-v','--verbosity',action='count',default=0,help='increase output of verbosity',)

# arguments = parser.parse_args()

# answer = arguments.cubed**3

# if arguments.verbosity >= 1:
#     print('{}^3 = {}'.format(arguments.cubed,answer))
# elif arguments.verbosity >=2:
#      print('the cube of {} is {}'.format(arguments.cubed, answer))

# else:
#     print(answer)



# parser = argparse.ArgumentParser(description='calculate x to the power of y')
# parser.add_argument('x',type=int, help='the base')
# parser.add_argument('y',type=int, help='the exponent')
# parser.add_argument('-v','--verbosity',action='store_true')
# parser.add_argument('-q','--quiet',action='store_true')

# arguments = parser.parse_args()

# answer = arguments.x**arguments.y

# if arguments.quiet:
#     print('{}^{} = {}'.format(arguments.x,arguments.y,answer))
# elif arguments.verbosity:
#     print('{} raise to the power of {} is {}'.format(arguments.x,arguments.y,answer))
# else:
#     print(answer)


# create a geometrical calculator for a square*

parser = argparse.ArgumentParser(description='a calculator for a square or rectangle ')
parser.add_argument('length', type=int,help='enter length(if 3d)')
parser.add_argument('width', type=int, help='enter width')
parser.add_argument('height', type=int,help='enter height')

argu = parser.parse_args()

area = argu.length * argu.width
volume = argu.length * argu.width * argu.height

if argu.height != 0:
    print(volume)
else:
    print(area)