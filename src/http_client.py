import socket
from sys import argv


HTTP_M = ['GET', 'HEAD']
CONNECT = ['keep-alive', 'close', 'upgrade']
ENCODING = ['gzip', 'deflate', 'identity']


def process_args() -> dict:
    assert len(argv) == 7, 'Not enough arguments'
    arguments = dict()
    arguments['host_server'] = argv[1]

    assert argv[2] in HTTP_M, error_msg(argv[2], HTTP_M)
    arguments['http_method'] = argv[2]

    arguments['url'] = argv[3]

    user_a = int(argv[4])
    assert 1 <= user_a and user_a <= 3, error_msg(argv[4], [1, 2, 3])
    arguments['user_a'] = user_a

    assert argv[5] in ENCODING, error_msg(argv[5], ENCODING)
    arguments['encoding'] = argv[5]

    assert argv[6] in CONNECT, error_msg(argv[6], CONNECT)
    arguments['connection'] = argv[6]

    return arguments


def error_msg(usr_input: str, options: list) -> str:
    return '\'' + usr_input + '\' invalid or unavailable argument option,' \
        + ' try with one of the following options: ' + str(options)

USER_AGENTS = ['Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0',
               'MyFakeBrowser/1.0 (FakeOS; Simulator 3.0)']


def construct_http_request(args: dict) -> bytes:
    request_line =  args['http_method'] + ' ' + \
                    args['url'] + ' HTTP/1.1\r\n'

    header_lines =  'Host: ' + args['host_server'] + '\r\n' + \
                    'User-Agent: ' + USER_AGENTS[args['user_a'] - 1] + '\r\n' + \
                    'Accept: text/html, application/xhtml+xml,' + \
                    'application/xml;q=0.9, */*;q=0.8\r\n' + \
                    'Accept-Charset: utf-8\r\n' + \
                    'Connection: ' + args['connection'] + '\r\n' + \
                    'Accept-Encoding: ' + args['encoding'] + '\r\n' + \
                    'Accept-Language: en-US\r\n'

    http_request = request_line + header_lines + '\r\n'
    return http_request.encode('utf-8')


def tcp_connection(host_server: str, http_request: bytes) -> None:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        print('Starting connection.')
        s.connect((host_server, 80))
        s.send(http_request)
        response = b''

        while True:
            data = s.recv(1024)
            if not data: break
            response += data

        print('Server response:\n----------------------------------------')
        print(response.decode('utf-8'))
        print('----------------------------------------')
        print('Connection to the server finished.\n')

    except Exception as e:
        print(f"Error: {e}")
        print('Connection failed.')



if __name__ == "__main__":
    arguments = None
    try:
        arguments = process_args()
    except Exception as e:
        print(e)
        exit()

    print('python3', end=' ')
    for e in argv:
        print(e, end=' ')
    print()
    http_request = construct_http_request(arguments)
    tcp_connection(arguments['host_server'], http_request)
