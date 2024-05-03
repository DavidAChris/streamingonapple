import jmespath
from appleparser import log
from appleparser.request import Request
from appleparser.state import State
from appleparser.properties import Environment


class AppleTv(Request, State, Environment):
    def __init__(self):
        log.info("Init Apple")
        Environment.__init__(self)
        State.__init__(self)
        Request.__init__(self)
        self.config = self.get_config()
        self.set_headers(self.config['headers'])
        self.jmes_shelves = jmespath.compile(self.config['jmes']['shelves'])
        self.jmes_movie = jmespath.compile(self.config['jmes']['movie'])
        self.jmes_episodes = jmespath.compile(self.config['jmes']['episodes'])
        self.jmes_next_token = jmespath.compile(self.config['jmes']['nextToken'])
        self.next_token = self.config['nextToken']
        self.tmp = set()
