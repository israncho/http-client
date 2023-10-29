import socket
from sys import argv

def process_args() -> dict:
    assert len(argv) == 7, 'Not enough arguments'
    arguments = dict()
    arguments['host'] = argv[1]
    arguments['http_method'] = argv[2]
    arguments['url'] = argv[3]
    user_agent = int(argv[4])
    assert 1 <= user_agent and user_agent <= 3, 'Wrong user agent'
    arguments['user_agent'] = user_agent
    arguments['encoding'] = argv[5]
    arguments['connection'] = argv[6]
    return arguments


USER_AGENTS = ['Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0',
               'MyFakeBrowser/1.0 (FakeOS; Simulator 3.0)']


if __name__ == "__main__":
    print(process_args())
