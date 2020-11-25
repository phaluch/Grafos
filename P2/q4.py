def read_map():
    y, x = [int(x) for x in input().split()]
    chart = [[value for value in input()] for _ in range(y)]
    return x,y,chart

x,y,chart = read_map()
coast = {}
for x_pos in range(x):
    for y_pos in range(y):
        if chart[y_pos][x_pos] == '.':
            continue
        for x_displacement in [-1,1]:
            if x_pos+x_displacement in range(x):
                if (y_pos,x_pos) in coast.keys():
                    continue
                if chart[y_pos][x_pos+x_displacement] == '.':
                    #print(f'({y_pos},{x_pos}) água com ({y_pos},{x_pos+x_displacement})')
                    coast[(y_pos,x_pos)] = 'C'
                    continue
            else:
                #print(f'({y_pos},{x_pos}) na borda')
                coast[(y_pos,x_pos)] = 'C'
        for y_displacement in [-1,1]:
            if y_pos+y_displacement in range(y):
                if (y_pos,x_pos) in coast.keys():
                    continue
                if chart[y_pos+y_displacement][x_pos] == '.':
                    #print(f'({y_pos},{x_pos}) água com ({y_pos+y_displacement},{x_pos})')
                    coast[(y_pos,x_pos)] = 'C'
                    continue
            else:
                #print(f'({y_pos},{x_pos}) na borda')
                coast[(y_pos,x_pos)] = 'C'

print(len(coast))