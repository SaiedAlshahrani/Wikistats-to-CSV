import pandas as pd
import sys, os, ssl


# To Suppress SettingWithCopyWarning in Pandas
pd.options.mode.chained_assignment = None

# To Override the SSL Error of '[SSL: CERTIFICATE_VERIFY_FAILED]'. 
ssl._create_default_https_context = ssl._create_unverified_context

# os.system(f"{sys.executable} -m pip install -q lxml pandas==1.4.3 ")


class Helper:
    def get_Wikis_Codes():
        url = r'https://en.wikipedia.org/wiki/List_of_Wikipedias'
        tables = pd.read_html(url)
        wikis_codes = tables[2] 
        wikis_codes = wikis_codes[['Wiki', 'Language']]
        wikis_codes = wikis_codes.set_index('Wiki').to_dict()['Language']
        return wikis_codes


    def get_Wikis_Depths():
        url = r'https://en.wikipedia.org/wiki/List_of_Wikipedias'
        tables = pd.read_html(url)
        wikis_depths = tables[2] 
        wikis_depths = wikis_depths[['Wiki', 'Language', 'Depth']]
        wikis_depths.loc[wikis_depths['Depth']=='——', 'Depth'] = 0
        wikis_depths["Depth"] = wikis_depths["Depth"].astype(str).astype(int)
        wikis_depths = wikis_depths.set_index('Wiki').to_dict()['Depth']
        return wikis_depths

        
