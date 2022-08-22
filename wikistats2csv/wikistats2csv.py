import sys
import rich
from .helper import Helper
from .content import Content
from .reading import Reading
from .contributing import Contributing
from .custom_argparse import ArgumentParser


def list_Wikis_Codes():
    wikis = Helper.get_Wikis_Codes()
    print(f"## List of `{len(wikis)}` Wikipedias and its languages codes:\n")
    for code, wiki in wikis.items():
        print(f"{wiki}:`{code}`", end=', ')
    print('\n') ; exit()


def main():

    rich.print('''
            [dodger_blue2]▌│║▌║▌█║▌║║▌│║▌│║▌║▌█║[/][spring_green4]▌█║▌║│▌║│▌║│█║│▌[/][dodger_blue2]║▌│█║▌│▌║│▌║║▌║▌█║▌║│▌[/]
            [dodger_blue2]▌│║▌║▌█║▌║║▌│║▌│║▌║▌█║[/][red]WIKISTATS-TO-CSV[/][dodger_blue2]║▌│█║▌│▌║│▌║║▌║▌█║▌║│▌[/]
            [dodger_blue2]▌│║▌║▌█║▌║║▌│║▌│║▌║▌█║[/][spring_green4]▌█║▌║│▌║│▌║│█║│▌[/][dodger_blue2]║▌│█║▌│▌║│▌║║▌║▌█║▌║│▌[/]
            ''')

    try:
        if sys.argv[1]=='-lw' or sys.argv[1]=='--list-wikis':
            list_Wikis_Codes()
    except IndexError:
        pass

    parser = ArgumentParser(add_help=False)
    parser.add_argument('-h', '--help', action='help', help='Show Help Message')
    parser.add_argument('-w', '--wiki', type=str, required=True, metavar='', help='Wikipedia Codes')
    parser.add_argument('-m', '--metric', type=str, required=True, metavar='', help='Wikipedia Metrics')
    parser.add_argument('-q', '--query', type=str, required=True, metavar='', help='Wikipedia Queries')
    parser.add_argument('-p', '--period', type=str, required=False, default='all-years', metavar='', help='Time Periods')
    parser.add_argument('-f', '--filter', type=str, required=False, default='no-filter', metavar='', help='Metrics Filters')
    parser.add_argument('-i', '--interval', type=str, required=False, default='monthly', metavar='', help='Time Intervals')
    parser.add_argument('-lw', '--list-wikis', type=str, required=False, metavar='', help='List Wikipedias')
    
    try:
        args = parser.parse_args()
    
        if args.wiki!=None:

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
                        print("\u001b[91mError:\u001b[0m query `top-media-requests` has only one pre-defined time period: 'last-month'.\n")

                else:
                    print(f"\u001b[91mError:\u001b[0m wikistats2csv metric `content` does not support this query: '{args.query}'.\n")

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
                        print("\u001b[91mError:\u001b[0m query `page-views-by-country` has one pre-defined time period: 'last-month'.\n")

                elif args.query=='unique-devices':
                    Reading.unique_devices(args.wiki, args.period, args.filter, args.interval)

                elif args.query=='top-viewed-articles':
                    if args.period=='last-month':
                        Reading.top_viewed_articles(args.wiki, args.period, args.filter, args.interval)
                    elif args.period!=None and args.period!='all-years':
                        Reading.top_viewed_articles(args.wiki, args.period, args.filter, args.interval)
                    else:
                        print("\u001b[91mError:\u001b[0m query `top-viewed-articles` has one pre-defined time period: 'last-month'.\n")

                else:
                    print(f"\u001b[91mError:\u001b[0m wikistats2csv metric `reading` does not support this query: '{args.query}'.\n")

            elif args.metric=='contributing':
                if args.query=='editors':
                    Contributing.editors(args.wiki, args.period, args.filter, args.interval)

                elif args.query=='active-editors':
                    Contributing.active_editors(args.wiki, args.period, args.filter, args.interval)

                elif args.query=='edits':
                    Contributing.edits(args.wiki, args.period, args.filter, args.interval)

                elif args.query=='user-edits':
                    Contributing.user_edits(args.wiki, args.period, args.filter, args.interval)

                elif args.query=='new-pages':
                    Contributing.new_pages(args.wiki, args.period, args.filter, args.interval)

                elif args.query=='new-registered-users':
                    Contributing.new_registered_users(args.wiki, args.period, args.filter, args.interval)

                elif args.query=='top-editors':
                    if args.period=='last-month':
                        Contributing.top_editors(args.wiki, args.period, args.filter, args.interval)
                    elif args.period!=None and args.period!='all-years':
                        Contributing.top_editors(args.wiki, args.period, args.filter, args.interval)
                    else:
                        print("\u001b[91mError:\u001b[0m query  `top-editors`  has  only  one  pre-defined  time period: 'last-month'.\n")

                elif args.query=='top-edited-pages':
                    if args.period=='last-month':
                        Contributing.top_edited_pages(args.wiki, args.period, args.filter, args.interval)
                    elif args.period!=None and args.period!='all-years':
                        Contributing.top_edited_pages(args.wiki, args.period, args.filter, args.interval)
                    else:
                        print("\u001b[91mError:\u001b[0m query  `top-edited-pages`  has  only  one  pre-defined  time period: 'last-month'.\n")

                elif args.query=='active-editors-by-country':
                    if args.period=='last-month':
                        if args.filter!='no-filter':
                            Contributing.active_editors_by_country(args.wiki, args.period, args.filter, args.interval)
                        else:
                            print("\u001b[91mError:\u001b[0m query  `active-editors-by-country`  has  only  two  pre-defined  filters:")
                            print("       Use: 'activity-level-5-to-99-edits' or 'activity-level-100-or-more-edits'.\n")
                    elif args.period!=None and args.period!='all-years':
                        Contributing.active_editors_by_country(args.wiki, args.period, args.filter, args.interval)
                    else:
                        print("\u001b[91mError:\u001b[0m query `active-editors-by-country` has one pre-defined time period: 'last-month'.\n")

                else:
                    print(f"\u001b[91mError:\u001b[0m wikistats2csv metric `contributing` does not support this query: '{args.query}'.\n")
            
            else:
                print(f"\u001b[91mError:\u001b[0m wikistats2csv does not support this metric: '{args.metric}'.\n")

    except SystemExit:
        print('')


if __name__ == "__main__":
    main()