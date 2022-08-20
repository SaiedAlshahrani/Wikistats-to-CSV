from itertools import islice
from wikistats2csv import Helper
from wikistats2csv import Content


def absolute_bytes_difference__test():
    wikis = Helper.get_Wikis_Codes()
    # Select only the 1st Wiki.
    wikis = list(islice(wikis, 1))
    periods = {'all-years':'all', 'one-year':'1-year', 'two-years':'2-year', 'three-months':'3-month', 'one-month':'1-month'}
    filters = {'no-filter':'~total', 'page-type-content':'page_type~content', 'page-type-non-content':'page_type~non-content', 'page-type-all':'page_type~content*non-content',
                'editor-type-user':'editor_type~user', 'editor-type-name-bot':'editor_type~name-bot', 'editor-type-anonymous':'editor_type~anonymous', 'editor-type-group-bot':
                'editor_type~group-bot', 'editor-type-all':'editor_type~anonymous*group-bot*name-bot*user'}
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
                    Content_Metrics.absolute_bytes_difference(wiki=wikis[wiki], period=period, filter=filter, interval=interval)
                    print('\n')


def edited_pages__test():
    wikis = Helper.get_Wikis_Codes()
    # Select only the 1st Wiki.
    wikis = list(islice(wikis, 1))
    periods = {'all-years':'all', 'one-year':'1-year', 'two-years':'2-year', 'three-months':'3-month', 'one-month':'1-month'}
    filters = {'no-filter':'~total', 'page-type-content':'page_type~content', 'page-type-non-content':'page_type~non-content', 'page-type-all':'page_type~content*non-content',
                'editor-type-user':'editor_type~user', 'editor-type-name-bot':'editor_type~name-bot', 'editor-type-anonymous':'editor_type~anonymous', 'editor-type-group-bot':
                'editor_type~group-bot', 'editor-type-all':'editor_type~anonymous*group-bot*name-bot*user', 'activity-level-1-to-4-edits':'activity_level~1..4-edits',
                'activity-level-5-to-24-edits':'activity_level~5..24-edits', 'activity-level-25-to-99-edits':'activity_level~25..99-edits',
                'activity-level-100-or-more-edits':'activity_level~100..-edits', 'activity-level-all':'activity_level~1..4-edits*5..24-edits*25..99-edits*100..-edits'}
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
                    Content_Metrics.edited_pages(wiki=wikis[wiki], period=period, filter=filter, interval=interval)
                    print('\n')


def net_bytes_difference__test():
    wikis = Helper.get_Wikis_Codes()
    # Select only the 1st Wiki.
    wikis = list(islice(wikis, 1))
    periods = {'all-years':'all', 'one-year':'1-year', 'two-years':'2-year', 'three-months':'3-month', 'one-month':'1-month'}
    filters = {'no-filter':'~total', 'page-type-content':'page_type~content', 'page-type-non-content':'page_type~non-content', 'page-type-all':'page_type~content*non-content',
                'editor-type-user':'editor_type~user', 'editor-type-name-bot':'editor_type~name-bot', 'editor-type-anonymous':'editor_type~anonymous', 'editor-type-group-bot':
                'editor_type~group-bot', 'editor-type-all':'editor_type~anonymous*group-bot*name-bot*user'}
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
                    Content_Metrics.net_bytes_difference(wiki=wikis[wiki], period=period, filter=filter, interval=interval)
                    print('\n')


def pages_to_date__test():
    wikis = Helper.get_Wikis_Codes()
    # Select only the 1st Wiki.
    wikis = list(islice(wikis, 1))
    periods = {'all-years':'all', 'one-year':'1-year', 'two-years':'2-year', 'three-months':'3-month', 'one-month':'1-month'}
    filters = {'no-filter':'~total', 'page-type-content':'page_type~content', 'page-type-non-content':'page_type~non-content', 'page-type-all':'page_type~content*non-content',
               'editor-type-user':'editor_type~user', 'editor-type-name-bot':'editor_type~name-bot', 'editor-type-anonymous':'editor_type~anonymous', 'editor-type-group-bot':
               'editor_type~group-bot', 'editor-type-all':'editor_type~anonymous*group-bot*name-bot*user'}
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
                    Content_Metrics.pages_to_date(wiki=wikis[wiki], period=period, filter=filter, interval=interval)
                    print('\n')


def total_media_requests__test():
    wikis = Helper.get_Wikis_Codes()
    # Select only the 1st Wiki.
    wikis = list(islice(wikis, 1))
    periods = {'all-years':'all', 'one-year':'1-year', 'two-years':'2-year', 'three-months':'3-month', 'one-month':'1-month'}
    filters = {'no-filter':'~total', 'media-type-image':'media_type~image', 'media-type-video':'media_type~video', 'media-type-audio':'media_type~audio',
                'media-type-document':'media_type~document', 'media-type-other':'media_type~other', 'media-type-all':'media_type~image*video*audio*document*other',
                'agent-type-user':'agent~user', 'agent-type-spider':'agent~spider', 'agent-type-all':'agent~user*spider'}
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
                    Content_Metrics.total_media_requests(wiki=wikis[wiki], period=period, filter=filter, interval=interval)
                    print('\n')


def top_media_requests__test():
    wikis = Helper.get_Wikis_Codes()
    # Select only the 1st Wiki.
    wikis = list(islice(wikis, 1))
    periods = {'last-month':'last-month'}
    filters = {'no-filter':'~total', 'media-type-image':'(media_type)~image', 'media-type-video':'(media_type)~video', 'media-type-audio':'(media_type)~audio',
                'media-type-document':'(media_type)~document', 'media-type-other':'(media_type)~other', 'media-type-all':'(media_type)~image*video*audio*document*other'}
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
                    Content_Metrics.top_media_requests(wiki=wikis[wiki], period=period, filter=filter, interval=interval)
                    print('\n')


if __name__ == "__main__":
    print("$$$ Testing: `absolute_bytes_difference(wiki, period, filter, interval)`:")
    absolute_bytes_difference__test()

    print("$$$ Testing: `edited_pages(wiki, period, filter, interval)`:")
    edited_pages__test()

    print("$$$ Testing: `net_bytes_difference(wiki, period, filter, interval)`:")
    net_bytes_difference__test()

    print("$$$ Testing: `pages_to_date(wiki, period, filter, interval)`:")
    pages_to_date__test()

    print("$$$ Testing: `total_media_requests(wiki, period, filter, interval)`:")
    total_media_requests__test()

    print("$$$ Testing: `top_media_requests(wiki, period, filter, interval)`:")
    top_media_requests__test()
