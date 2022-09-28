class MaxHeap:
    def __init__(self):
        self.heap = []
        self.heap.append(0)

    def size(self) -> int:
        return len(self.heap) - 1

    def isEmpty(self) -> bool:
        return self.size() == 0

    def parent(self, i):
        return self.heap[i // 2]

    def left(self, i):
        return self.heap[i * 2]

    def right(self, i):
        return self.heap[i * 2 + 1]

    def display(self, msg='heap tree'):
        print(msg, self.heap[1:])

    def insert(self, node):
        self.heap.append(node)  # 제일 마지막 노드에 삽입함
        index = self.size()  # 제일 마지막 노드의 index를 알아내기 위해서 size()함수를 이용함

        while (index != 1 and node > self.parent(index)):  # index가 root 보다는 크고 부모 노드보다 큰값을 가질때 까지만 사용함.
            self.heap[index] = self.parent(index)  # 다운 힙을 하기 위해서 부모노드에 삽입함.
            index = index // 2  # 인덱스를 반으로 나눠서 올린다.
        self.heap[index] = node  # 마지막에 값을 삽입한다.

    def delete(self):

        parent = 1  # 최상위로 부모를 설정함
        child = 2  # 자식을 좌측자식으로 설정함

        if not self.isEmpty():  # heap이 비어있지 않다면

            hroot = self.heap[1]  # 제일 위에 있는 것이 heap의 root이다 반환을 위해서 미리 저장함
            last = self.heap[self.size()]  # 마지막 원소를 지정함

            while (child <= self.size()):  # 자식의 인덱스가 마지막 인덱스보다 작을 때까지 반보감

                if child < self.size() and self.left(parent) < self.right(parent):  # 만약 왼쪽 자식이 크다면
                    child += 1
                if last >= self.heap[child]:  # 마지막 node보다 작은 자식을 발견한다면
                    break

                self.heap[parent] = self.heap[child]  # 부모와 자식의 위치를 바꿈
                parent = child  # 부모와 자식의 인덱스를 바꿔서
                child *= 2  # 자시삭 인덱스를 직접접으로 늘린다.

        self.heap[parent] = last
        self.heap.pop(-1)
        return hroot


def heapify(arr, arrlen, i):
    largest = i
    left = i * 2 + 1  # 원래 힙을 사용한것이 아니고 리스트를 사용했기 때문에 인덱스0번을 사용해서 왼쪽 자식이 i*2 +1이다
    right = i * 2 + 2  # 인덱스 0 번을 사용한 list에서의 오른쪽 자식의 인덱스

    if left < arrlen and arr[i] < arr[left]: largest = left  # 왼쪽 자식이 더 크다면
    if right < arrlen and arr[largest] < arr[right]: largest = right  # 오른쪽 자식이 더 크다면

    if largest != i:  # 위의 if 문장이 실행되었다면
        tmp = arr[i]  # 부모와 자식간의 위치를 바꾼다.
        arr[i] = arr[largest]
        arr[largest] = tmp
        print(arr)
        heapify(arr, arrlen, largest)  # 더 밑의 트리에서도 조건에 부합해야 하기 때문에 더 밑에 순환호출을 이용해서
        # 자식을 최값으로 잡고 다시 호출한다.


lista = [0, 3, 8, 5, 22, 7, 4, 8, 48, 5, 21, 6, 31]

for i in range((len(lista) // 2), -1, -1):
    heapify(lista, len(lista), i)
print(lista)

max = MaxHeap()
for i in lista:
    max.insert(i)
print(max.heap)

listb = [9, 4, 8, 3, 7, 19, 35, 136, 6, 17]


def build_max_heap(list_heap):
    heap_size = len(list_heap)
    for i in range((len(list_heap) // 2), -1, -1):
        print(list_heap)
        heapify(list_heap, len(list_heap), i)


def heapSort(list):
    build_max_heap(list)
    for i in range(len(list)-1,0,-1):
        tmp = list[0]
        list[0] = list[i]
        list[i] = tmp
        heapify(list,len(list)-(len(list)-i),0)
        print(list)
print("==================================================")
heapSort(listb)