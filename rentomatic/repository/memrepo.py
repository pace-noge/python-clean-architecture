from typing import Any

from rentomatic.domain.room import Room


class MemRepo:
    def __init__(self, data: [dict]) -> Any:
        self.data = data

    def list(self, filters=None) -> [Room]:
        result = [Room.from_dict(i) for i in self.data]

        if filters is None:
            return result

        if "code__eq" in filters:
            result = [r for r in result if r.code == filters["code__eq"]]

        if "price__eq" in filters:
            result = [r for r in result if r.price == filters["price__eq"]]

        if "price__lt" in filters:
            result = [r for r in result if r.price < int(filters["price__lt"])]

        if "price__gt" in filters:
            result = [r for r in result if r.price > int(filters["price__gt"])]

        return result
