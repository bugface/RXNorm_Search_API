import requests
from functools import lru_cache
import re
# import os
import logging
from rxnorm_restful_api import NDC_PROPERTIES, RXCUI_ALLRELATED, RXCUI_ALLPROPERTIES, NDC_STATUS
from time import sleep
import json


FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('query_api')
logger.setLevel(logging.DEBUG)
headers = {'Accept':'application/json'}
cache_size = 2**12
query_sleep_time = 0.05
except_sleep_time = 60


def process_responce(rep):
    if rep.status_code == 200:
        return rep.text # json.loads(rep.text)


def find_ingradient(info):
    try:
        for each in info['allRelatedGroup']['conceptGroup']:
            if each['tty'] == "IN":
                for e in each['conceptProperties']:
                    ingrads = e['name']
                    ingrad_rxcui = e['rxcui']
        return ingrads, ingrad_rxcui
    except Exception as ex:
        logger.error(ex)
        return None, None


def find_schedule(props):
    # try:
    for each in props['propConceptGroup']['propConcept']:
        if each['propName'] == 'SCHEDULE':
            return each['propValue']
    # except Exception as e:
    #     logger.error(e)


def format_rxcui_properties(data):
    d = dict()
    for each in data['propConceptGroup']['propConcept']:
        d[each['propName']] = each['propValue']
    return d


@lru_cache(maxsize=cache_size)
def ndc_allRelated(ndc):
    url_ndc = NDC_STATUS.format(ndc)
    res = dict()
    try:
        #get NDC status
        rep = requests.get(url_ndc, headers=headers)
        ndc_info = json.loads(process_responce(rep))
        # del ndc_info['ndcStatus']['sourceName']
        rxcui = ndc_info['ndcStatus']['rxcui']
        #get ingredient
        url_rxcui = RXCUI_ALLRELATED.format(rxcui)
        rep = requests.get(url_rxcui, headers=headers)
        info = json.loads(process_responce(rep))
        print(rxcui)
        print(info)
        ingrad = find_ingradient(info)[0]
        # search for properties
        # logger.info(rxcui)
        url_schedule = RXCUI_ALLPROPERTIES.format(rxcui)
        rep = requests.get(url_schedule, headers=headers)
        sleep(query_sleep_time)
        props = json.loads(process_responce(rep))
        # logger.info(format_rxcui_properties(props))
        rxcui_props = format_rxcui_properties(props)
        return {**ndc_info['ndcStatus'], **rxcui_props, **{'ingredient': ingrad}}
    except requests.exceptions.HTTPError as errh:
        logger.info(f"Http Error: {errh}")
        sleep(except_sleep_time)
    except requests.exceptions.ConnectionError as errc:
        logger.info(f"Error Connecting: {errc}")
        sleep(except_sleep_time)
    except requests.exceptions.Timeout as errt:
        logger.info(f"Timeout Error: {errt}")
        sleep(except_sleep_time)
    except requests.exceptions.RequestException as err:
        logger.info(err)
        sleep(except_sleep_time)
    except Exception as e:
        logger.info(e)


def test():
    print(ndc_allRelated('00054485951'))


if __name__ == '__main__':
    test()