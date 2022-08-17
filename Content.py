import selenium
import os , pandas
from Helper import *
from time import sleep
from selenium import webdriver


class Content:
    def absolute_bytes_difference(wiki, period, filter, interval):
        try:
            wikis = Helper.get_Wikis_Codes()

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
            driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='geckodriver')

            base_url = f'https://stats.wikimedia.org/#/{wiki}.wikipedia.org/content/absolute-bytes-diff/full|table|'
            parameters = f'{periods[period]}|{filters[filter]}|{intervals[interval]}'
            request_url = "".join([base_url, parameters])
            
            driver.implicitly_wait(5)
            driver.get(request_url) 
            html = driver.page_source

            if intervals[interval]=='daily':
                sleep(15*2)
            if intervals[interval]=='monthly':
                sleep(15)

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


    def edited_pages(wiki, period, filter, interval):
        try:
            wikis = Helper.get_Wikis_Codes()

            periods = {'all-years':'all', 'one-year':'1-year', 'two-years':'2-year', 'three-months':'3-month', 'one-month':'1-month'}

            filters = {'no-filter':'~total', 'page-type-content':'page_type~content', 'page-type-non-content':'page_type~non-content', 'page-type-all':'page_type~content*non-content', 
                       'editor-type-user':'editor_type~user', 'editor-type-name-bot':'editor_type~name-bot', 'editor-type-anonymous':'editor_type~anonymous', 'editor-type-group-bot':
                       'editor_type~group-bot', 'editor-type-all':'editor_type~anonymous*group-bot*name-bot*user', 'activity-level-1-to-4-edits':'activity_level~1..4-edits', 
                       'activity-level-5-to-24-edits':'activity_level~5..24-edits', 'activity-level-25-to-99-edits':'activity_level~25..99-edits', 
                        'activity-level-100-to-more-edits':'activity_level~100..-edits', 'activity-level-all':'activity_level~1..4-edits*5..24-edits*25..99-edits*100..-edits'}
            
            intervals = {'daily':'daily', 'monthly':'monthly'}

            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.manager.showWhenStarting", False)
            profile.set_preference("browser.download.dir", f"{os.getcwd()}")
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
            driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='geckodriver')
            
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

           
    def net_bytes_difference(wiki, period, filter, interval):
        try:
            wikis = Helper.get_Wikis_Codes()

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
            driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='geckodriver')

            base_url = f'https://stats.wikimedia.org/#/{wiki}.wikipedia.org/content/net-bytes-difference/full|table|'
            parameters = f'{periods[period]}|{filters[filter]}|{intervals[interval]}'
            request_url = "".join([base_url, parameters])
            
            driver.implicitly_wait(5)
            driver.get(request_url) 
            html = driver.page_source

            if intervals[interval]=='daily':
                sleep(15*2)
            if intervals[interval]=='monthly':
                sleep(15)

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


    def pages_to_date(wiki, period, filter, interval):
        try:
            wikis = Helper.get_Wikis_Codes()

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
            driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='geckodriver')

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


    def total_media_requests(wiki, period, filter, interval):
        try:
            wikis = Helper.get_Wikis_Codes()

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
            driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='geckodriver')

            base_url = f'https://stats.wikimedia.org/#/{wiki}.wikipedia.org/content/total-mediarequests/full|table|'
            parameters = f'{periods[period]}|{filters[filter]}|{intervals[interval]}'
            request_url = "".join([base_url, parameters])
            
            driver.implicitly_wait(5)
            driver.get(request_url) 
            html = driver.page_source

            if intervals[interval]=='daily':
                sleep(15*2)
            if intervals[interval]=='monthly':
                sleep(15)

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

              
    def top_media_requests(wiki, period, filter, interval):
        try:
            wikis = Helper.get_Wikis_Codes()

            periods = {'last-month':'last-month'}

            if period not in periods:
                periods.update({period:period})

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
            driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='geckodriver')

            base_url = f'https://stats.wikimedia.org/#/{wiki}.wikipedia.org/content/top-mediarequests/full|table|'
            parameters = f'{periods[period]}|{filters[filter]}|{intervals[interval]}'
            request_url = "".join([base_url, parameters])
            
            driver.implicitly_wait(5)
            driver.get(request_url) 
            html = driver.page_source

            if intervals[interval]=='daily':
                sleep(15*2)
            if intervals[interval]=='monthly':
                sleep(15)

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