class BinarySearch(list):
    def __init__(self, a, b):
        self.a = a
        self.b = b

        for i in range(1, a + 1):
            self.append(i * b)

        self.length = len(self)

    def search(self, search_item):
        self.sort()

        beginning = 0
        end = len(self) - 1

        count = 0

        while beginning <= end:
            middle = (end + beginning) // 2
            value = self[middle]
            if value == search_item:
                return {'count': count, 'index': self.index(value)}

            elif self[end] == search_item:
                return {'count': count, 'index': end}

            elif self[beginning] == search_item:
                return {'count': count, 'index': beginning}

            elif middle == beginning or middle == beginning:
                return {'count': count, 'index': -1}


            elif value > search_item:
                end = middle - 1

            elif value < search_item:
                beginning = middle + 1

            count += 1
