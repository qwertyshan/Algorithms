# Write a function to find the rectangular intersection of two given rectangles.

rect1 = {
    # coordinates of bottom-left corner
    'x': 1,
    'y': 5,

    # width and height
    'width': 10,
    'height': 4,
}

rect2 = {
    # coordinates of bottom-left corner
    'x': 3,
    'y': 4,

    # width and height
    'width': 20,
    'height': 8,
}

def intersection(r1, r2):
    i = {}  # intersection rectangle
    scenario = 0

    i['x'] = max(r1['x'], r2['x'])
    i['y'] = max(r1['y'], r2['y'])

    if r1['x']<=r2['x']:
        i['width'] = r1['width']+r1['x']-i['x']
    else:
        i['width'] = r2['width']+r2['x']-i['x']

    if r1['y']>=r2['y']:
        scenario = 4
        i['height'] = r2['height']+r2['y']-i['y']
    else:
        scenario = 3
        i['height'] = r1['height']+r1['y']-i['y']

    if i['width'] <=0 or i['height'] <=0:
        return {'x':0,'y':0,'width':0,'height':0}
    else:
        return i

print intersection(rect1, rect2)