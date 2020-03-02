from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from typing import List, Dict, Any

from mailinator.rule import Rule
from .part import Part


@dataclass_json
@dataclass
class Message(object):
    from_full: str = field(metadata=config(field_name='fromfull'))
    headers: Dict[str, Any]
    subject: str
    parts: List[Part]
    msg_from: str = field(metadata=config(field_name='from'))
    to: str
    msg_id: str = field(metadata=config(field_name='id'))
    time: int
    seconds_ago: int
    domain: str
    orig_from: str = field(metadata=config(field_name='origfrom'))
    mrid: str
    size: int
    stream: str
    msg_type: str
    source: str
    text: str


@dataclass_json
@dataclass
class DeletedMessages(object):
    status: str
    count: int


@dataclass_json
@dataclass
class MessageToPost(object):
    subject: str
    msg_from: str = field(metadata=config(field_name='from'))
    text: str


@dataclass_json
@dataclass
class PostedMessage(object):
    status: str
    id: str
    rules_fired: List[Rule]
