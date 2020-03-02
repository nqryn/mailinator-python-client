from abc import ABC, abstractmethod
from requests import Session


class ResourceInterface(ABC):

	@abstractmethod
	def execute(self, session: Session):
		pass


class MailinatorClient(object):

	def __init__(self, api_token: str):
		s = Session()
		s.headers.update({
			'Authorization': api_token,
			'Content-Type': 'application/json',
		})
		self.session = s

	def request(self, resource: ResourceInterface):
		return resource.execute(self.session)
