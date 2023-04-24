# клас для представлення графа
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # кількість вершин у графі
        self.graph = []    # зберігає зв'язки між вершинами графа

    # функція для додавання зв'язку між вершинами графа
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # функція для знаходження представника множини
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # функція для об'єднання двох множин
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # прикріплення меншої гілки до більшої гілки
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        # якщо ранк однаковий, то можна прикріплювати до будь-якої гілки
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # функція для виконання алгоритму Крускала
    def kruskal(self):
        result = []         # зберігає кінцевий мінімальний остов графа
        i = 0               # індекс для проходження по всіх зв'язках графа
        e = 0               # індекс для зберігання мінімального остову

        # сортування всіх зв'язків у порядку зростання ваги
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        # створення підмножин для кожної вершини графа
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # проходження по всіх зв'язках графа, починаючи з мінімального
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # перевірка чи не створить цей зв'язок цикл в графі
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

                # виведення мінімального остову
            print("Мінімальний остов графа:")
            for u, v, weight in result:
                print(f"{u} - {v}: {weight}")



distance = [0, 3, 0, 0, 0, 34, 0, 80,
            3, 0, 0, 1, 0, 0, 0, 68,
            0, 0, 0, 0, 23, 0, 12, 0,
            0, 1, 0, 0, 53, 0, 0, 39,
            0, 0, 23, 53, 0, 0, 6, 14,
            34, 0, 0, 0, 0, 0, 0, 25,
            0, 0, 12, 0, 68, 0, 0, 99,
            80, 68, 0, 39, 14, 25, 99, 0]


g = Graph(8)
for i in range(8):
    for j in range(8):
        if distance[i*8+j] != 0:
            g.add_edge(i, j, distance[i*8+j])

g.kruskal()




