K = int(input())
initial_rooms = list(map(int, input().split()))

# tourist_rooms = []
# i = 0
# while i < len(initial_rooms):
#     room = initial_rooms[i]
#     for number in range(i, len(initial_rooms)):
#         if i != number and room == initial_rooms[number] and initial_rooms[number] not in tourist_rooms:
#             tourist_rooms.append(initial_rooms[number])
#             break
#     i += 1
        
# captain_room = list(set (initial_rooms) ^ set(tourist_rooms))
# print(captain_room[0])

sum_k_rooms = sum(set(initial_rooms)) * K
sum_initial_rooms = sum(initial_rooms)

captain_room = (sum_k_rooms - sum_initial_rooms)//(K - 1)
print(captain_room)