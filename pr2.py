


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        self._bubble_up(len(self.heap) - 1)

    def extract_min(self):
        if self.is_empty():
            raise Exception("Heap is empty")
        if len(self.heap) == 1:
            return self.heap.pop()
        min_item = self.heap[0]
        self.heap[0] = self.heap.pop()  # Заменяем корень последним элементом
        self._bubble_down(0)
        return min_item

    def decrease_key(self, index, new_value):
        if index < 0 or index >= len(self.heap):
            raise IndexError("Index out of bounds")
        if new_value > self.heap[index][0]:
            raise ValueError("New value is greater than current value")
        self.heap[index] = (new_value[0], self.heap[index][1])  # Обновляем значение
        self._bubble_up(index)

    def is_empty(self):
        return len(self.heap) == 0

    def _bubble_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index][0] < self.heap[parent_index][0]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _bubble_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            if left_child_index < len(self.heap) and self.heap[left_child_index][0] < self.heap[smallest][0]:
                smallest = left_child_index
            if right_child_index < len(self.heap) and self.heap[right_child_index][0] < self.heap[smallest][0]:
                smallest = right_child_index

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break


def dijkstra(graph, start_vertex):
    min_heap = MinHeap()
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_vertex] = 0
    min_heap.insert((0, start_vertex))

    while not min_heap.is_empty():
        current_distance, current_vertex = min_heap.extract_min()

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                min_heap.insert((distance, neighbor))

    return distances


# Пример использования
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

distances = dijkstra(graph, 'A')
print(distances)