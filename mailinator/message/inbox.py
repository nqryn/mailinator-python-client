from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List

from .message import Message


@dataclass_json
@dataclass
class Inbox(object):

    domain: str
    to: str
    msgs: List[Message]
