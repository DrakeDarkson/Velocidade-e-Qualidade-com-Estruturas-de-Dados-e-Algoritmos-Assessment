def selection_sort(players):
    n = len(players)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if players[j]['score'] < players[min_index]['score']:
                min_index = j
        players[i], players[min_index] = players[min_index], players[i]

players = [
    {"name": "Alice", "score": 350},
    {"name": "Bob", "score": 120},
    {"name": "Charlie", "score": 470},
    {"name": "Diana", "score": 200}
]

selection_sort(players)
print(players)
