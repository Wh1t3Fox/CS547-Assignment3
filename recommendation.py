'''
Craig West
CS 54701
Assignment 3
'''
import argparse
import sys
import math
import numpy as np

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

#manhattan distance
def manhattan(v1, v2):
    distance = 0
    total = 0
    for key1,key2 in zip(v1,v2):
        if key1 != 0 and key2 != 0:
            distance += abs(key1 - key2)
            total += 1
    if total > 0:
        return distance / total
    else:
        return -1 #Indicates no ratings in common

#pearson coefficient
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
    if math.sqrt(sumxx*sumyy) == 0:
        return 0
    else:
        return sumxy/math.sqrt(sumxx*sumyy)

#cosine similarity
def cosine_similarity(v1, v2):
    assert len(v1) == len(v2) and len(v1) > 0
    sumxx, sumxy, sumyy = 0, 0, 0
    for x,y in zip(v1, v2):
        sumxx += x * x
        sumxy += x * y
        sumyy += y * y
    return sumxy/math.sqrt(sumxx*sumyy)

#prediction of a users non rated movies
def prediction(user, sim='cosine'):
    v1 = [x[1] for x in test[user] if x[1] != 0][:10]
    v1_avg = average(v1)
    numerator, denominator = 0, 0

    for movie, rating in test[user]:
        movie -= 1
        #we need to predict the rating
        if rating == 0:
            #calculate similar users
            similar_users = []
            for k, v in sorted(train.items()):
                #if the train user hasn't rated the value skip
                if int(v[movie]) == 0:
                    continue
                else:
                    #for the user get the first n movies
                    #the user has rated, n is defined by
                    #the number of movies rated by the test user
                    tmpv = []
                    for x in v:
                        if len(tmpv) == len(v1):
                            break
                        elif x != 0:
                            tmpv.append(x)

                    if sim == 'cosine':
                        similar_users.append((k, cosine_similarity(v1,tmpv)))
                    elif sim == 'pearson':
                        similar_users.append((k, pearson_coefficient(v1,tmpv)))
                    elif sim == 'manhattan':
                        similar_users.append((k, manhattan(v1,tmpv)))

            #sort the users by descreaing similarity
            similar_users.sort(key=lambda x: x[1],reverse=True)

            #Go through the similar users and calculate rating
            for u,r in similar_users[:20]:
                v2 = [x for x in train[u] if x != 0][:len(v1)]
                user_avg = average(v2)

                if sim == 'cosine':
                    similarity = cosine_similarity(v1,v2)
                elif sim == 'pearson':
                    similarity = pearson_coefficient(v1,v2)
                elif sim == 'manhattan':
                    similarity = manhattan(v1,tmpv)

                numerator += similarity * (train[u][movie] - user_avg)
                denominator += abs(similarity)

            if denominator == 0:
                value = int(round(v1_avg + (0)))
            else:
                value = int(round(v1_avg + (numerator/denominator)))

            if value < 1:
                value = 1
            elif value > 5:
                value = 5
            yield user + ' ' + str(movie+1) + ' ' + str(value)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True, help="the input test file")
    parser.add_argument("-o", "--output", required=False, help="the output test file")
    parser.add_argument("-v", "--verbose", action="store_true", help="enable verbose mode")
    args = parser.parse_args()

    #save training data
    with open('train.txt', 'r') as fr:
        for row, line in enumerate(fr):
            train[row+1] = [int(x) for x in line.translate(None, '\r\n\t')]

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

    #compute similar between all users
    for k in sorted(test):
        #results = prediction(str(k), 'cosine') #cosine similarity
        #results = prediction(str(k), 'pearson') #pearson coefficient
        results = prediction(str(k), 'manhattan') #pearson coefficient
        with open(output_file, 'a+') as fw:
            for rslt in results:
                fw.write(rslt)
                fw.write("\n")
                pretty_print(rslt)
