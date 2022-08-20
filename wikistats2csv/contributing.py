import os
import rich
import pandas
import selenium
from time import sleep
from .helper import Helper
from selenium import webdriver
import geckodriver_autoinstaller
geckodriver_autoinstaller.install()


class Contributing:

    def editors(wiki, period, filter, interval):
        try:
            wikis = Helper.get_Wikis_Codes()

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

            base_url = f'https://stats.wikimedia.org/#/{wiki}.wikipedia.org/contributing/editors/full|table|'
            parameters = f'{periods[period]}|{filters[filter]}|{intervals[interval]}'
            request_url = "".join([base_url, parameters])

            driver.implicitly_wait(5)
            driver.get(request_url)
            html = driver.page_source

            if intervals[interval]=='daily':
                sleep(10*2)
            if intervals[interval]=='monthly':
                sleep(10)

            csvFile = f"{(wikis[wiki]).lower()}--editors--{filter}--{period}--{interval}.csv"
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
            rich.print(f"[bright_red]## Error:[/][bright_white] exiting due to pressing ctrl-c ...[/]\n")
            exit()

        except KeyError:
            if wiki not in wikis:
                rich.print(f"[bright_red]## Error:[/][bright_white] this Wikipedia: '{wiki}' is not supported. To list wiki codes use: `wikistats2csv -lw or --list-wikis`.[/]\n")
            elif period not in periods:
                rich.print(f"[bright_red]## Error:[/][bright_white] this time period: '{period}' is not supported. To list time periods use: `wikistats2csv -lp or --list-periods`[/]\n")
            elif filter not in filters:
                rich.print(f"[bright_red]## Error:[/][bright_white] this filter: '{filter}' is not supported. To list supported filters use: `wikistats2csv -lf or --list-filters`.[/]\n")
            elif interval not in intervals:
                rich.print(f"[bright_red]## Error:[/][bright_white] this time interval: '{interval}' is not supported. To list time intervals use: `wikistats2csv -li or --list-intervals`.[/]\n")
            else: 
                rich.print(f"[bright_red]## Error:[/][bright_white] one of these parameters: period-->'{period}', filter-->'{filter}', or interval-->'{interval}' is not supported.[/]\n")

        except selenium.common.exceptions.NoSuchElementException:
            rich.print(f"[bright_red]## Error:[/][bright_white] one of these parameters: period-->'{period}', filter-->'{filter}', or interval-->'{interval}' is not supported.[/]\n")

        except:
            if 'Loading metric...' in html:
                rich.print(f"[bright_red]## Error:[/][bright_white] cannot load and save this metric due to connection timeout!! Try again, or access it manually from here:[/]")
                print(request_url, '\n')
            elif 'There is no data available for this date range on this project' in html:
                rich.print(f"[bright_red]## Error:[/][bright_white] there is no data available for this date range on this Wikipedia.[/]\n")
            else: 
                rich.print(f"[bright_red]## Error:[/][bright_white] something unknown went wrong!! Please, try again!![/]\n")


    def active_editors(wiki, period, filter, interval):
        try:
            wikis = Helper.get_Wikis_Codes()

            periods = {'all-years':'all', 'one-year':'1-year', 'two-years':'2-year', 'three-months':'3-month', 'one-month':'1-month'}

            filters = {'no-filter':'~total', 'page-type-content':'page_type~content', 'page-type-non-content':'page_type~non-content', 'page-type-all':'page_type~content*non-content'}

            intervals = {'daily':'daily', 'monthly':'monthly'}

            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.manager.showWhenStarting", False)
            profile.set_preference("browser.download.dir", f"{os.getcwd()}")
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
            driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='geckodriver', service_log_path=os.devnull)

            base_url = f'https://stats.wikimedia.org/#/{wiki}.wikipedia.org/contributing/active-editors/full|table|'
            parameters = f'{periods[period]}|{filters[filter]}|{intervals[interval]}'
            request_url = "".join([base_url, parameters])

            driver.implicitly_wait(5)
            driver.get(request_url)
            html = driver.page_source

            if intervals[interval]=='daily':
                sleep(10*2)
            if intervals[interval]=='monthly':
                sleep(10)

            csvFile = f"{(wikis[wiki]).lower()}--active-editors--{filter}--{period}--{interval}.csv"
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
            rich.print(f"[bright_red]## Error:[/][bright_white] exiting due to pressing ctrl-c ...[/]\n")
            exit()

        except KeyError:
            if wiki not in wikis:
                rich.print(f"[bright_red]## Error:[/][bright_white] this Wikipedia: '{wiki}' is not supported. To list wiki codes use: `wikistats2csv -lw or --list-wikis`.[/]\n")
            elif period not in periods:
                rich.print(f"[bright_red]## Error:[/][bright_white] this time period: '{period}' is not supported. To list time periods use: `wikistats2csv -lp or --list-periods`[/]\n")
            elif filter not in filters:
                rich.print(f"[bright_red]## Error:[/][bright_white] this filter: '{filter}' is not supported. To list supported filters use: `wikistats2csv -lf or --list-filters`.[/]\n")
            elif interval not in intervals:
                rich.print(f"[bright_red]## Error:[/][bright_white] this time interval: '{interval}' is not supported. To list time intervals use: `wikistats2csv -li or --list-intervals`.[/]\n")
            else: 
                rich.print(f"[bright_red]## Error:[/][bright_white] one of these parameters: period-->'{period}', filter-->'{filter}', or interval-->'{interval}' is not supported.[/]\n")

        except selenium.common.exceptions.NoSuchElementException:
            rich.print(f"[bright_red]## Error:[/][bright_white] one of these parameters: period-->'{period}', filter-->'{filter}', or interval-->'{interval}' is not supported.[/]\n")

        except:
            if 'Loading metric...' in html:
                rich.print(f"[bright_red]## Error:[/][bright_white] cannot load and save this metric due to connection timeout!! Try again, or access it manually from here:[/]")
                print(request_url, '\n')
            elif 'There is no data available for this date range on this project' in html:
                rich.print(f"[bright_red]## Error:[/][bright_white] there is no data available for this date range on this Wikipedia.[/]\n")
            else: 
                rich.print(f"[bright_red]## Error:[/][bright_white] something unknown went wrong!! Please, try again!![/]\n")


    def edits(wiki, period, filter, interval):
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
            driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='geckodriver', service_log_path=os.devnull)

            base_url = f'https://stats.wikimedia.org/#/{wiki}.wikipedia.org/contributing/edits/full|table|'
            parameters = f'{periods[period]}|{filters[filter]}|{intervals[interval]}'
            request_url = "".join([base_url, parameters])

            driver.implicitly_wait(5)
            driver.get(request_url)
            html = driver.page_source

            if intervals[interval]=='daily':
                sleep(10*2)
            if intervals[interval]=='monthly':
                sleep(10)

            csvFile = f"{(wikis[wiki]).lower()}--edits--{filter}--{period}--{interval}.csv"
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
            rich.print(f"[bright_red]## Error:[/][bright_white] exiting due to pressing ctrl-c ...[/]\n")
            exit()

        except KeyError:
            if wiki not in wikis:
                rich.print(f"[bright_red]## Error:[/][bright_white] this Wikipedia: '{wiki}' is not supported. To list wiki codes use: `wikistats2csv -lw or --list-wikis`.[/]\n")
            elif period not in periods:
                rich.print(f"[bright_red]## Error:[/][bright_white] this time period: '{period}' is not supported. To list time periods use: `wikistats2csv -lp or --list-periods`[/]\n")
            elif filter not in filters:
                rich.print(f"[bright_red]## Error:[/][bright_white] this filter: '{filter}' is not supported. To list supported filters use: `wikistats2csv -lf or --list-filters`.[/]\n")
            elif interval not in intervals:
                rich.print(f"[bright_red]## Error:[/][bright_white] this time interval: '{interval}' is not supported. To list time intervals use: `wikistats2csv -li or --list-intervals`.[/]\n")
            else: 
                rich.print(f"[bright_red]## Error:[/][bright_white] one of these parameters: period-->'{period}', filter-->'{filter}', or interval-->'{interval}' is not supported.[/]\n")

        except selenium.common.exceptions.NoSuchElementException:
            rich.print(f"[bright_red]## Error:[/][bright_white] one of these parameters: period-->'{period}', filter-->'{filter}', or interval-->'{interval}' is not supported.[/]\n")

        except:
            if 'Loading metric...' in html:
                rich.print(f"[bright_red]## Error:[/][bright_white] cannot load and save this metric due to connection timeout!! Try again, or access it manually from here:[/]")
                print(request_url, '\n')
            elif 'There is no data available for this date range on this project' in html:
                rich.print(f"[bright_red]## Error:[/][bright_white] there is no data available for this date range on this Wikipedia.[/]\n")
            else: 
                rich.print(f"[bright_red]## Error:[/][bright_white] something unknown went wrong!! Please, try again!![/]\n")


    def user_edits(wiki, period, filter, interval):
        try:
            wikis = Helper.get_Wikis_Codes()

            periods = {'all-years':'all', 'one-year':'1-year', 'two-years':'2-year', 'three-months':'3-month', 'one-month':'1-month'}

            filters = {'no-filter':'~total', 'page-type-content':'page_type~content', 'page-type-non-content':'page_type~non-content', 'page-type-all':'page_type~content*non-content'}

            intervals = {'daily':'daily', 'monthly':'monthly'}

            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.manager.showWhenStarting", False)
            profile.set_preference("browser.download.dir", f"{os.getcwd()}")
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
            driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='geckodriver', service_log_path=os.devnull)

            base_url = f'https://stats.wikimedia.org/#/{wiki}.wikipedia.org/contributing/user-edits/full|table|'
            parameters = f'{periods[period]}|{filters[filter]}|{intervals[interval]}'
            request_url = "".join([base_url, parameters])

            driver.implicitly_wait(5)
            driver.get(request_url)
            html = driver.page_source

            if intervals[interval]=='daily':
                sleep(10*2)
            if intervals[interval]=='monthly':
                sleep(10)

            csvFile = f"{(wikis[wiki]).lower()}--user-edits--{filter}--{period}--{interval}.csv"
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
            rich.print(f"[bright_red]## Error:[/][bright_white] exiting due to pressing ctrl-c ...[/]\n")
            exit()

        except KeyError:
            if wiki not in wikis:
                rich.print(f"[bright_red]## Error:[/][bright_white] this Wikipedia: '{wiki}' is not supported. To list wiki codes use: `wikistats2csv -lw or --list-wikis`.[/]\n")
            elif period not in periods:
                rich.print(f"[bright_red]## Error:[/][bright_white] this time period: '{period}' is not supported. To list time periods use: `wikistats2csv -lp or --list-periods`[/]\n")
            elif filter not in filters:
                rich.print(f"[bright_red]## Error:[/][bright_white] this filter: '{filter}' is not supported. To list supported filters use: `wikistats2csv -lf or --list-filters`.[/]\n")
            elif interval not in intervals:
                rich.print(f"[bright_red]## Error:[/][bright_white] this time interval: '{interval}' is not supported. To list time intervals use: `wikistats2csv -li or --list-intervals`.[/]\n")
            else: 
                rich.print(f"[bright_red]## Error:[/][bright_white] one of these parameters: period-->'{period}', filter-->'{filter}', or interval-->'{interval}' is not supported.[/]\n")

        except selenium.common.exceptions.NoSuchElementException:
            rich.print(f"[bright_red]## Error:[/][bright_white] one of these parameters: period-->'{period}', filter-->'{filter}', or interval-->'{interval}' is not supported.[/]\n")

        except:
            if 'Loading metric...' in html:
                rich.print(f"[bright_red]## Error:[/][bright_white] cannot load and save this metric due to connection timeout!! Try again, or access it manually from here:[/]")
                print(request_url, '\n')
            elif 'There is no data available for this date range on this project' in html:
                rich.print(f"[bright_red]## Error:[/][bright_white] there is no data available for this date range on this Wikipedia.[/]\n")
            else: 
                rich.print(f"[bright_red]## Error:[/][bright_white] something unknown went wrong!! Please, try again!![/]\n")


    def new_pages(wiki, period, filter, interval):
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
            driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='geckodriver', service_log_path=os.devnull)

            base_url = f'https://stats.wikimedia.org/#/{wiki}.wikipedia.org/contributing/new-pages/full|table|'
            parameters = f'{periods[period]}|{filters[filter]}|{intervals[interval]}'
            request_url = "".join([base_url, parameters])

            driver.implicitly_wait(5)
            driver.get(request_url)
            html = driver.page_source

            if intervals[interval]=='daily':
                sleep(10*2)
            if intervals[interval]=='monthly':
                sleep(10)

            csvFile = f"{(wikis[wiki]).lower()}--new-pages--{filter}--{period}--{interval}.csv"
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
            rich.print(f"[bright_red]## Error:[/][bright_white] exiting due to pressing ctrl-c ...[/]\n")
            exit()

        except KeyError:
            if wiki not in wikis:
                rich.print(f"[bright_red]## Error:[/][bright_white] this Wikipedia: '{wiki}' is not supported. To list wiki codes use: `wikistats2csv -lw or --list-wikis`.[/]\n")
            elif period not in periods:
                rich.print(f"[bright_red]## Error:[/][bright_white] this time period: '{period}' is not supported. To list time periods use: `wikistats2csv -lp or --list-periods`[/]\n")
            elif filter not in filters:
                rich.print(f"[bright_red]## Error:[/][bright_white] this filter: '{filter}' is not supported. To list supported filters use: `wikistats2csv -lf or --list-filters`.[/]\n")
            elif interval not in intervals:
                rich.print(f"[bright_red]## Error:[/][bright_white] this time interval: '{interval}' is not supported. To list time intervals use: `wikistats2csv -li or --list-intervals`.[/]\n")
            else: 
                rich.print(f"[bright_red]## Error:[/][bright_white] one of these parameters: period-->'{period}', filter-->'{filter}', or interval-->'{interval}' is not supported.[/]\n")

        except selenium.common.exceptions.NoSuchElementException:
            rich.print(f"[bright_red]## Error:[/][bright_white] one of these parameters: period-->'{period}', filter-->'{filter}', or interval-->'{interval}' is not supported.[/]\n")

        except:
            if 'Loading metric...' in html:
                rich.print(f"[bright_red]## Error:[/][bright_white] cannot load and save this metric due to connection timeout!! Try again, or access it manually from here:[/]")
                print(request_url, '\n')
            elif 'There is no data available for this date range on this project' in html:
                rich.print(f"[bright_red]## Error:[/][bright_white] there is no data available for this date range on this Wikipedia.[/]\n")
            else: 
                rich.print(f"[bright_red]## Error:[/][bright_white] something unknown went wrong!! Please, try again!![/]\n")


    def new_registered_users(wiki, period, filter, interval):
        try:
            wikis = Helper.get_Wikis_Codes()

            periods = {'all-years':'all', 'one-year':'1-year', 'two-years':'2-year', 'three-months':'3-month', 'one-month':'1-month'}

            filters = {'no-filter':'~total'}

            intervals = {'daily':'daily', 'monthly':'monthly'}

            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.manager.showWhenStarting", False)
            profile.set_preference("browser.download.dir", f"{os.getcwd()}")
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
            driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='geckodriver', service_log_path=os.devnull)

            base_url = f'https://stats.wikimedia.org/#/{wiki}.wikipedia.org/contributing/new-registered-users/full|table|'
            parameters = f'{periods[period]}|{filters[filter]}|{intervals[interval]}'
            request_url = "".join([base_url, parameters])

            driver.implicitly_wait(5)
            driver.get(request_url)
            html = driver.page_source

            if intervals[interval]=='daily':
                sleep(10*2)
            if intervals[interval]=='monthly':
                sleep(10)

            csvFile = f"{(wikis[wiki]).lower()}--new-registered-users--{filter}--{period}--{interval}.csv"
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
            rich.print(f"[bright_red]## Error:[/][bright_white] exiting due to pressing ctrl-c ...[/]\n")
            exit()

        except KeyError:
            if wiki not in wikis:
                rich.print(f"[bright_red]## Error:[/][bright_white] this Wikipedia: '{wiki}' is not supported. To list wiki codes use: `wikistats2csv -lw or --list-wikis`.[/]\n")
            elif period not in periods:
                rich.print(f"[bright_red]## Error:[/][bright_white] this time period: '{period}' is not supported. To list time periods use: `wikistats2csv -lp or --list-periods`[/]\n")
            elif filter not in filters:
                rich.print(f"[bright_red]## Error:[/][bright_white] this filter: '{filter}' is not supported. To list supported filters use: `wikistats2csv -lf or --list-filters`.[/]\n")
            elif interval not in intervals:
                rich.print(f"[bright_red]## Error:[/][bright_white] this time interval: '{interval}' is not supported. To list time intervals use: `wikistats2csv -li or --list-intervals`.[/]\n")
            else: 
                rich.print(f"[bright_red]## Error:[/][bright_white] one of these parameters: period-->'{period}', filter-->'{filter}', or interval-->'{interval}' is not supported.[/]\n")

        except selenium.common.exceptions.NoSuchElementException:
            rich.print(f"[bright_red]## Error:[/][bright_white] one of these parameters: period-->'{period}', filter-->'{filter}', or interval-->'{interval}' is not supported.[/]\n")

        except:
            if 'Loading metric...' in html:
                rich.print(f"[bright_red]## Error:[/][bright_white] cannot load and save this metric due to connection timeout!! Try again, or access it manually from here:[/]")
                print(request_url, '\n')
            elif 'There is no data available for this date range on this project' in html:
                rich.print(f"[bright_red]## Error:[/][bright_white] there is no data available for this date range on this Wikipedia.[/]\n")
            else: 
                rich.print(f"[bright_red]## Error:[/][bright_white] something unknown went wrong!! Please, try again!![/]\n")


    def top_editors(wiki, period, filter, interval):
        try:
            wikis = Helper.get_Wikis_Codes()

            periods = {'last-month':'last-month'}

            if period not in periods:
                periods.update({period:period})

            filters = {'no-filter':'~total', 'page-type-content':'(page_type)~content', 'page-type-non-content':'(page_type)~non-content', 'page-type-all':'(page_type)~content*non-content',
                       'editor-type-user':'(editor_type)~user', 'editor-type-name-bot':'(editor_type)~name-bot', 'editor-type-anonymous':'(editor_type)~anonymous', 'editor-type-group-bot':
                       '(editor_type)~group-bot', 'editor-type-all':'(editor_type)~anonymous*group-bot*name-bot*user'}

            intervals = {'daily':'daily', 'monthly':'monthly'}

            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.manager.showWhenStarting", False)
            profile.set_preference("browser.download.dir", f"{os.getcwd()}")
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
            driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='geckodriver', service_log_path=os.devnull)

            base_url = f'https://stats.wikimedia.org/#/{wiki}.wikipedia.org/contributing/top-editors/full|table|'
            parameters = f'{periods[period]}|{filters[filter]}|{intervals[interval]}'
            request_url = "".join([base_url, parameters])

            driver.implicitly_wait(5)
            driver.get(request_url)
            html = driver.page_source

            if intervals[interval]=='daily':
                sleep(10*2)
            if intervals[interval]=='monthly':
                sleep(10)

            csvFile = f"{(wikis[wiki]).lower()}--top-editors--{filter}--{period}--{interval}.csv"
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
            rich.print(f"[bright_red]## Error:[/][bright_white] exiting due to pressing ctrl-c ...[/]\n")
            exit()

        except KeyError:
            if wiki not in wikis:
                rich.print(f"[bright_red]## Error:[/][bright_white] this Wikipedia: '{wiki}' is not supported. To list wiki codes use: `wikistats2csv -lw or --list-wikis`.[/]\n")
            elif period not in periods:
                rich.print(f"[bright_red]## Error:[/][bright_white] this time period: '{period}' is not supported. To list time periods use: `wikistats2csv -lp or --list-periods`[/]\n")
            elif filter not in filters:
                rich.print(f"[bright_red]## Error:[/][bright_white] this filter: '{filter}' is not supported. To list supported filters use: `wikistats2csv -lf or --list-filters`.[/]\n")
            elif interval not in intervals:
                rich.print(f"[bright_red]## Error:[/][bright_white] this time interval: '{interval}' is not supported. To list time intervals use: `wikistats2csv -li or --list-intervals`.[/]\n")
            else: 
                rich.print(f"[bright_red]## Error:[/][bright_white] one of these parameters: period-->'{period}', filter-->'{filter}', or interval-->'{interval}' is not supported.[/]\n")

        except selenium.common.exceptions.NoSuchElementException:
            rich.print(f"[bright_red]## Error:[/][bright_white] one of these parameters: period-->'{period}', filter-->'{filter}', or interval-->'{interval}' is not supported.[/]\n")

        except:
            if 'Loading metric...' in html:
                rich.print(f"[bright_red]## Error:[/][bright_white] cannot load and save this metric due to connection timeout!! Try again, or access it manually from here:[/]")
                print(request_url, '\n')
            elif 'There is no data available for this date range on this project' in html:
                rich.print(f"[bright_red]## Error:[/][bright_white] there is no data available for this date range on this Wikipedia.[/]\n")
            else: 
                rich.print(f"[bright_red]## Error:[/][bright_white] something unknown went wrong!! Please, try again!![/]\n")


    def top_edited_pages(wiki, period, filter, interval):
        try:
            wikis = Helper.get_Wikis_Codes()

            periods = {'last-month':'last-month'}

            if period not in periods:
                periods.update({period:period})

            filters = {'no-filter':'~total', 'page-type-content':'(page_type)~content', 'page-type-non-content':'(page_type)~non-content', 'page-type-all':'(page_type)~content*non-content',
                       'editor-type-user':'(editor_type)~user', 'editor-type-name-bot':'(editor_type)~name-bot', 'editor-type-anonymous':'(editor_type)~anonymous', 'editor-type-group-bot':
                       '(editor_type)~group-bot', 'editor-type-all':'(editor_type)~anonymous*group-bot*name-bot*user'}

            intervals = {'daily':'daily', 'monthly':'monthly'}

            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.manager.showWhenStarting", False)
            profile.set_preference("browser.download.dir", f"{os.getcwd()}")
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
            driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='geckodriver', service_log_path=os.devnull)

            base_url = f'https://stats.wikimedia.org/#/{wiki}.wikipedia.org/contributing/top-edited-pages/full|table|'
            parameters = f'{periods[period]}|{filters[filter]}|{intervals[interval]}'
            request_url = "".join([base_url, parameters])

            driver.implicitly_wait(5)
            driver.get(request_url)
            html = driver.page_source

            if intervals[interval]=='daily':
                sleep(10*2)
            if intervals[interval]=='monthly':
                sleep(10)

            csvFile = f"{(wikis[wiki]).lower()}--top-edited-pages--{filter}--{period}--{interval}.csv"
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
            rich.print(f"[bright_red]## Error:[/][bright_white] exiting due to pressing ctrl-c ...[/]\n")
            exit()

        except KeyError:
            if wiki not in wikis:
                rich.print(f"[bright_red]## Error:[/][bright_white] this Wikipedia: '{wiki}' is not supported. To list wiki codes use: `wikistats2csv -lw or --list-wikis`.[/]\n")
            elif period not in periods:
                rich.print(f"[bright_red]## Error:[/][bright_white] this time period: '{period}' is not supported. To list time periods use: `wikistats2csv -lp or --list-periods`[/]\n")
            elif filter not in filters:
                rich.print(f"[bright_red]## Error:[/][bright_white] this filter: '{filter}' is not supported. To list supported filters use: `wikistats2csv -lf or --list-filters`.[/]\n")
            elif interval not in intervals:
                rich.print(f"[bright_red]## Error:[/][bright_white] this time interval: '{interval}' is not supported. To list time intervals use: `wikistats2csv -li or --list-intervals`.[/]\n")
            else: 
                rich.print(f"[bright_red]## Error:[/][bright_white] one of these parameters: period-->'{period}', filter-->'{filter}', or interval-->'{interval}' is not supported.[/]\n")

        except selenium.common.exceptions.NoSuchElementException:
            rich.print(f"[bright_red]## Error:[/][bright_white] one of these parameters: period-->'{period}', filter-->'{filter}', or interval-->'{interval}' is not supported.[/]\n")

        except:
            if 'Loading metric...' in html:
                rich.print(f"[bright_red]## Error:[/][bright_white] cannot load and save this metric due to connection timeout!! Try again, or access it manually from here:[/]")
                print(request_url, '\n')
            elif 'There is no data available for this date range on this project' in html:
                rich.print(f"[bright_red]## Error:[/][bright_white] there is no data available for this date range on this Wikipedia.[/]\n")
            else: 
                rich.print(f"[bright_red]## Error:[/][bright_white] something unknown went wrong!! Please, try again!![/]\n")


    def active_editors_by_country(wiki, period, filter, interval):
        try:
            wikis = Helper.get_Wikis_Codes()

            periods = {'last-month':'last-month'}

            if period not in periods:
                periods.update({period:period})

            filters = {'activity-level-5-to-99-edits':'(activity-level)~5..99-edits', 'activity-level-100-or-more-edits':'(activity-level)~100..-edits'}

            intervals = {'monthly':'monthly'}

            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.manager.showWhenStarting", False)
            profile.set_preference("browser.download.dir", f"{os.getcwd()}")
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
            driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='geckodriver', service_log_path=os.devnull)

            base_url = f'https://stats.wikimedia.org/#/{wiki}.wikipedia.org/contributing/active-editors-by-country/full|table|'
            if filter=='activity-level-5-to-99-edits':
                parameters = f'{periods[period]}|(activity-level)~5..99-edits|{intervals[interval]}'
            elif filter=='activity-level-100-or-more-edits':
                parameters = f'{periods[period]}|(activity-level)~100..-edits|{intervals[interval]}'
            else:
                parameters = f'{periods[period]}|{filters[filter]}|{intervals[interval]}'
            request_url = "".join([base_url, parameters])

            driver.implicitly_wait(5)
            driver.get(request_url)
            html = driver.page_source

            if intervals[interval]=='daily':
                sleep(10*2)
            if intervals[interval]=='monthly':
                sleep(10)

            csvFile = f"{(wikis[wiki]).lower()}--active-editors-by-country--{filter}--{period}--{interval}.csv"
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
            rich.print(f"[bright_red]## Error:[/][bright_white] exiting due to pressing ctrl-c ...[/]\n")
            exit()

        except KeyError:
            if wiki not in wikis:
                rich.print(f"[bright_red]## Error:[/][bright_white] this Wikipedia: '{wiki}' is not supported. To list wiki codes use: `wikistats2csv -lw or --list-wikis`.[/]\n")
            elif period not in periods:
                rich.print(f"[bright_red]## Error:[/][bright_white] this time period: '{period}' is not supported. To list time periods use: `wikistats2csv -lp or --list-periods`[/]\n")
            elif filter not in filters:
                rich.print(f"[bright_red]## Error:[/][bright_white] this filter: '{filter}' is not supported. To list supported filters use: `wikistats2csv -lf or --list-filters`.[/]\n")
            elif interval not in intervals:
                rich.print(f"[bright_red]## Error:[/][bright_white] this time interval: '{interval}' is not supported. To list time intervals use: `wikistats2csv -li or --list-intervals`.[/]\n")
            else: 
                rich.print(f"[bright_red]## Error:[/][bright_white] one of these parameters: period-->'{period}', filter-->'{filter}', or interval-->'{interval}' is not supported.[/]\n")

        except selenium.common.exceptions.NoSuchElementException:
            rich.print(f"[bright_red]## Error:[/][bright_white] one of these parameters: period-->'{period}', filter-->'{filter}', or interval-->'{interval}' is not supported.[/]\n")

        except:
            if 'Loading metric...' in html:
                rich.print(f"[bright_red]## Error:[/][bright_white] cannot load and save this metric due to connection timeout!! Try again, or access it manually from here:[/]")
                print(request_url, '\n')
            elif 'There is no data available for this date range on this project' in html:
                rich.print(f"[bright_red]## Error:[/][bright_white] there is no data available for this date range on this Wikipedia.[/]\n")
            else: 
                rich.print(f"[bright_red]## Error:[/][bright_white] something unknown went wrong!! Please, try again!![/]\n")
