def arithmetic_arranger(problems, ans = False):
  arranged_problems = ""

  if len(problems)>5:
    arranged_problems = "Error: Too many problems."
    return arranged_problems
  
  i = 0
  d = dict()
  l = list()
  for s in problems:
    s = s.split()
    #print(s)
    if s[1] != '+' and s[1] != '-':
      arranged_problems = "Error: Operator must be '+' or '-'."
      return arranged_problems
    
    if len(s[0])>4 or len(s[2])>4:
      arranged_problems = "Error: Numbers cannot be more than four digits."
      return arranged_problems

    try:
      al = len(s[0])
      bl = len(s[2])
      a = int(s[0])
      b = int(s[2])
      if s[1] == '+':
        c = a + b
      else:
        c = a - b
      sp = max(al, bl) + 2
      l = [al, a, bl, b, c, s[1], sp]
      d[i] = l
      i = i + 1

    except:
      arranged_problems = "Error: Numbers must only contain digits."
      return arranged_problems
  j = 0
  #print(d)
  for k,v in d.items():
    space = v[6] - v[0]
    while(space):
      arranged_problems = arranged_problems + " "
      space = space - 1
    arranged_problems = arranged_problems + str(v[1])
    if j < len(problems)-1:
      for q in range(4):
        arranged_problems = arranged_problems + " "
    j = j + 1
  
  arranged_problems = arranged_problems + '\n'

  j = 0
  for k,v in d.items():
    arranged_problems = arranged_problems + v[5] + " "
    if v[2] < v[0]:
      space = v[0] - v[2]
      while space:
        arranged_problems = arranged_problems + " "
        space = space - 1
    arranged_problems = arranged_problems + str(v[3])
    if j < len(problems)-1:
      for q in range(4):
        arranged_problems = arranged_problems + " "
    j = j + 1
  
  arranged_problems = arranged_problems + '\n'
  
  j = 0
  for k,v in d.items():
    dash = v[6]
    while dash:
      arranged_problems = arranged_problems + '-'
      dash = dash - 1
    if j < len(problems)-1:
      for q in range(4):
        arranged_problems = arranged_problems + " "
    j = j + 1

  if ans == True:
    arranged_problems = arranged_problems + '\n'
    j = 0
    for k,v in d.items():
      cl = len(str(v[4]))
      space = v[6] - cl
      while space:
        arranged_problems = arranged_problems + " "
        space = space - 1
      arranged_problems  = arranged_problems + str(v[4])
      if j < len(problems)-1:
        for q in range(4):
          arranged_problems = arranged_problems + " "
      j = j + 1

  print(arranged_problems)

  return arranged_problems