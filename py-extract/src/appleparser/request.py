import time
from appleparser import log
from requests import Session


class RequestError(Exception): pass


class Request:
    def __init__(self, **kwargs):
        log.info("Init Requests")
        self.__session = Session()

    def try_request(self, method: str, url: str, sleep=2, retry=0, json=True, provider=None):
        res = self.__session.request(method, url)
        try:
            res.raise_for_status()
            if json:
                content = res.json()
            else:
                content = res.content
            return content
        except Exception as err:
            status_code = res.status_code
            time.sleep(sleep)
            if 500 <= status_code <= 599:
                log.warning(" Retry Client Issue: %s, %s" % (res, url))
                return self.try_request(method, url, sleep, retry)
            log.warning(" %s: %s" % (res, url))
            if retry >= 3:
                log.error(" %s: %s" % (res, url))
                raise RequestError(err)
            return self.try_request(method, url, sleep + 2, retry + 1, json, provider)

    def set_headers(self, headers):
        self.__session.headers = headers
