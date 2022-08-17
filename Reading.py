import selenium
import os , pandas
from Helper import *
from time import sleep
from selenium import webdriver

class Reading:
    def total_page_views(wiki, period, filter, interval):
        try:
            wikis = Helper.get_Wikis_Codes()

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
            driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='geckodriver')

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
             
        except KeyError:
           print(f"## Error: one of these: period->'{period}', filter->'{filter}', or interval->'{interval}' is not supported.\n")

        except selenium.common.exceptions.NoSuchElementException:
           print(f"## Error: one of these: period->'{period}', filter->'{filter}', or interval->'{interval}' is not supported.\n")

        except:
            if 'Loading metric...' in html:
                print('## Error: cannot load and save the metric due to connection timeout!! Try downloading it manually from here:')                
                print(request_url, '\n')
            elif 'There is no data available for this date range on this project' in html:
                print('## Error: there is no data available for this date range on this Wikipedia.\n')
            else:  
                print(f"## Error: something unknown went wrong! Sorry, try again!.\n")
            
        finally: exit()


    def legacy_page_views(wiki, period, filter, interval):
        try:
            wikis = Helper.get_Wikis_Codes()

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
            driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='geckodriver')

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
             
        except KeyError:
           print(f"## Error: one of these: period->'{period}', filter->'{filter}', or interval->'{interval}' is not supported.\n")

        except selenium.common.exceptions.NoSuchElementException:
           print(f"## Error: one of these: period->'{period}', filter->'{filter}', or interval->'{interval}' is not supported.\n")

        except:
            if 'Loading metric...' in html:
                print('## Error: cannot load and save the metric due to connection timeout!! Try downloading it manually from here:')                
                print(request_url, '\n')
            elif 'There is no data available for this date range on this project' in html:
                print('## Error: there is no data available for this date range on this Wikipedia.\n')
            else:  
                print(f"## Error: something unknown went wrong! Sorry, try again!.\n")
            
        finally: exit()


    def page_views_by_country(wiki, period, filter, interval):
        try:
            wikis = Helper.get_Wikis_Codes()

            periods = {'last-month':'last-month'}

            if period not in periods:
                periods.update({period:period})

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
            driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='geckodriver')

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
             
        except KeyError:
           print(f"## Error: one of these: period->'{period}', filter->'{filter}', or interval->'{interval}' is not supported.\n")

        except selenium.common.exceptions.NoSuchElementException:
           print(f"## Error: one of these: period->'{period}', filter->'{filter}', or interval->'{interval}' is not supported.\n")

        except:
            if 'Loading metric...' in html:
                print('## Error: cannot load and save the metric due to connection timeout!! Try downloading it manually from here:')                
                print(request_url, '\n')
            elif 'There is no data available for this date range on this project' in html:
                print('## Error: there is no data available for this date range on this Wikipedia.\n')
            else:  
                print(f"## Error: something unknown went wrong! Sorry, try again!.\n")
            
        finally: exit()


    def unique_devices(wiki, period, filter, interval):
        try:
            wikis = Helper.get_Wikis_Codes()

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
            driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='geckodriver')

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
             
        except KeyError:
           print(f"## Error: one of these: period->'{period}', filter->'{filter}', or interval->'{interval}' is not supported.\n")

        except selenium.common.exceptions.NoSuchElementException:
           print(f"## Error: one of these: period->'{period}', filter->'{filter}', or interval->'{interval}' is not supported.\n")

        except:
            if 'Loading metric...' in html:
                print('## Error: cannot load and save the metric due to connection timeout!! Try downloading it manually from here:')                
                print(request_url, '\n')
            elif 'There is no data available for this date range on this project' in html:
                print('## Error: there is no data available for this date range on this Wikipedia.\n')
            else:  
                print(f"## Error: something unknown went wrong! Sorry, try again!.\n")
            
        finally: exit()


    def top_viewed_articles(wiki, period, filter, interval):
        try:
            wikis = Helper.get_Wikis_Codes()

            periods = {'last-month':'last-month'}

            if period not in periods:
                periods.update({period:period})

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
            driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='geckodriver')

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
             
        except KeyError:
           print(f"## Error: one of these: period->'{period}', filter->'{filter}', or interval->'{interval}' is not supported.\n")

        except selenium.common.exceptions.NoSuchElementException:
           print(f"## Error: one of these: period->'{period}', filter->'{filter}', or interval->'{interval}' is not supported.\n")

        except:
            if 'Loading metric...' in html:
                print('## Error: cannot load and save the metric due to connection timeout!! Try downloading it manually from here:')                
                print(request_url, '\n')
            elif 'There is no data available for this date range on this project' in html:
                print('## Error: there is no data available for this date range on this Wikipedia.\n')
            else:  
                print(f"## Error: something unknown went wrong! Sorry, try again!.\n")
            
        finally: exit()