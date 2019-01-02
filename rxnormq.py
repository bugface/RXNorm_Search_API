import requests
import traceback
from rxnorm_restful_api import RXNORM_RESTFUL_API
from config import create_logger, REQUESTS_TIMEOUT


# header used for requests to get json returned from get
headers = {'Accept': 'application/json',
           'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}


class RxNorm:
    def __init__(self):
        self.rxnorm_restful_api = RXNORM_RESTFUL_API()
        self.logger = None
        self.timeout = REQUESTS_TIMEOUT
        self.session = requests.Session()

    def task(self, task='is_rxcui_ingredient', **kwargs):
        self.logger = create_logger(task)
        self.logger.info(f'start task {task}...')
        if 'timeout' in kwargs:
            self.timeout = kwargs.get('timeout')

        if task == 'is_rxcui_ingredient':
            assert 'rxcui' in kwargs, 'rxcui code must be provided for this task'
            return self.__task_is_rxcui_ingredient(rxcui=kwargs.get('rxcui'))
        elif task == 'rxcui2ndc':
            pass
        elif task == 'ndc2rxcui':
            assert 'ndc' in kwargs, 'ndc code must be provided for this task'
            return self.__task_ndc2rxcui(ndc=kwargs.get('ndc'))

        # reset timeout to config timeout
        self.timeout = REQUESTS_TIMEOUT

    def __task_is_rxcui_ingredient(self, rxcui):
        rest_api = self.rxnorm_restful_api.get_is_rxcui_ingredient(rxcui)
        self.logger.info(f'restful api: {rest_api}')
        try:
            info = self.session.get(rest_api, headers=headers, timeout=self.timeout)
            self.logger.info(f'status: {info.status_code}')
            if info.text == 'null':
                return False
            return True
        except requests.exceptions.ReadTimeout:
            self.logger.info(f'request time out for checking rxcui code: {rxcui}')
        return False

    def __task_ndc2rxcui(self, ndc):
        pass


def test():
    rxnorm = RxNorm()
    print(rxnorm.task(rxcui=316326))
    print(rxnorm.task(rxcui=7052))
    print(rxnorm.task(rxcui=105918, timeout=1))
    try:
        print(rxnorm.task())
    except:
        traceback.print_exc()



if __name__ == '__main__':
    test()