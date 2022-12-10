import httpagentparser


def _client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class UserAgentParser(object):
    def __init__(self, request):
        self._get_user_agent = request.META.get('HTTP_USER_AGENT')
        self.user_agent_parser = httpagentparser.simple_detect(self._get_user_agent)
        self.user_ip = _client_ip(request)

    @property
    def get_user_os(self):
        return self.user_agent_parser[0]

    @property
    def get_user_browser(self):
        return self.user_agent_parser[1]

    @property
    def get_user_ip(self):
        return self.user_ip
