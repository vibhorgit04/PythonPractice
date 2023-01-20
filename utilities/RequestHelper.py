import logging as logger

import requests


class RequestHelper():

    def assert_status_code(self):
        assert self.rs.status_code == self.expected_status_code, "Bad status code. Endpoint: {}, Params: {}. " \
                                                                 "Actual status code: {}, Expected status code: {}, Response body: {}".format(
            self.endpoint, self.params, self.rs.status_code,
            self.expected_status_code, self.rs.json())

    def get(self, endpoint, params=None, expected_status_code=200):
        logger.info(f"Params: {params}")
        self.rs = requests.get(endpoint, params=params)
        self.endpoint = endpoint
        self.expected_status_code = expected_status_code
        self.params = params
        self.assert_status_code()

        return self.rs.json()

    def post(self, endpoint, params=None, expected_status_code=201):
        """
        Creating resource through POST method on system
        """
        logger.info(f"Params: {params}")
        self.rs = requests.post(endpoint, json=params)
        self.endpoint = endpoint
        self.expected_status_code = expected_status_code
        self.params = params
        self.assert_status_code()

        return self.rs.json()

    def delete(self):
        pass

    def put(self):
        pass
