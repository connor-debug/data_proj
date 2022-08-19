import math

data = [i.strip('\n').split('\t') for i in open('Data.txt')]

sums = [0] * 5

for i in data[1:]:
    sums[0] = int(i[1]) + sums[0]

for i in data[1:]:
    sums[1] = int(i[2]) + sums[1]

for i in data[1:]:
    sums[2] = int(i[3]) + sums[2]

for i in data[1:]:
    sums[3] = int(i[4]) + sums[3]

for i in data[1:]:
    sums[4] = int(i[5]) + sums[4]

def entropyAZ( len, text ):
    AZ_sum = 0
    for i in data[33:59]:
        AZ_sum = int(i[text]) + AZ_sum
    prob_az = (AZ_sum/sums[text-1])*len
    prob_az_log = math.log((AZ_sum/sums[text-1])*len,2)
    print(-prob_az_log * prob_az, end = ' | ')

def entropyAZaz( len, text ):
    AZ_sum = 0
    for i in data[33:59]:
        AZ_sum = int(i[text]) + AZ_sum
    for i in data[65:91]:
        AZ_sum = int(i[text]) + AZ_sum
    prob_az = (AZ_sum/sums[text-1])*len
    prob_az_log = math.log((AZ_sum/sums[text-1])*len,2)
    print(prob_az_log * prob_az, end = ' | ')

def entropyAZaz09( len, text ):
    AZ_sum = 0
    for i in data[33:59]:
        AZ_sum = int(i[text]) + AZ_sum
    for i in data[65:91]:
        AZ_sum = int(i[text]) + AZ_sum
    for i in data[16:26]:
        AZ_sum = int(i[text]) + AZ_sum
    prob_az = (AZ_sum/sums[text-1])*len
    prob_az_log = math.log((AZ_sum/sums[text-1])*len,2)
    print(prob_az_log * prob_az, end = ' | ')


entropyAZ(3,1)
entropyAZ(3,2)
entropyAZ(3,3)
entropyAZ(3,4)
entropyAZ(3,5)
print()

entropyAZaz(3,1)
entropyAZaz(3,2)
entropyAZaz(3,3)
entropyAZaz(3,4)
entropyAZaz(3,5)
print()

entropyAZaz09(3,1)
entropyAZaz09(3,2)
entropyAZaz09(3,3)
entropyAZaz09(3,4)
entropyAZaz09(3,5)
print()