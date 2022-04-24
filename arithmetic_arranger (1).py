def arithmetic_arranger(problems, result = False):

  line1 = ''
  line2 = ''
  line3 = ''
  line4 = ''
  if len(problems) > 5:
    return("Error: Too many problems.")
  for i in range(len(problems)):
    elements = problems[i].split()
    if elements[1] != '+' and elements[1] != '-':
      return("Error: Operator must be '+' or '-'.")
    else:
      try:
        operand1 = int(elements[0])
        operand2 = int(elements[2])
      except:
        return("Error: Numbers must only contain digits.")
    if len(elements[0]) > 4 or len(elements[2]) > 4:
      return("Error: Numbers cannot be more than four digits.")
  # All conditions are met
    first = elements[0]
    second = elements[2]
    sign = elements[1]
    diff = len(first) - len(second)
    bigger = max(len(first),len(second))
    
    if diff < 0:
      diff = diff * -1
      first = ' '*(diff) + first
    else:
      second = ' ' * diff + second
    
    line1 += ' '*2 + first + ' '*4
    line2 += sign + ' ' + second + ' '*4
    line3 += '-' * (bigger + 2) + ' '*4
    if sign == '+':
      resnum = str(int(first) + int(second))
    else:
      resnum = str(int(first) - int(second))
    if len(resnum) > bigger:
      line4 += ' ' + resnum + ' '*4
    else:
      line4 += '  ' + resnum + ' '*4

  arranged_problems = line1[ :len(line1) - 4] + '\n' + line2[:len(line2) - 4] + '\n' + line3[:len(line3)-4]
  if result :
    arranged_problems += '\n' + line4[:len(line4) - 4]
      
  return arranged_problems