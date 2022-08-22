import os
import pandas
import selenium
from time import sleep
from .helper import Helper
from selenium import webdriver
import geckodriver_autoinstaller
geckodriver_autoinstaller.install()


class Reading:

    def total_page_views(wiki, period, filter, interval):
        try:

            try:
                wikis = Helper.get_Wikis_Codes()
            except NameError:
                print("\u001b[91mError:\u001b[0m you need to import `Helper` class. Use 'from wikistats2csv import Helper'.\n")
                exit()

            periods = {'all-years':'all', 'one-year':'1-year', 'two-years':'2-year', 'three-months':'3-month', 'one-month':'1-month'}

            filters = {'no-filter':'~total', 'access-method-desktop':'access~desktop', 'access-method-mobile-app':'access~mobile-app',
                       'access-method-mobile-web':'access~mobile-web', 'access-method-all':'access~desktop*mobile-app*mobile-web',
                       'agent-type-user':'agent~user', 'agent-type-spider':'agent~spider', 'agent-type-automated':'agent~automated',
                       'agent-type-all':'agent~user*spider*automated'}

            intervals = {'daily':'daily', 'monthly':'monthly'}

            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.manager.showWhenStarting", False)
            profile.set_preference("browser.download.dir", f"{os.getcwd()}")
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
            driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='geckodriver', service_log_path=os.devnull)

            base_url = f'https://stats.wikimedia.org/#/{wiki}.wikipedia.org/reading/total-page-views/normal|table|'
            parameters = f'{periods[period]}|{filters[filter]}|{intervals[interval]}'
            request_url = "".join([base_url, parameters])

            driver.implicitly_wait(5)
            driver.get(request_url)
            html = driver.page_source

            if intervals[interval]=='daily':
                sleep(10*2)
            if intervals[interval]=='monthly':
                sleep(10)

            csvFile = f"{(wikis[wiki]).lower()}--total-page-views--{filter}--{period}--{interval}.csv"
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


    def legacy_page_views(wiki, period, filter, interval):
        try:

            try:
                wikis = Helper.get_Wikis_Codes()
            except NameError:
                print("\u001b[91mError:\u001b[0m you need to import `Helper` class. Use 'from wikistats2csv import Helper'.\n")
                exit()

            periods = {'all-years':'all', 'one-year':'1-year', 'two-years':'2-year', 'three-months':'3-month', 'one-month':'1-month'}

            filters = {'no-filter':'~total', 'access-site-mobile-site':'(access-site)~mobile-site', 'access-site-desktop-site':
                       '(access-site)~desktop-site', 'access-site-all':'(access-site)~mobile-site*desktop-site'}

            intervals = {'daily':'daily', 'monthly':'monthly'}

            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.manager.showWhenStarting", False)
            profile.set_preference("browser.download.dir", f"{os.getcwd()}")
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
            driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='geckodriver', service_log_path=os.devnull)

            base_url = f'https://stats.wikimedia.org/#/{wiki}.wikipedia.org/reading/legacy-page-views/normal|table|'
            parameters = f'{periods[period]}|{filters[filter]}|{intervals[interval]}'
            request_url = "".join([base_url, parameters])

            driver.implicitly_wait(5)
            driver.get(request_url)
            html = driver.page_source

            if intervals[interval]=='daily':
                sleep(10*2)
            if intervals[interval]=='monthly':
                sleep(10)

            csvFile = f"{(wikis[wiki]).lower()}--legacy-page-views--{filter}--{period}--{interval}.csv"
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


    def page_views_by_country(wiki, period, filter, interval):
        try:

            try:
                wikis = Helper.get_Wikis_Codes()
            except NameError:
                print("\u001b[91mError:\u001b[0m you need to import `Helper` class. Use 'from wikistats2csv import Helper'.\n")
                exit()

            periods = {'last-month':'last-month'}

            # if period not in periods:
            #     periods.update({period:period})

            filters = {'no-filter':'~total', 'access-method-desktop':'(access)~desktop', 'access-method-mobile-app':'(access)~mobile-app',
                       'access-method-mobile-web':'(access)~mobile-web', 'access-method-all':'(access)~desktop*mobile-app*mobile-web'}

            intervals = {'daily':'daily', 'monthly':'monthly'}

            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.manager.showWhenStarting", False)
            profile.set_preference("browser.download.dir", f"{os.getcwd()}")
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
            driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='geckodriver', service_log_path=os.devnull)

            base_url = f'https://stats.wikimedia.org/#/{wiki}.wikipedia.org/reading/page-views-by-country/normal|table|'
            parameters = f'{periods[period]}|{filters[filter]}|{intervals[interval]}'
            request_url = "".join([base_url, parameters])

            driver.implicitly_wait(5)
            driver.get(request_url)
            html = driver.page_source

            if intervals[interval]=='daily':
                sleep(10*2)
            if intervals[interval]=='monthly':
                sleep(10)

            csvFile = f"{(wikis[wiki]).lower()}--page-views-by-country--{filter}--{period}--{interval}.csv"
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


    def unique_devices(wiki, period, filter, interval):
        try:

            try:
                wikis = Helper.get_Wikis_Codes()
            except NameError:
                print("\u001b[91mError:\u001b[0m you need to import `Helper` class. Use 'from wikistats2csv import Helper'.\n")
                exit()

            periods = {'all-years':'all', 'one-year':'1-year', 'two-years':'2-year', 'three-months':'3-month', 'one-month':'1-month'}

            filters = {'no-filter':'~total', 'access-site-mobile-site':'(access-site)~mobile-site', 'access-site-desktop-site':
                       '(access-site)~desktop-site', 'access-site-all':'(access-site)~mobile-site*desktop-site'}

            intervals = {'daily':'daily', 'monthly':'monthly'}

            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.manager.showWhenStarting", False)
            profile.set_preference("browser.download.dir", f"{os.getcwd()}")
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
            driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='geckodriver', service_log_path=os.devnull)

            base_url = f'https://stats.wikimedia.org/#/{wiki}.wikipedia.org/reading/unique-devices/normal|table|'
            parameters = f'{periods[period]}|{filters[filter]}|{intervals[interval]}'
            request_url = "".join([base_url, parameters])

            driver.implicitly_wait(5)
            driver.get(request_url)
            html = driver.page_source

            if intervals[interval]=='daily':
                sleep(10*2)
            if intervals[interval]=='monthly':
                sleep(10)

            csvFile = f"{(wikis[wiki]).lower()}--unique-devices--{filter}--{period}--{interval}.csv"
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


    def top_viewed_articles(wiki, period, filter, interval):
        try:

            try:
                wikis = Helper.get_Wikis_Codes()
            except NameError:
                print("\u001b[91mError:\u001b[0m you need to import `Helper` class. Use 'from wikistats2csv import Helper'.\n")
                exit()

            periods = {'last-month':'last-month'}

            # if period not in periods:
            #     periods.update({period:period})

            filters = {'no-filter':'~total', 'access-method-desktop':'(access)~desktop', 'access-method-mobile-app':'(access)~mobile-app',
                       'access-method-mobile-web':'(access)~mobile-web', 'access-method-all':'(access)~desktop*mobile-app*mobile-web'}

            intervals = {'daily':'daily', 'monthly':'monthly'}

            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.manager.showWhenStarting", False)
            profile.set_preference("browser.download.dir", f"{os.getcwd()}")
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
            driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='geckodriver', service_log_path=os.devnull)

            base_url = f'https://stats.wikimedia.org/#/{wiki}.wikipedia.org/reading/top-viewed-articles/normal|table|'
            parameters = f'{periods[period]}|{filters[filter]}|{intervals[interval]}'
            request_url = "".join([base_url, parameters])

            driver.implicitly_wait(5)
            driver.get(request_url)
            html = driver.page_source

            if intervals[interval]=='daily':
                sleep(10*2)
            if intervals[interval]=='monthly':
                sleep(10)

            csvFile = f"{(wikis[wiki]).lower()}--top-viewed-articles--{filter}--{period}--{interval}.csv"
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
