************************
mailinator-python-client
************************


Python Client for the Mailinator Email System https://www.mailinator.com

Usage:

0. Creating a client::

    from mailinator.client import MailinatorClient
    client = MailinatorClient('token here')


1. Getting all domains::

    from mailinator.domain.interface import DomainsInterface

    domains_interface = DomainsInterface()
    domains = client.request(domains_interface)
    for d in domains:
        print(d)


2. Get a single domain (by id)::

    from mailinator.domain.interface import DomainInterface
    
    domain_interface = DomainInterface(domain_id='hello.m8r.co')
    domain = client.request(domain_interface)

3. Get an inbox::

    from mailinator.message.interface import InboxInterface

    inbox_interface = InboxInterface(domain_id='hello.m8r.co', inbox_id='test')
    inbox = client.request(inbox_interface)

    for msg in inbox.msgs:
        print(msg)

