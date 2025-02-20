class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self._iter_index = 0  #tracking the  iteration state

    def __iter__(self):
        # Reset the iteration index- to handle iterations
        self._iter_index = 0
        return self

    def __next__(self):
        if self._iter_index == 0:
            self._iter_index += 1
            return {'length': self.length}
        elif self._iter_index == 1:
            self._iter_index += 1
            return {'width': self.width}
        else:
            raise StopIteration  # Stop iteration after producing length and width

# Example 
rectangle = Rectangle(10, 5)

# Iterating over the Rectangle instance
for dimension in rectangle:
    print(dimension)