import sys , os
import argparse
from Content import *
from Reading import *

# os.system(f"{sys.executable} -m pip install -q pyyaml==6.0 pandas==1.4.3 selenium==3.141.0")

parser = argparse.ArgumentParser(description="Wikistats-to-CSV tool downloads Wikipedia Statistics in CSV format.")
parser.add_argument('-w', '--wiki', type=str, required=True, metavar='', help='Wikipedia Code: [en -> English, ar -> Arabic, ...]')
parser.add_argument('-m', '--metric', type=str, required=True, metavar='', help='Wikipedia Metrics: [reading, content, contributing]')
parser.add_argument('-q', '--query', type=str, required=True, metavar='', help='Wikipedia Queries: [pages-to-date, edited-pages, ...]')
parser.add_argument('-p', '--period', type=str, required=False, default='all-years', metavar='', help='Time Period: [all, one-year, one-month, ...]')
parser.add_argument('-f', '--filter', type=str, required=False, default='no-filter', metavar='', help='Metrics Filters: [no-filter, page-type-all, ...]')
parser.add_argument('-i', '--interval', type=str, required=False, default='monthly', metavar='', help='Time Interval: [daily, monthly]')
args = parser.parse_args()


if __name__ == "__main__":

    print('''
              ▌│║▌║▌█║▌║║▌│║▌│║▌║▌█║▌█║▌║│▌║│▌║│█║│▌║▌│█║▌│▌║│▌║║▌║▌█║▌║│▌
              ▌│║▌║▌█║▌║║▌│║▌│║▌║▌█║WIKISTATS-TO-CSV║▌│█║▌│▌║│▌║║▌║▌█║▌║│▌
              ▌│║▌║▌█║▌║║▌│║▌│║▌║▌█║▌█║▌║│▌║│▌║│█║│▌║▌│█║▌│▌║│▌║║▌║▌█║▌║│▌
          ''')

    if args.metric=='content':
        if args.query=='pages-to-date':
            Content.pages_to_date(args.wiki, args.period, args.filter, args.interval)
    
        elif args.query=='edited-pages':
            Content.edited_pages(args.wiki, args.period, args.filter, args.interval)
    
        elif args.query=='absolute-bytes-difference':
            Content.absolute_bytes_difference(args.wiki, args.period, args.filter, args.interval)

        elif args.query=='net-bytes-difference':
            Content.net_bytes_difference(args.wiki, args.period, args.filter, args.interval)

        elif args.query=='total-media-requests':
            Content.total_media_requests(args.wiki, args.period, args.filter, args.interval)

        elif args.query=='top-media-requests':
            if args.period=='last-month':
                Content.top_media_requests(args.wiki, args.period, args.filter, args.interval)
            elif args.period!=None and args.period!='all-years':
                Content.top_media_requests(args.wiki, args.period, args.filter, args.interval)
            else:
                print("## Error: query `top-media-requests` has only one pre-defined time period 'last-month'.")
                print("          You can specify a 30-day time period between two dates following this format:")
                print("          `YYYY-MM-DD~YYYY-MM-DD`. For example, you can use: '2022-01-01~2022-01-30'.\n")

        else:
            print('## Error: metric `content` does not have this type of query.\n')

    elif args.metric=='reading':
        if args.query=='total-page-views':
            Reading.total_page_views(args.wiki, args.period, args.filter, args.interval)
        
        elif args.query=='legacy-page-views':
            Reading.legacy_page_views(args.wiki, args.period, args.filter, args.interval)

        elif args.query=='page-views-by-country':
            if args.period=='last-month':
                Reading.page_views_by_country(args.wiki, args.period, args.filter, args.interval)
            elif args.period!=None and args.period!='all-years':
                Reading.page_views_by_country(args.wiki, args.period, args.filter, args.interval)
            else:
                print("## Error: query `page-views-by-country` has one pre-defined time period 'last-month'.")
                print("          You can specify a 30-day time period between two dates following this format:")
                print("          `YYYY-MM-DD~YYYY-MM-DD`. For example, you can use: '2022-01-01~2022-01-30'.\n")

        elif args.query=='unique-devices':
            Reading.unique_devices(args.wiki, args.period, args.filter, args.interval)

        elif args.query=='top-viewed-articles':
            if args.period=='last-month':
                Reading.top_viewed_articles(args.wiki, args.period, args.filter, args.interval)
            elif args.period!=None and args.period!='all-years':
                Reading.top_viewed_articles(args.wiki, args.period, args.filter, args.interval)
            else:
                print("## Error: query `page-views-by-country` has one pre-defined time period 'last-month'.")
                print("          You can specify a 30-day time period between two dates following this format:")
                print("          `YYYY-MM-DD~YYYY-MM-DD`. For example, you can use: '2022-01-01~2022-01-30'.\n")

            
        else:
            print('## Error: metric `reading` does not have this type of query.\n')


    else:
        print('## Error: Wikistats-to-CSV does not have this type of metric.\n')

