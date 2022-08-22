import os
import pandas
import selenium
from time import sleep
from .helper import Helper
from selenium import webdriver
import geckodriver_autoinstaller
geckodriver_autoinstaller.install()


class Content:

    def absolute_bytes_difference(wiki, period, filter, interval):
        try:

            try:
                wikis = Helper.get_Wikis_Codes()
            except NameError:
                print("\u001b[91mError:\u001b[0m you need to import `Helper` class. Use 'from wikistats2csv import Helper'.\n")
                exit()

            periods = {'all-years':'all', 'one-year':'1-year', 'two-years':'2-year', 'three-months':'3-month', 'one-month':'1-month'}

            filters = {'no-filter':'~total', 'page-type-content':'page_type~content', 'page-type-non-content':'page_type~non-content', 'page-type-all':'page_type~content*non-content',
                       'editor-type-user':'editor_type~user', 'editor-type-name-bot':'editor_type~name-bot', 'editor-type-anonymous':'editor_type~anonymous', 'editor-type-group-bot':
                       'editor_type~group-bot', 'editor-type-all':'editor_type~anonymous*group-bot*name-bot*user'}

            intervals = {'daily':'daily', 'monthly':'monthly'}

            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.manager.showWhenStarting", False)
            profile.set_preference("browser.download.dir", f"{os.getcwd()}")
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
            driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='geckodriver', service_log_path=os.devnull)

            base_url = f'https://stats.wikimedia.org/#/{wiki}.wikipedia.org/content/absolute-bytes-diff/full|table|'
            parameters = f'{periods[period]}|{filters[filter]}|{intervals[interval]}'
            request_url = "".join([base_url, parameters])

            driver.implicitly_wait(5)
            driver.get(request_url)
            html = driver.page_source

            if intervals[interval]=='daily':
                sleep(10*2)
            if intervals[interval]=='monthly':
                sleep(10)

            csvFile = f"{(wikis[wiki]).lower()}--absolute-bytes-difference--{filter}--{period}--{interval}.csv"
            csvFile = csvFile.replace(' ','-')
            driver.find_element_by_class_name("ui.icon.button.tooltipped.tooltipped-n").click()
            sleep(3) ; os.rename("undefined.csv", csvFile)

            print(f"## Downloaded `{csvFile}` successfully :-)\n")
            print(f"** Quick glance at `{csvFile}` file:")
            readCSVfile = pandas.read_csv(csvFile)
            print(readCSVfile.to_string(max_rows=5), '\n')

            driver.close()
            driver.quit()

        except KeyboardInterrupt:
            print(f"\u001b[91mError:\u001b[0m exiting due to pressing ctrl-c ...\n")
            exit()

        except KeyError:
            if wiki not in wikis:
                print(f"\u001b[91mError:\u001b[0m this Wikipedia: '{wiki}' is not supported. To list Wikipedias with codes: `wikistats2csv -lw/--list-wikis`.\n")
            elif period not in periods:
                print(f"\u001b[91mError:\u001b[0m this time period: '{period}' is not supported. See GitHub for details: ")
                print("       https://github.com/SaiedAlshahrani/Wikistats-to-CSV/blob/main/README.md \n")            
            elif filter not in filters:
                print(f"\u001b[91mError:\u001b[0m this filter: '{filter}' is not supported. See GitHub for details: ")
                print("       https://github.com/SaiedAlshahrani/Wikistats-to-CSV/blob/main/README.md \n")
            elif interval not in intervals:
                print(f"\u001b[91mError:\u001b[0m this time interval: '{interval}' is not supported. See GitHub for details: ")
                print("       https://github.com/SaiedAlshahrani/Wikistats-to-CSV/blob/main/README.md \n")
            else: 
                print(f"\u001b[91mError:\u001b[0m one of these parameters: period-->'{period}', filter-->'{filter}', or interval-->'{interval}' is not supported.\n")
        
        except selenium.common.exceptions.WebDriverException:
            print(f"\u001b[91mError:\u001b[0m 'geckodriver' executable needs to be in PATH. See this documentation for details: ")
            print("       https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/ \n")

        except selenium.common.exceptions.NoSuchElementException:
            print(f"\u001b[91mError:\u001b[0m one of these parameters: period-->'{period}', filter-->'{filter}', or interval-->'{interval}' is not supported.\n")

        except:
            if 'Loading metric...' in html:
                print(f"\u001b[91mError:\u001b[0m cannot load and save this metric due to connection timeout!! Try again, or access it manually from here:")
                print(request_url, '\n')
            elif 'There is no data available for this date range on this project' in html:
                print("\u001b[91mError:\u001b[0m there is no data available for this date range on this Wikipedia.\n")
            else: 
                print("\u001b[91mError:\u001b[0m something unknown went wrong!! Please, try again!!\n")


    def edited_pages(wiki, period, filter, interval):
        try:
            
            try:
                wikis = Helper.get_Wikis_Codes()
            except NameError:
                print("\u001b[91mError:\u001b[0m you need to import `Helper` class. Use 'from wikistats2csv import Helper'.\n")
                exit()

            periods = {'all-years':'all', 'one-year':'1-year', 'two-years':'2-year', 'three-months':'3-month', 'one-month':'1-month'}

            filters = {'no-filter':'~total', 'page-type-content':'page_type~content', 'page-type-non-content':'page_type~non-content', 'page-type-all':'page_type~content*non-content',
                       'editor-type-user':'editor_type~user', 'editor-type-name-bot':'editor_type~name-bot', 'editor-type-anonymous':'editor_type~anonymous', 'editor-type-group-bot':
                       'editor_type~group-bot', 'editor-type-all':'editor_type~anonymous*group-bot*name-bot*user', 'activity-level-1-to-4-edits':'activity_level~1..4-edits',
                       'activity-level-5-to-24-edits':'activity_level~5..24-edits', 'activity-level-25-to-99-edits':'activity_level~25..99-edits',
                        'activity-level-100-or-more-edits':'activity_level~100..-edits', 'activity-level-all':'activity_level~1..4-edits*5..24-edits*25..99-edits*100..-edits'}

            intervals = {'daily':'daily', 'monthly':'monthly'}

            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.manager.showWhenStarting", False)
            profile.set_preference("browser.download.dir", f"{os.getcwd()}")
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
            driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='geckodriver', service_log_path=os.devnull)

            base_url = f'https://stats.wikimedia.org/#/{wiki}.wikipedia.org/content/edited-pages/full|table|'
            parameters = f'{periods[period]}|{filters[filter]}|{intervals[interval]}'
            request_url = "".join([base_url, parameters])

            driver.implicitly_wait(5)
            driver.get(request_url)
            html = driver.page_source

            if intervals[interval]=='daily':
                sleep(10*2)
            if intervals[interval]=='monthly':
                sleep(10)

            csvFile = f"{(wikis[wiki]).lower()}--edited-pages--{filter}--{period}--{interval}.csv"
            csvFile = csvFile.replace(' ','-')
            driver.find_element_by_class_name("ui.icon.button.tooltipped.tooltipped-n").click()
            sleep(3) ; os.rename("undefined.csv", csvFile)

            print(f"## Downloaded `{csvFile}` successfully :-)\n")
            print(f"** Quick glance at `{csvFile}` file:")
            readCSVfile = pandas.read_csv(csvFile)
            print(readCSVfile.to_string(max_rows=5), '\n')

            driver.close()
            driver.quit()

        except KeyboardInterrupt:
            print(f"\u001b[91mError:\u001b[0m exiting due to pressing ctrl-c ...\n")
            exit()

        except KeyError:
            if wiki not in wikis:
                print(f"\u001b[91mError:\u001b[0m this Wikipedia: '{wiki}' is not supported. To list Wikipedias with codes: `wikistats2csv -lw/--list-wikis`.\n")
            elif period not in periods:
                print(f"\u001b[91mError:\u001b[0m this time period: '{period}' is not supported. See GitHub for details: ")
                print("       https://github.com/SaiedAlshahrani/Wikistats-to-CSV/blob/main/README.md \n")            
            elif filter not in filters:
                print(f"\u001b[91mError:\u001b[0m this filter: '{filter}' is not supported. See GitHub for details: ")
                print("       https://github.com/SaiedAlshahrani/Wikistats-to-CSV/blob/main/README.md \n")
            elif interval not in intervals:
                print(f"\u001b[91mError:\u001b[0m this time interval: '{interval}' is not supported. See GitHub for details: ")
                print("       https://github.com/SaiedAlshahrani/Wikistats-to-CSV/blob/main/README.md \n")
            else: 
                print(f"\u001b[91mError:\u001b[0m one of these parameters: period-->'{period}', filter-->'{filter}', or interval-->'{interval}' is not supported.\n")
        
        except selenium.common.exceptions.WebDriverException:
            print(f"\u001b[91mError:\u001b[0m 'geckodriver' executable needs to be in PATH. See this documentation for details: ")
            print("       https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/ \n")

        except selenium.common.exceptions.NoSuchElementException:
            print(f"\u001b[91mError:\u001b[0m one of these parameters: period-->'{period}', filter-->'{filter}', or interval-->'{interval}' is not supported.\n")

        except:
            if 'Loading metric...' in html:
                print(f"\u001b[91mError:\u001b[0m cannot load and save this metric due to connection timeout!! Try again, or access it manually from here:")
                print(request_url, '\n')
            elif 'There is no data available for this date range on this project' in html:
                print("\u001b[91mError:\u001b[0m there is no data available for this date range on this Wikipedia.\n")
            else: 
                print("\u001b[91mError:\u001b[0m something unknown went wrong!! Please, try again!!\n")


    def net_bytes_difference(wiki, period, filter, interval):
        try:
            
            try:
                wikis = Helper.get_Wikis_Codes()
            except NameError:
                print("\u001b[91mError:\u001b[0m you need to import `Helper` class. Use 'from wikistats2csv import Helper'.\n")
                exit()

            periods = {'all-years':'all', 'one-year':'1-year', 'two-years':'2-year', 'three-months':'3-month', 'one-month':'1-month'}

            filters = {'no-filter':'~total', 'page-type-content':'page_type~content', 'page-type-non-content':'page_type~non-content', 'page-type-all':'page_type~content*non-content',
                       'editor-type-user':'editor_type~user', 'editor-type-name-bot':'editor_type~name-bot', 'editor-type-anonymous':'editor_type~anonymous', 'editor-type-group-bot':
                       'editor_type~group-bot', 'editor-type-all':'editor_type~anonymous*group-bot*name-bot*user'}

            intervals = {'daily':'daily', 'monthly':'monthly'}

            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.manager.showWhenStarting", False)
            profile.set_preference("browser.download.dir", f"{os.getcwd()}")
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
            driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='geckodriver', service_log_path=os.devnull)

            base_url = f'https://stats.wikimedia.org/#/{wiki}.wikipedia.org/content/net-bytes-difference/full|table|'
            parameters = f'{periods[period]}|{filters[filter]}|{intervals[interval]}'
            request_url = "".join([base_url, parameters])

            driver.implicitly_wait(5)
            driver.get(request_url)
            html = driver.page_source

            if intervals[interval]=='daily':
                sleep(10*2)
            if intervals[interval]=='monthly':
                sleep(10)

            csvFile = f"{(wikis[wiki]).lower()}--net-bytes-difference--{filter}--{period}--{interval}.csv"
            csvFile = csvFile.replace(' ','-')
            driver.find_element_by_class_name("ui.icon.button.tooltipped.tooltipped-n").click()
            sleep(3) ; os.rename("undefined.csv", csvFile)

            print(f"## Downloaded `{csvFile}` successfully :-)\n")
            print(f"** Quick glance at `{csvFile}` file:")
            readCSVfile = pandas.read_csv(csvFile)
            print(readCSVfile.to_string(max_rows=5), '\n')

            driver.close()
            driver.quit()

        except KeyboardInterrupt:
            print(f"\u001b[91mError:\u001b[0m exiting due to pressing ctrl-c ...\n")
            exit()

        except KeyError:
            if wiki not in wikis:
                print(f"\u001b[91mError:\u001b[0m this Wikipedia: '{wiki}' is not supported. To list Wikipedias with codes: `wikistats2csv -lw/--list-wikis`.\n")
            elif period not in periods:
                print(f"\u001b[91mError:\u001b[0m this time period: '{period}' is not supported. See GitHub for details: ")
                print("       https://github.com/SaiedAlshahrani/Wikistats-to-CSV/blob/main/README.md \n")            
            elif filter not in filters:
                print(f"\u001b[91mError:\u001b[0m this filter: '{filter}' is not supported. See GitHub for details: ")
                print("       https://github.com/SaiedAlshahrani/Wikistats-to-CSV/blob/main/README.md \n")
            elif interval not in intervals:
                print(f"\u001b[91mError:\u001b[0m this time interval: '{interval}' is not supported. See GitHub for details: ")
                print("       https://github.com/SaiedAlshahrani/Wikistats-to-CSV/blob/main/README.md \n")
            else: 
                print(f"\u001b[91mError:\u001b[0m one of these parameters: period-->'{period}', filter-->'{filter}', or interval-->'{interval}' is not supported.\n")
        
        except selenium.common.exceptions.WebDriverException:
            print(f"\u001b[91mError:\u001b[0m 'geckodriver' executable needs to be in PATH. See this documentation for details: ")
            print("       https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/ \n")

        except selenium.common.exceptions.NoSuchElementException:
            print(f"\u001b[91mError:\u001b[0m one of these parameters: period-->'{period}', filter-->'{filter}', or interval-->'{interval}' is not supported.\n")

        except:
            if 'Loading metric...' in html:
                print(f"\u001b[91mError:\u001b[0m cannot load and save this metric due to connection timeout!! Try again, or access it manually from here:")
                print(request_url, '\n')
            elif 'There is no data available for this date range on this project' in html:
                print("\u001b[91mError:\u001b[0m there is no data available for this date range on this Wikipedia.\n")
            else: 
                print("\u001b[91mError:\u001b[0m something unknown went wrong!! Please, try again!!\n")


    def pages_to_date(wiki, period, filter, interval):
        try:
            
            try:
                wikis = Helper.get_Wikis_Codes()
            except NameError:
                print("\u001b[91mError:\u001b[0m you need to import `Helper` class. Use 'from wikistats2csv import Helper'.\n")
                exit()

            periods = {'all-years':'all', 'one-year':'1-year', 'two-years':'2-year', 'three-months':'3-month', 'one-month':'1-month'}

            filters = {'no-filter':'~total', 'page-type-content':'page_type~content', 'page-type-non-content':'page_type~non-content', 'page-type-all':'page_type~content*non-content',
                       'editor-type-user':'editor_type~user', 'editor-type-name-bot':'editor_type~name-bot', 'editor-type-anonymous':'editor_type~anonymous', 'editor-type-group-bot':
                       'editor_type~group-bot', 'editor-type-all':'editor_type~anonymous*group-bot*name-bot*user'}

            intervals = {'daily':'daily', 'monthly':'monthly'}
            
            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.manager.showWhenStarting", False)
            profile.set_preference("browser.download.dir", f"{os.getcwd()}")
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
            driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='geckodriver', service_log_path=os.devnull)

            base_url = f'https://stats.wikimedia.org/#/{wiki}.wikipedia.org/content/pages-to-date/full|table|'
            parameters = f'{periods[period]}|{filters[filter]}|{intervals[interval]}'
            request_url = "".join([base_url, parameters])

            driver.implicitly_wait(5)
            driver.get(request_url)
            html = driver.page_source

            if intervals[interval]=='daily':
                sleep(10*2)
            if intervals[interval]=='monthly':
                sleep(10)

            csvFile = f"{(wikis[wiki]).lower()}--pages-to-date--{filter}--{period}--{interval}.csv"
            csvFile = csvFile.replace(' ','-')
            driver.find_element_by_class_name("ui.icon.button.tooltipped.tooltipped-n").click()
            sleep(3) ; os.rename("undefined.csv", csvFile)

            print(f"## Downloaded `{csvFile}` successfully :-)\n")
            print(f"** Quick glance at `{csvFile}` file:")
            readCSVfile = pandas.read_csv(csvFile)
            print(readCSVfile.to_string(max_rows=5), '\n')

            driver.close()
            driver.quit()

        except KeyboardInterrupt:
            print(f"\u001b[91mError:\u001b[0m exiting due to pressing ctrl-c ...\n")
            exit()

        except KeyError:
            if wiki not in wikis:
                print(f"\u001b[91mError:\u001b[0m this Wikipedia: '{wiki}' is not supported. To list Wikipedias with codes: `wikistats2csv -lw/--list-wikis`.\n")
            elif period not in periods:
                print(f"\u001b[91mError:\u001b[0m this time period: '{period}' is not supported. See GitHub for details: ")
                print("       https://github.com/SaiedAlshahrani/Wikistats-to-CSV/blob/main/README.md \n")            
            elif filter not in filters:
                print(f"\u001b[91mError:\u001b[0m this filter: '{filter}' is not supported. See GitHub for details: ")
                print("       https://github.com/SaiedAlshahrani/Wikistats-to-CSV/blob/main/README.md \n")
            elif interval not in intervals:
                print(f"\u001b[91mError:\u001b[0m this time interval: '{interval}' is not supported. See GitHub for details: ")
                print("       https://github.com/SaiedAlshahrani/Wikistats-to-CSV/blob/main/README.md \n")
            else: 
                print(f"\u001b[91mError:\u001b[0m one of these parameters: period-->'{period}', filter-->'{filter}', or interval-->'{interval}' is not supported.\n")
        
        except selenium.common.exceptions.WebDriverException:
            print(f"\u001b[91mError:\u001b[0m 'geckodriver' executable needs to be in PATH. See this documentation for details: ")
            print("       https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/ \n")

        except selenium.common.exceptions.NoSuchElementException:
            print(f"\u001b[91mError:\u001b[0m one of these parameters: period-->'{period}', filter-->'{filter}', or interval-->'{interval}' is not supported.\n")

        except:
            if 'Loading metric...' in html:
                print(f"\u001b[91mError:\u001b[0m cannot load and save this metric due to connection timeout!! Try again, or access it manually from here:")
                print(request_url, '\n')
            elif 'There is no data available for this date range on this project' in html:
                print("\u001b[91mError:\u001b[0m there is no data available for this date range on this Wikipedia.\n")
            else: 
                print("\u001b[91mError:\u001b[0m something unknown went wrong!! Please, try again!!\n")


    def total_media_requests(wiki, period, filter, interval):
        try:

            try:
                wikis = Helper.get_Wikis_Codes()
            except NameError:
                print("\u001b[91mError:\u001b[0m you need to import `Helper` class. Use 'from wikistats2csv import Helper'.\n")
                exit()

            periods = {'all-years':'all', 'one-year':'1-year', 'two-years':'2-year', 'three-months':'3-month', 'one-month':'1-month'}

            filters = {'no-filter':'~total', 'media-type-image':'media_type~image', 'media-type-video':'media_type~video', 'media-type-audio':'media_type~audio',
                       'media-type-document':'media_type~document', 'media-type-other':'media_type~other', 'media-type-all':'media_type~image*video*audio*document*other',
                       'agent-type-user':'agent~user', 'agent-type-spider':'agent~spider', 'agent-type-all':'agent~user*spider'}

            intervals = {'daily':'daily', 'monthly':'monthly'}

            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.manager.showWhenStarting", False)
            profile.set_preference("browser.download.dir", f"{os.getcwd()}")
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
            driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='geckodriver', service_log_path=os.devnull)

            base_url = f'https://stats.wikimedia.org/#/{wiki}.wikipedia.org/content/total-mediarequests/full|table|'
            parameters = f'{periods[period]}|{filters[filter]}|{intervals[interval]}'
            request_url = "".join([base_url, parameters])

            driver.implicitly_wait(5)
            driver.get(request_url)
            html = driver.page_source

            if intervals[interval]=='daily':
                sleep(10*2)
            if intervals[interval]=='monthly':
                sleep(10)

            csvFile = f"{(wikis[wiki]).lower()}--total-media-requests--{filter}--{period}--{interval}.csv"
            csvFile = csvFile.replace(' ','-')
            driver.find_element_by_class_name("ui.icon.button.tooltipped.tooltipped-n").click()
            sleep(3) ; os.rename("undefined.csv", csvFile)

            print(f"## Downloaded `{csvFile}` successfully :-)\n")
            print(f"** Quick glance at `{csvFile}` file:")
            readCSVfile = pandas.read_csv(csvFile)
            print(readCSVfile.to_string(max_rows=5), '\n')

            driver.close()
            driver.quit()

        except KeyboardInterrupt:
            print(f"\u001b[91mError:\u001b[0m exiting due to pressing ctrl-c ...\n")
            exit()

        except KeyError:
            if wiki not in wikis:
                print(f"\u001b[91mError:\u001b[0m this Wikipedia: '{wiki}' is not supported. To list Wikipedias with codes: `wikistats2csv -lw/--list-wikis`.\n")
            elif period not in periods:
                print(f"\u001b[91mError:\u001b[0m this time period: '{period}' is not supported. See GitHub for details: ")
                print("       https://github.com/SaiedAlshahrani/Wikistats-to-CSV/blob/main/README.md \n")            
            elif filter not in filters:
                print(f"\u001b[91mError:\u001b[0m this filter: '{filter}' is not supported. See GitHub for details: ")
                print("       https://github.com/SaiedAlshahrani/Wikistats-to-CSV/blob/main/README.md \n")
            elif interval not in intervals:
                print(f"\u001b[91mError:\u001b[0m this time interval: '{interval}' is not supported. See GitHub for details: ")
                print("       https://github.com/SaiedAlshahrani/Wikistats-to-CSV/blob/main/README.md \n")
            else: 
                print(f"\u001b[91mError:\u001b[0m one of these parameters: period-->'{period}', filter-->'{filter}', or interval-->'{interval}' is not supported.\n")
        
        except selenium.common.exceptions.WebDriverException:
            print(f"\u001b[91mError:\u001b[0m 'geckodriver' executable needs to be in PATH. See this documentation for details: ")
            print("       https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/ \n")

        except selenium.common.exceptions.NoSuchElementException:
            print(f"\u001b[91mError:\u001b[0m one of these parameters: period-->'{period}', filter-->'{filter}', or interval-->'{interval}' is not supported.\n")

        except:
            if 'Loading metric...' in html:
                print(f"\u001b[91mError:\u001b[0m cannot load and save this metric due to connection timeout!! Try again, or access it manually from here:")
                print(request_url, '\n')
            elif 'There is no data available for this date range on this project' in html:
                print("\u001b[91mError:\u001b[0m there is no data available for this date range on this Wikipedia.\n")
            else: 
                print("\u001b[91mError:\u001b[0m something unknown went wrong!! Please, try again!!\n")


    def top_media_requests(wiki, period, filter, interval):
        try:
            
            try:
                wikis = Helper.get_Wikis_Codes()
            except NameError:
                print("\u001b[91mError:\u001b[0m you need to import `Helper` class. Use 'from wikistats2csv import Helper'.\n")
                exit()

            periods = {'last-month':'last-month'}

            # if period not in periods:
                # periods.update({period:period})

            filters = {'no-filter':'~total', 'media-type-image':'(media_type)~image', 'media-type-video':'(media_type)~video', 'media-type-audio':'(media_type)~audio',
                       'media-type-document':'(media_type)~document', 'media-type-other':'(media_type)~other', 'media-type-all':'(media_type)~image*video*audio*document*other'}

            intervals = {'daily':'daily', 'monthly':'monthly'}

            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.manager.showWhenStarting", False)
            profile.set_preference("browser.download.dir", f"{os.getcwd()}")
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
            driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='geckodriver', service_log_path=os.devnull)

            base_url = f'https://stats.wikimedia.org/#/{wiki}.wikipedia.org/content/top-mediarequests/full|table|'
            parameters = f'{periods[period]}|{filters[filter]}|{intervals[interval]}'
            request_url = "".join([base_url, parameters])

            driver.implicitly_wait(5)
            driver.get(request_url)
            html = driver.page_source

            if intervals[interval]=='daily':
                sleep(10*2)
            if intervals[interval]=='monthly':
                sleep(10)

            csvFile = f"{(wikis[wiki]).lower()}--top-media-requests--{filter}--{period}--{interval}.csv"
            csvFile = csvFile.replace(' ','-')
            driver.find_element_by_class_name("ui.icon.button.tooltipped.tooltipped-n").click()
            sleep(3) ; os.rename("undefined.csv", csvFile)

            print(f"## Downloaded `{csvFile}` successfully :-)\n")
            print(f"** Quick glance at `{csvFile}` file:")
            readCSVfile = pandas.read_csv(csvFile)
            print(readCSVfile.to_string(max_rows=5), '\n')

            driver.close()
            driver.quit()

        except KeyboardInterrupt:
            print(f"\u001b[91mError:\u001b[0m exiting due to pressing ctrl-c ...\n")
            exit()

        except KeyError:
            if wiki not in wikis:
                print(f"\u001b[91mError:\u001b[0m this Wikipedia: '{wiki}' is not supported. To list Wikipedias with codes: `wikistats2csv -lw/--list-wikis`.\n")
            elif period not in periods:
                print(f"\u001b[91mError:\u001b[0m this time period: '{period}' is not supported. See GitHub for details: ")
                print("       https://github.com/SaiedAlshahrani/Wikistats-to-CSV/blob/main/README.md \n")            
            elif filter not in filters:
                print(f"\u001b[91mError:\u001b[0m this filter: '{filter}' is not supported. See GitHub for details: ")
                print("       https://github.com/SaiedAlshahrani/Wikistats-to-CSV/blob/main/README.md \n")
            elif interval not in intervals:
                print(f"\u001b[91mError:\u001b[0m this time interval: '{interval}' is not supported. See GitHub for details: ")
                print("       https://github.com/SaiedAlshahrani/Wikistats-to-CSV/blob/main/README.md \n")
            else: 
                print(f"\u001b[91mError:\u001b[0m one of these parameters: period-->'{period}', filter-->'{filter}', or interval-->'{interval}' is not supported.\n")
        
        except selenium.common.exceptions.WebDriverException:
            print(f"\u001b[91mError:\u001b[0m 'geckodriver' executable needs to be in PATH. See this documentation for details: ")
            print("       https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/ \n")

        except selenium.common.exceptions.NoSuchElementException:
            print(f"\u001b[91mError:\u001b[0m one of these parameters: period-->'{period}', filter-->'{filter}', or interval-->'{interval}' is not supported.\n")

        except:
            if 'Loading metric...' in html:
                print(f"\u001b[91mError:\u001b[0m cannot load and save this metric due to connection timeout!! Try again, or access it manually from here:")
                print(request_url, '\n')
            elif 'There is no data available for this date range on this project' in html:
                print("\u001b[91mError:\u001b[0m there is no data available for this date range on this Wikipedia.\n")
            else: 
                print("\u001b[91mError:\u001b[0m something unknown went wrong!! Please, try again!!\n")
