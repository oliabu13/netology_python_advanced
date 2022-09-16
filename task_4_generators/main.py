import itertools


class FlatIterator:
	def __init__(self, lists):
		self.list = iter(itertools.chain(*lists))

	def __iter__(self):
		return self

	def __next__(self):
		return next(self.list)


def flat_generator(lists):
	for element in FlatIterator(lists):
		if isinstance(element, list):
			yield from flat_generator(element)
		else:
			yield element


if __name__ == '__main__':
	nested_list = [
		['a', 'b', 'c'],
		['d', 'e', 'f', 'h', False],
		[1, 2, None],
	]

	for item in FlatIterator(nested_list):
		print(item)

	flat_list = [item for item in flat_generator(nested_list)]
	print(flat_list)
