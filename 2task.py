N = 5
participants = list(range(1,N+1))
print(participants)
k = 10
count_out = 0
for _ in range(N - 1):
    start_count = count_out % len(participants)
    count_out = (start_count + k - 1) % len(participants)
    participants.pop(count_out)
print(participants)
