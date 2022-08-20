from itertools import islice
from wikistats2csv import Helper
from wikistats2csv import Reading


def total_page_views__test():
    wikis = Helper.get_Wikis_Codes()
    # Select only the 1st Wiki.
    wikis = list(islice(wikis, 1))
    periods = {'all-years':'all', 'one-year':'1-year', 'two-years':'2-year', 'three-months':'3-month', 'one-month':'1-month'}
    filters = {'no-filter':'~total', 'access-method-desktop':'access~desktop', 'access-method-mobile-app':'access~mobile-app',
                       'access-method-mobile-web':'access~mobile-web', 'access-method-all':'access~desktop*mobile-app*mobile-web',
                       'agent-type-user':'agent~user', 'agent-type-spider':'agent~spider', 'agent-type-automated':'agent~automated',
                       'agent-type-all':'agent~user*spider*automated'}
    intervals = {'daily':'daily', 'monthly':'monthly'}
    counter=0
    for wiki in range(len(wikis)):
        for p in periods:
            period=list(periods.keys())[list(periods.values()).index(periods[p])]
            for f in filters:
                filter=list(filters.keys())[list(filters.values()).index(filters[f])]
                for i in intervals:
                    interval=list(intervals.keys())[list(intervals.values()).index(intervals[i])]
                    counter+=1
                    print(f'@@ Iteration #{counter}:  wiki=`{wikis[wiki]}`,  period=`{period}`,  filter=`{filter}`,  interval=`{interval}`:')
                    Reading_Metrics.total_page_views(wiki=wikis[wiki], period=period, filter=filter, interval=interval)
                    print('\n')


def legacy_page_views__test():
    wikis = Helper.get_Wikis_Codes()
    # Select only the 1st Wiki.
    wikis = list(islice(wikis, 1))
    periods = {'all-years':'all', 'one-year':'1-year', 'two-years':'2-year', 'three-months':'3-month', 'one-month':'1-month'}
    filters = {'no-filter':'~total', 'access-site-mobile-site':'(access-site)~mobile-site', 'access-site-desktop-site':
                       '(access-site)~desktop-site', 'access-site-all':'(access-site)~mobile-site*desktop-site'}
    intervals = {'daily':'daily', 'monthly':'monthly'}
    counter=0
    for wiki in range(len(wikis)):
        for p in periods:
            period=list(periods.keys())[list(periods.values()).index(periods[p])]
            for f in filters:
                filter=list(filters.keys())[list(filters.values()).index(filters[f])]
                for i in intervals:
                    interval=list(intervals.keys())[list(intervals.values()).index(intervals[i])]
                    counter+=1
                    print(f'@@ Iteration #{counter}:  wiki=`{wikis[wiki]}`,  period=`{period}`,  filter=`{filter}`,  interval=`{interval}`:')
                    Reading_Metrics.legacy_page_views(wiki=wikis[wiki], period=period, filter=filter, interval=interval)
                    print('\n')


def page_views_by_country__test():
    wikis = Helper.get_Wikis_Codes()
    # Select only the 1st Wiki.
    wikis = list(islice(wikis, 1))
    periods = {'last-month':'last-month'}
    filters = {'no-filter':'~total', 'access-method-desktop':'(access)~desktop', 'access-method-mobile-app':'(access)~mobile-app',
                'access-method-mobile-web':'(access)~mobile-web', 'access-method-all':'(access)~desktop*mobile-app*mobile-web'}
    intervals = {'daily':'daily', 'monthly':'monthly'}
    counter=0
    for wiki in range(len(wikis)):
        for p in periods:
            period=list(periods.keys())[list(periods.values()).index(periods[p])]
            for f in filters:
                filter=list(filters.keys())[list(filters.values()).index(filters[f])]
                for i in intervals:
                    interval=list(intervals.keys())[list(intervals.values()).index(intervals[i])]
                    counter+=1
                    print(f'@@ Iteration #{counter}:  wiki=`{wikis[wiki]}`,  period=`{period}`,  filter=`{filter}`,  interval=`{interval}`:')
                    Reading_Metrics.page_views_by_country(wiki=wikis[wiki], period=period, filter=filter, interval=interval)
                    print('\n')


def unique_devices__test():
    wikis = Helper.get_Wikis_Codes()
    # Select only the 1st Wiki.
    wikis = list(islice(wikis, 1))
    periods = {'all-years':'all', 'one-year':'1-year', 'two-years':'2-year', 'three-months':'3-month', 'one-month':'1-month'}
    filters = {'no-filter':'~total', 'access-site-mobile-site':'(access-site)~mobile-site', 'access-site-desktop-site':
                '(access-site)~desktop-site', 'access-site-all':'(access-site)~mobile-site*desktop-site'}
    intervals = {'daily':'daily', 'monthly':'monthly'}
    counter=0
    for wiki in range(len(wikis)):
        for p in periods:
            period=list(periods.keys())[list(periods.values()).index(periods[p])]
            for f in filters:
                filter=list(filters.keys())[list(filters.values()).index(filters[f])]
                for i in intervals:
                    interval=list(intervals.keys())[list(intervals.values()).index(intervals[i])]
                    counter+=1
                    print(f'@@ Iteration #{counter}:  wiki=`{wikis[wiki]}`,  period=`{period}`,  filter=`{filter}`,  interval=`{interval}`:')
                    Reading_Metrics.unique_devices(wiki=wikis[wiki], period=period, filter=filter, interval=interval)
                    print('\n')


def top_viewed_articles__test():
    wikis = Helper.get_Wikis_Codes()
    # Select only the 1st Wiki.
    wikis = list(islice(wikis, 1))
    periods = {'last-month':'last-month'}
    filters = {'no-filter':'~total', 'access-method-desktop':'(access)~desktop', 'access-method-mobile-app':'(access)~mobile-app',
                'access-method-mobile-web':'(access)~mobile-web', 'access-method-all':'(access)~desktop*mobile-app*mobile-web'}
    intervals = {'daily':'daily', 'monthly':'monthly'}
    counter=0
    for wiki in range(len(wikis)):
        for p in periods:
            period=list(periods.keys())[list(periods.values()).index(periods[p])]
            for f in filters:
                filter=list(filters.keys())[list(filters.values()).index(filters[f])]
                for i in intervals:
                    interval=list(intervals.keys())[list(intervals.values()).index(intervals[i])]
                    counter+=1
                    print(f'@@ Iteration #{counter}:  wiki=`{wikis[wiki]}`,  period=`{period}`,  filter=`{filter}`,  interval=`{interval}`:')
                    Reading_Metrics.top_viewed_articles(wiki=wikis[wiki], period=period, filter=filter, interval=interval)
                    print('\n')


if __name__ == "__main__":
    print("$$$ Testing: `total_page_views(wiki, period, filter, interval)`:")
    total_page_views__test()

    print("$$$ Testing: `legacy_page_views(wiki, period, filter, interval)`:")
    legacy_page_views__test()

    print("$$$ Testing: `page_views_by_country(wiki, period, filter, interval)`:")
    page_views_by_country__test()

    print("$$$ Testing: `unique_devices(wiki, period, filter, interval)`:")
    unique_devices__test()

    print("$$$ Testing: `top_viewed_articles(wiki, period, filter, interval)`:")
    top_viewed_articles__test()
