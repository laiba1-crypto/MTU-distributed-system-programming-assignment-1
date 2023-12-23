import copy
class Document:
    def __init__(self):
        self.data = [[1, 2, 3], [4, 5, 6]]

    def clone(self):
        return copy.copy(self)

    def deep_clone(self):
        return copy.deepcopy(self)

    def set_data(self, data):
        self.data = data

    def __str__(self):
        return str(self.data)

original_document = Document()

copy1 = original_document.clone()
copy1.set_data([[1, 2, 3], [4, 5, 15]])

copy2 = original_document.deep_clone()
copy2.set_data([[1, 2, 3], [9, 10, 11]])

copy3 = original_document.clone()
copy3.set_data([[1, 2, 3], ['456', 7, 15, 16]])

copy4 = original_document.deep_clone()
copy4.set_data([[1, 2, 3], ["789", 7, 15, 16]])

print("name=Original list=", original_document)
print(" ")

print("name=Copy 1 list=", copy1)
print("name=Original list=", copy1)
print(" ")

print("name=Copy 2 list=", copy2)
print("name=Original list=", copy1)

print(" ")
print("name=Copy 3 list=", copy3)
print("name=Original list=", copy3)
print(" ")

print("name=Copy 4 list=", copy4)
print("name=Original list=", copy3)
