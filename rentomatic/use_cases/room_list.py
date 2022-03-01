from typing import Union

from rentomatic.responses import (
    ResponseSuccess,
    ResponseFailure,
    ResponseTypes,
    build_response_from_invalid_request
)
from rentomatic.requests.room_list import RoomListValidRequest, RoomListInvalidRequest
from rentomatic.repository.memrepo import MemRepo


def room_list_use_case(repo: MemRepo, request: Union[RoomListValidRequest, RoomListInvalidRequest]):
    if not request:
        return build_response_from_invalid_request(request)
    try:
        rooms = repo.list(filters=request.filters)
        return ResponseSuccess(rooms)
    except Exception as exc:
        return ResponseFailure(ResponseTypes.SYSTEM_ERROR, exc)
