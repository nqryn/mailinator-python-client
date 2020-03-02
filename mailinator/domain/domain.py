from dataclasses import dataclass
from dataclasses_json import dataclass_json
from enum import Enum
from typing import List

from mailinator.rule import Rule


class DomainType(Enum):
	PRIVATE = 'PRIVATE'
	PUBLIC = 'PUBLIC'


@dataclass_json
@dataclass
class Domain(object):
	_id: str
	description: str
	enabled: bool
	name: str
	ownerid: str
	rules: List[Rule]
