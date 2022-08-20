import pandas , ssl

# To Override the SSL Error of '[SSL: CERTIFICATE_VERIFY_FAILED]'. 
ssl._create_default_https_context = ssl._create_unverified_context

class Helper:
    def get_Wikis_Codes():
        url = r'https://en.wikipedia.org/wiki/List_of_Wikipedias'
        tables = pandas.read_html(url)
        wikis_codes = tables[2] 
        wikis_codes = wikis_codes[['Wiki', 'Language']]
        wikis_codes = wikis_codes.set_index('Wiki').to_dict()['Language']
        return wikis_codes