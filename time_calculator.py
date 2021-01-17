def add_time(start, duration, day = ""):

  days = {0:'monday', 1:'tuesday', 2:'wednesday', 3:'thursday', 4:'friday', 5:'saturday', 6:'sunday'}
  start = start.split()
  time = start[0].split(':')
  duration = duration.split(':')
  min = int(time[1]) + int(duration[1])
  carry = 0
  
  if min>60:
    carry = int(min/60)
    min = min%60

  if(len(str(min)))<2:
    min = str(min)
    min = '0' + min

  hour = int(time[0]) + int(duration[0]) + carry
  h1 = hour%12
  h2 = int(hour/12)
  d1 = int(h2/2)
  if h2%2:
    if start[1] == 'PM':
      start[1] = 'AM'
      d1 = d1 + 1
    else:
      start[1] = 'PM'
  
  if h1==0:
    h1 = 12
  new_time = str(h1) + ":" + str(min) + " " + start[1]

  if len(day):
    day = day.lower()
    next_day = 0
    for k,v in days.items():
      if v==day:
        next_day = k + d1
        next_day = next_day%7
    
    days[next_day] = days[next_day][0].upper() + days[next_day][1:]
    new_time = str(h1) + ":" + str(min) + " " + start[1] + ", " + days[next_day]
    
  if d1 == 1:
    new_time = new_time + ' (next day)'
  elif d1>1:
    new_time = new_time + ' (' + str(d1) + ' days later)'

  return new_time