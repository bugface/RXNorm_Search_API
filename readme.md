## Searching information in RxNorm database using NDC codes

### install packages
>To use the code, packages need to be installed first
```bash
 pip install -r requirements.txt
```

### modify cofig for app to find and create input and output files
>In the config.py, you have to change the file variables
- input_file: a excel file containing all the NDC code you want to search
- ndc_col: the column name in your excel file for the column containing the actual NDC codes
- output_file: name the file you want the search results to be stored in TSV format
- json_file: name the file you want to store the search results in json format

### run the query
>To run the code, excute the following commend:
```bash
 python app.py -i input_file -o output_file --cache cache_file(json format)
```

### api
>several APIs will be provided if you import the package
- rxcui2ingredient: map given rxcui code to its ingredient level rxcui code with ingredient name
