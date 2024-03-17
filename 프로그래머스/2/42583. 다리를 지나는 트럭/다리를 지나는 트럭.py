import sys
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    current_weight = 0

    while truck_weights or sum(bridge) > 0:
        answer += 1

        out = bridge.popleft()
        current_weight -= out

        if truck_weights:
            if current_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                current_weight += truck

            else:
                bridge.append(0)

    return answer


solution(2, 10, [7, 4, 5, 6])