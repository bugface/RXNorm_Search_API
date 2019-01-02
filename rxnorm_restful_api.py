import traceback
import sys


class RXNORM_RESTFUL_API:
    def __init__(self):
        # base URL
        self.__ROOT = "https://rxnav.nlm.nih.gov/REST/"
        # NDC code related
        self.NDC_PROPERTIES = "ndcproperties?id={}"
        self.NDC_STATUS = "ndcstatus?ndc={}"
        # rxcui related
        self.RXCUI_ALLRELATED = "rxcui/{}/allrelated"
        self.RXCUI_ALLPROPERTIES = "rxcui/{}/allProperties.json?prop=attributes"
        self.RXCUI_HISTORY = "rxcuihistory/concept?rxcui={}"
        # rxcui and ingredients relation
        self.IS_RXCUI_IN = "rxcui/{}/filter?propName=TTY&propValues=IN"
        # relation between ndc and rxnorm
        self.RXCUI2NDC = "/rxcui/{}/allhistoricalndcs"

    def get_ndc_properties_by_id(self, ndc_id):
        return self.__ROOT + self.NDC_PROPERTIES.format(ndc_id)

    def get_ndc_status_by_ndc_code(self, ndc_code):
        return self.__ROOT + self.NDC_STATUS.format(ndc_code)

    def get_rxcui_allrelated(self, rxcui):
        return self.__ROOT + self.RXCUI_ALLRELATED.format(rxcui)

    def get_rxcui_history(self, rxcui):
        return self.__ROOT + self.RXCUI_HISTORY.format(rxcui)

    def get_rxcui_allproperties(self, rxcui):
        return self.__ROOT + self.RXCUI_ALLPROPERTIES.format(rxcui)

    def get_rxcui2ndc(self, rxcui):
        return self.__ROOT + self.RXCUI2NDC.format(rxcui)

    def get_is_rxcui_ingredient(self, rxcui):
        return  self.__ROOT + self.IS_RXCUI_IN.format(rxcui)


def test():
    rxnorm_api = RXNORM_RESTFUL_API()

    try:
        print(rxnorm_api.__ROOT + rxnorm_api.NDC_PROPERTIES.format(2018))
    except:
        print("It will raise an exception with trace: ")
        traceback.print_exc(file=sys.stdout)
        print("\n")

    print(rxnorm_api.get_ndc_properties_by_id(2018))


if __name__ == '__main__':
    test()