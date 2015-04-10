'''
Craig West
CS 54701
Assignment 3
'''
import argparse
import sys
import math

COLORS = {
    'PURPLE' : '\033[95m',
    'BLUE' : '\033[94m',
    'GREEN' : '\033[92m',
    'YELLOW' : '\033[93m',
    'RED' : '\033[91m',
    'BOLD' : '\033[1m',
    'UNDERLINE' : '\033[4m',
    'ENDC' : '\033[0m'
}

train = {}
test = {}
output_file = None


average = lambda x: float(sum(x))/len(x)

def pretty_print(message, color='GREEN'):
    if color.upper() in COLORS:
        print '{0}[+] {1}{2}'.format(COLORS[color.upper()], message, COLORS['ENDC'])
    else:
        print '{0}[-] ERROR: {1} is not in the color list!{2}'.format(COLORS['RED'], color, COLORS['ENDC'])

def pearson_coefficient(v1, v2):
    assert len(v1) == len(v2) and len(v1) > 0
    sumxx, sumyy, sumxy = 0, 0, 0
    x_avg, y_avg = average(v1), average(v2)
    for x,y in zip(v1, v2):
        x = x - x_avg
        y = y - y_avg
        sumxy += x * y
        sumxx += x * x
        sumyy += y * y
    return sumxy/math.sqrt(sumxx*sumyy)

def cosine_similarity(v1, v2):
    assert len(v1) == len(v2) and len(v1) > 0
    sumxx, sumxy, sumyy = 0, 0, 0
    for x,y in zip(v1, v2):
        sumxx += x * x
        sumxy += x * y
        sumyy += y * y
    return sumxy/math.sqrt(sumxx*sumyy)

def prediction(user, item, sim='cosine'):
    numerator, denominator = 0, 0
    v1 = [x[1] for x in user if x[1] != 0]
    v2 = [v[item-1] for v in train.values() if v[item-1] != 0][:5]
    print v2
    for entry in train:
        if train[entry][item-1] == 0:
            continue
        user_avg = average(train[entry])
        if sim == 'cosine':
            numerator += cosine_similarity(v1,v2) * (train[entry][item-1] - user_avg)
            denominator += abs(cosine_similarity(v1,v2))
        else:
            numerator += pearson_coefficient(v1,v2) * (train[entry][item-1] - user_avg)
            denominator += abs(pearson_coefficient(v1,v2))

    return average(v1) + (numerator/denominator)




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True, help="the input test file")
    parser.add_argument("-o", "--output", required=False, help="the output test file")
    parser.add_argument("-v", "--verbose", action="store_true", help="enable verbose mode")
    args = parser.parse_args()

    #save training data
    with open('train.txt', 'r') as fr:
        for row, line in enumerate(fr):
            train[row] = [int(x) for x in line.translate(None, '\r\n\t')]

    #store users ratings
    with open(args.input, 'r') as fr:
        if args.output:
            output_file = args.output
        else:
            output_file = args.input.replace('test', 'result')

        for line in fr:
            user, movie, score = line.split(' ')
            try:
                test[user] += [(int(movie), int(score))]
            except KeyError:
                test[user] = [(int(movie), int(score))]

    #compute similarity
    pretty_print(prediction(test['201'], 237))
    #pretty_print(cosine_similarity(train[1], train[2]))
