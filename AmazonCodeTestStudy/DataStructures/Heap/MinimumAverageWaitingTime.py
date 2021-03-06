"""
Minimum Average Waiting Time
https://www.hackerrank.com/challenges/minimum-average-waiting-time/problem?h_r=next-challenge&h_v=zen
Tieu owns a pizza restaurant and he manages it in his own way. While in a normal restaurant, a customer is served by following the first-come, first-served rule, Tieu simply minimizes the average waiting time of his customers. So he gets to decide who is served first, regardless of how sooner or later a person comes.

Different kinds of pizzas take different amounts of time to cook. Also, once he starts cooking a pizza, he cannot cook another pizza until the first pizza is completely cooked. Let's say we have three customers who come at time t=0, t=1, & t=2 respectively, and the time needed to cook their pizzas is 3, 9, & 6 respectively. If Tieu applies first-come, first-served rule, then the waiting time of three customers is 3, 11, & 16 respectively. The average waiting time in this case is (3 + 11 + 16) / 3 = 10. This is not an optimized solution. After serving the first customer at time t=3, Tieu can choose to serve the third customer. In that case, the waiting time will be 3, 7, & 17 respectively. Hence the average waiting time is (3 + 7 + 17) / 3 = 9.

Help Tieu achieve the minimum average waiting time. For the sake of simplicity, just find the integer part of the minimum average waiting time.

Input Format

The first line contains an integer N, which is the number of customers.
In the next N lines, the ith line contains two space separated numbers Ti and Li. Ti is the time when ith customer order a pizza, and Li is the time required to cook that pizza.

The  customer is not the customer arriving at the  arrival time.

Output Format

Display the integer part of the minimum average waiting time.
Constraints

1 ≤ N ≤ 105
0 ≤ Ti ≤ 109
1 ≤ Li ≤ 109
Note

The waiting time is calculated as the difference between the time a customer orders pizza (the time at which they enter the shop) and the time she is served.

Cook does not know about the future orders.

Sample Input #00

3
0 3
1 9
2 6
Sample Output #00

9
Sample Input #01

3
0 3
1 9
2 5
Sample Output #01

8
Explanation #01

Let's call the person ordering at time = 0 as A, time = 1 as B and time = 2 as C. By delivering pizza for A, C and B we get the minimum average wait time to be

(3 + 6 + 16)/3 = 25/3 = 8.33 
the integer part is 8 and hence the answer.

"""

#!/bin/python3

import os
import sys

from heapq import heappush, heappop

def minimumAverage(customers):
    customers.sort()
    queue = []
    time_waiting = 0
    current_time = 0
    N = len(customers)

    while customers or queue:
        while customers and customers[0][0] <= current_time:
            heappush(queue, customers.pop(0)[::-1])
        if queue:
            current_task = heappop(queue)
            current_time += current_task[0]
            time_waiting += current_time - current_task[1]
        else:
            heappush(queue, customers.pop(0)[::-1])
            current_time = queue[0][1]

    return time_waiting // N


customers = [[0, 3], [1, 9], [2, 6]]
print(minimumAverage(customers)) #9

customers = [[0, 3], [1, 9], [2, 5]]
print(minimumAverage(customers)) #8

customers = [[934504950, 861289137],[682111322, 496887795],[603236774, 713893904],[871832073, 264986656],[9361848, 539221796],[923314579, 687524372],[516631496, 436533893],[762108851, 407784436],[409617807, 615448498],[222634400, 208442731],[431098638, 148834388],[858636239, 742132465],[65595465, 104576384],[27592708, 611298565],[68765513, 26367219],[201384166, 114673012],[7863143, 797762645],[543771279, 29132945],[29130952, 854671993],[585445692, 593951356],[692134770, 533881497],[891653076, 49240670],[174260196, 913929115],[66288118, 194879400],[487706, 119659344],[194435589, 429754201],[4080371, 967838129],[793446473, 9878839],[701794212, 68187682],[628896716, 302869266],[333961924, 324019889],[757782965, 264845318],[753067776, 450723670],[986021138, 205616567],[180047190, 52602162],[175679615, 308585876],[22888493, 142102482],[704380635, 733794326],[271062208, 578646122],[773379847, 193003008],[678995092, 976381723],[336906181, 900464030],[239697689, 835175471],[676537797, 206323720],[946885385, 254902618],[254065061, 694451805],[786166049, 329338105],[70498307, 874368266],[775661614, 254369620],[948249666, 853779203]]
print(minimumAverage(customers)) #6667863382

stop = True

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input())

#     customers = []

#     for _ in range(n):
#         customers.append(list(map(int, input().rstrip().split())))

#     result = minimumAverage(customers)

#     fptr.write(str(result) + '\n')

#     fptr.close()



