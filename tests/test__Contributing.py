from Helper import *
from Contributing import *
from itertools import islice


def editors__test():
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
                    Contributing_Metrics.editors(wiki=wikis[wiki], period=period, filter=filter, interval=interval)
                    print('\n')


def active_editors__test():
    wikis = Helper.get_Wikis_Codes()
    # Select only the 1st Wiki.
    wikis = list(islice(wikis, 1))
    periods = {'all-years':'all', 'one-year':'1-year', 'two-years':'2-year', 'three-months':'3-month', 'one-month':'1-month'}
    filters = {'no-filter':'~total', 'page-type-content':'page_type~content', 'page-type-non-content':'page_type~non-content', 'page-type-all':'page_type~content*non-content'}
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
                    Contributing_Metrics.active_editors(wiki=wikis[wiki], period=period, filter=filter, interval=interval)
                    print('\n')


def edits__test():
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
                    Contributing_Metrics.edits(wiki=wikis[wiki], period=period, filter=filter, interval=interval)
                    print('\n')


def user_edits__test():
    wikis = Helper.get_Wikis_Codes()
    # Select only the 1st Wiki.
    wikis = list(islice(wikis, 1))
    periods = {'all-years':'all', 'one-year':'1-year', 'two-years':'2-year', 'three-months':'3-month', 'one-month':'1-month'}
    filters = {'no-filter':'~total', 'page-type-content':'page_type~content', 'page-type-non-content':'page_type~non-content', 'page-type-all':'page_type~content*non-content'}
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
                    Contributing_Metrics.user_edits(wiki=wikis[wiki], period=period, filter=filter, interval=interval)
                    print('\n')


def new_pages__test():
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
                    Contributing_Metrics.new_pages(wiki=wikis[wiki], period=period, filter=filter, interval=interval)
                    print('\n')


def new_registered_users__test():
    wikis = Helper.get_Wikis_Codes()
    # Select only the 1st Wiki.
    wikis = list(islice(wikis, 1))
    periods = {'all-years':'all', 'one-year':'1-year', 'two-years':'2-year', 'three-months':'3-month', 'one-month':'1-month'}
    filters = {'no-filter':'~total'}
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
                    Contributing_Metrics.new_registered_users(wiki=wikis[wiki], period=period, filter=filter, interval=interval)
                    print('\n')


def top_editors__test():
    wikis = Helper.get_Wikis_Codes()
    # Select only the 1st Wiki.
    wikis = list(islice(wikis, 1))
    periods = {'last-month':'last-month'}
    filters = {'no-filter':'~total', 'page-type-content':'(page_type)~content', 'page-type-non-content':'(page_type)~non-content', 'page-type-all':'(page_type)~content*non-content', 
                'editor-type-user':'(editor_type)~user', 'editor-type-name-bot':'(editor_type)~name-bot', 'editor-type-anonymous':'(editor_type)~anonymous', 'editor-type-group-bot':
                '(editor_type)~group-bot', 'editor-type-all':'(editor_type)~anonymous*group-bot*name-bot*user'}
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
                    Contributing_Metrics.top_editors(wiki=wikis[wiki], period=period, filter=filter, interval=interval)
                    print('\n')


def top_edited_pages__test():
    wikis = Helper.get_Wikis_Codes()
    # Select only the 1st Wiki.
    wikis = list(islice(wikis, 1))
    periods = {'last-month':'last-month'}
    filters = {'no-filter':'~total', 'page-type-content':'(page_type)~content', 'page-type-non-content':'(page_type)~non-content', 'page-type-all':'(page_type)~content*non-content', 
                'editor-type-user':'(editor_type)~user', 'editor-type-name-bot':'(editor_type)~name-bot', 'editor-type-anonymous':'(editor_type)~anonymous', 'editor-type-group-bot':
                '(editor_type)~group-bot', 'editor-type-all':'(editor_type)~anonymous*group-bot*name-bot*user'}
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
                    Contributing_Metrics.top_edited_pages(wiki=wikis[wiki], period=period, filter=filter, interval=interval)
                    print('\n')


def active_editors_by_country__test():
    wikis = Helper.get_Wikis_Codes()
    # Select only the 1st Wiki.
    wikis = list(islice(wikis, 1))
    periods = {'last-month':'last-month'}
    filters = {'activity-level-5-to-99-edits':'(activity-level)~5..99-edits', 'activity-level-100-or-more-edits':'(activity-level)~100..-edits'}
    intervals = {'monthly':'monthly'}
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
                    Contributing_Metrics.active_editors_by_country(wiki=wikis[wiki], period=period, filter=filter, interval=interval)
                    print('\n')


if __name__ == "__main__":
    print("$$$ Testing: `editors(wiki, period, filter, interval)`:")
    editors__test()

    print("$$$ Testing: `active_editors(wiki, period, filter, interval)`:")
    active_editors__test()

    print("$$$ Testing: `edits(wiki, period, filter, interval)`:")
    edits__test()

    print("$$$ Testing: `user_edits(wiki, period, filter, interval)`:")
    user_edits__test()

    print("$$$ Testing: `new_pages(wiki, period, filter, interval)`:")
    new_pages__test()

    print("$$$ Testing: `new_registered_users(wiki, period, filter, interval)`:")
    new_registered_users__test()

    print("$$$ Testing: `top_editors(wiki, period, filter, interval)`:")
    top_editors__test()

    print("$$$ Testing: `top_edited_pages(wiki, period, filter, interval)`:")
    top_edited_pages__test()

    print("$$$ Testing: `active_editors_by_country(wiki, period, filter, interval)`:")
    active_editors_by_country__test()