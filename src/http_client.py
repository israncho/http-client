import socket
from sys import argv


HTTP_M = ['GET', 'HEAD']
CONNECT = ['keep-alive', 'close', 'upgrade']
ENCODING = ['gzip', 'deflate', 'identity']


def process_args() -> dict:
    assert len(argv) == 7, 'Not enough arguments'
    arguments = dict()
    arguments['host_server'] = argv[1]

    assert argv[2] in HTTP_M, 'unavailable HTTP method, try: ' + str(HTTP_M)
    arguments['http_method'] = argv[2]

    arguments['url'] = argv[3]

    user_a = int(argv[4])
    assert 1 <= user_a and user_a <= 3, 'Wrong user agent'
    arguments['user_a'] = user_a

    assert argv[5] in ENCODING, 'unavailable encoding, try:' + str(ENCODING)
    arguments['encoding'] = argv[5]

    assert argv[6] in CONNECT, 'unavailable connection arg, try:' + str(CONNECT)
    arguments['connection'] = argv[6]

    return arguments


USER_AGENTS = ['Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0',
               'MyFakeBrowser/1.0 (FakeOS; Simulator 3.0)']


def construct_http_request(args: dict) -> str:
    request_line =  args['http_method'] + ' ' + \
                    args['url'] + ' HTTP/1.1\r\n'

    header_lines =  'Host: ' + args['host_server'] + '\r\n' + \
                    'User-Agent: ' + USER_AGENTS[args['user_a']] + '\r\n' + \
                    'Accept: text/html, application/xhtml+xml,' + \
                    'application/xml;q=0.9, */*;q=0.8\r\n' + \
                    'Accept-Charset: utf-8\r\n' + \
                    'Connection: ' + args['connection'] + '\r\n' + \
                    'Accept-Encoding: ' + args['encoding'] + '\r\n' + \
                    'Accept-Languaje: en-US\r\n'

    return request_line + header_lines + '\r\n'


if __name__ == "__main__":
    print(construct_http_request(process_args()).encode())
