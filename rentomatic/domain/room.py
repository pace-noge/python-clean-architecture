import uuid
import dataclasses


@dataclasses.dataclass
class Room:
    code: uuid.UUID
    size: int
    price: int
    longitude: float
    latitude: float

    @classmethod
    def from_dict(cls, d: dict):
        return cls(**d)

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)
