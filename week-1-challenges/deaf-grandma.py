import fileinput

print('HEY KID!')
goodbye = False
sleepyGrandma = 0

for line in fileinput.input():
  text = line.rstrip()
  sleepyGrandma += 1

  if sleepyGrandma > 9:
    print('> TOO MANY QUESTIONS! I GOTTA GO WATCH MY TV SHOW! LATER, SKATER!')
    break
  
  if text == '':
    print('> WHAT?!')
    continue

  if text == 'GOODBYE!':
    if goodbye:
      print('> LATER, SKATER!')
      break
    else:
      print('> LEAVING SO SOON?')
      goodbye = True
      continue
  
  if any(c for c in text if c.islower()):
    print('> SPEAK UP, KID!')
  else:
    print('> NO, NOT SINCE 1946!')
  continue