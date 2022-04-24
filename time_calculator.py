def add_time(start, duration, day = None):

  pos1 = start.find(':')
  pos2 = duration.find(':')
  pos = start.find(' ')
  days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

  nm = int(start[pos1+1:pos]) + int(duration[pos2+1:])
  nh = int(start[:pos1]) + int(duration[:pos2]) 
  if 'PM' in start:
    nh += 12
  if nm >= 60:
    nh += int(nm / 60)
    nm = nm % 60
  if nm < 10:
    new_time = ':0' + str(nm) + ' '
  else:
    new_time = ':' + str(nm) + ' '
  #the minutes are done and in the return string
  if nh % 24 >= 12:
    new_time += 'PM'
    if nh % 12 == 0:
      new_time = '12' + new_time
    else:
      new_time = str(nh % 12) + new_time
  else:
    new_time += 'AM'
    if nh % 12 == 0:
      new_time = '12' + new_time
    else:
      new_time = str(nh % 12) + new_time
  #hours and AM/PM are done
  if day != None:
    for i in range(len(days)):
      if day.lower() == days[i].lower():
        if nh >= 24:
          j = (i + int(nh / 24)) % len(days)
          if j == len(days):
            j = 0
        else:
          j = i
        new_time += ', ' + days[j]
  
  if int(nh / 24) != 0:
    if int(nh / 24) == 1:
      new_time += ' (next day)'
    else:
      new_time += ' (' + str(int(nh/24)) + ' days later)'
  
  return new_time
