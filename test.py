import re

text = "2 Very long corridor to the room , only one lift per level , therefore quite a far walking distance to room . " \
       "2 The near street is loud but the windows have good noise insulation ."

text2 = "1 The near street is loud but the windows have good noise insulation ."
text3 = "The near street is loud but the windows have good noise insulation ."

regexp = re.compile('([12])')

#matches = regexp.match(text)
#matches = regexp.findall(text)

matches = regexp.split(text2)

print matches
