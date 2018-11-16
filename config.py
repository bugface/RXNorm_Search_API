input_file = "test/nonmatching_subset2017.xlsx"
ndc_col = "ndcnum"
output_file = "test/test.tsv"
json_output = "test/test.json"


class RXNORM_API:
    def __init__(self):
        # NDC code related
        self.NDC_PROPERTIES = "https://rxnav.nlm.nih.gov/REST/ndcproperties?id={}"
        self.NDC_STATUS = "https://rxnav.nlm.nih.gov/REST/ndcstatus?ndc={}"
        # rxcui related
        self.RXCUI2INGREDIENT = "https://rxnav.nlm.nih.gov/REST/rxcui/{}/filter?propName=TTY&propValues=IN"
        self.RXCUI_ALLRELATED = "https://rxnav.nlm.nih.gov/REST/rxcui/{}/allrelated"
        self.RXCUI_ALLPROPERTIES = "https://rxnav.nlm.nih.gov/REST/rxcui/{}/allProperties.json?prop=attributes"
        self.RXCUI_HISTORY = "https://rxnav.nlm.nih.gov/REST/rxcuihistory/concept?rxcui={}"