#!/usr/bin/env python

colors = [ # names from colourlovers.com
(0, 0, 0, 'white'),
(255, 255, 255, 'black'),
(255, 0, 0, 'red'),
(0, 255, 0, 'green'),
(0, 0, 255, 'blue'),
(22, 147, 165, 'dutch teal'),
(255, 0, 102, 'hot pink'),
(251, 184, 41, 'heart of gold'),
(205, 215, 182, 'haunted milk'),
(85, 98, 112, 'mighty slate'),
(195, 255, 104, 'cerain frogs'),
(252, 251, 227, 'vanilla cream'),
(51, 51, 51, 'grr-ey'),
(211, 25, 150, 'bloons'),
(255, 153, 0, 'vitamin c'),
(240, 35, 17, 'sex on the floor'),
(97, 176, 244, 'shark lighter blue')
]


def distance(rgb1, rgb2):
  """Return distance in 3D space of RGB colors."""
  return ((rgb1[0]-rgb2[0])**2 + (rgb1[1]-rgb2[1])**2 + (rgb1[2]-rgb2[2])**2)**0.5

def guessColorName(nameMe, debug=0):
  """Return guessed human-name of a color.
  
  Keyword arguments:
  debug -- print debug messages if not 0 (default 0)
  """
  result = (distance(nameMe, colors[0]), colors[0][3])
  
  for color in colors:
    dist = distance(nameMe, color)
    if debug:
      print("\t" + str(dist) + " to " + color[3])
    if dist < result[0]:
      result = (dist, color[3])
  return result

def main():
  print(guessColorName((227, 155, 239), debug=1)[1])

if __name__ == '__main__':
  main()
