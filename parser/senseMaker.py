
# Read data from the boards.txt file

boards_file = open('boards.txt', "r")

def line_count():
  count = 0
  for line in boards_file:
    count = count + 1
  print "Line count: ", count
