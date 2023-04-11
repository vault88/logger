from logger2 import logger
import types


class FlatIterator:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.list = []
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= len(self.list_of_lists):
            if self.list:
                self.list_of_lists, self.counter = self.list.pop()
                return next(self)
            else:
                raise StopIteration

        item = self.list_of_lists[self.counter]
        self.counter += 1

        if type(item) is not list:
            return item
        else:
            self.list.append((self.list_of_lists, self.counter))
            self.list_of_lists = item
            self.counter = 0
            return next(self)


def test_1():

    list_of_lists_1 = [["a", "b", "c"], ["d", "e", "f", "h", False], [1, 2, None]]

    for flat_iterator_item, check_item in zip(
        FlatIterator(list_of_lists_1),
        ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None],
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "h",
        False,
        1,
        2,
        None,
    ]


if __name__ == "__main__":
    test_1()


@logger("task_3_log")
def flat_generator(list_of_lists):
    for item in list_of_lists:
        if type(item) is not list:
            yield item
        else:
            yield from flat_generator(item)


def test_2():
    list_of_lists_1 = [["a", "b", "c"], ["d", "e", "f", "h", False], [1, 2, None]]
    for flat_iterator_item, check_item in zip(
        flat_generator(list_of_lists_1),
        ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None],
    ):
        assert flat_iterator_item == check_item
    assert list(flat_generator(list_of_lists_1)) == [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "h",
        False,
        1,
        2,
        None,
    ]
    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == "__main__":
    test_2()
