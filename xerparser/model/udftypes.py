from xerparser.model.classes.udftypes import UDFType


class UDFTypes:

    def __init__(self):
        self.index = 0
        self._udftypes = []

    def add(self, params):
        self._udftypes.append(UDFType(params))

    def find_by_id(self, id) -> UDFType:
        obj = list(filter(lambda x: x.actv_code_type_id == id, self._udftypes))
        if len(obj) > 0:
            return obj[0]
        return obj

    @property
    def count(self):
        return len(self._udftypes)

    def __len__(self):
        return len(self._udftypes)

    def __iter__(self):
        return self

    def __next__(self) -> UDFType:
        if self.index >= len(self._udftypes):
            raise StopIteration
        idx = self.index
        self.index += 1
        return self._udftypes[idx]
