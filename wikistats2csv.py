import rich , argparse
from .content import Content
from .reading import Reading
from .contributing import Contributing


def main():
    parser = argparse.ArgumentParser(description="Wikistats-to-CSV downloads Wikipedia Statistics in CSV format.")
    parser.add_argument('-w', '--wiki', type=str, required=True, metavar='', help='Wikipedia Code: [en -> English, ar -> Arabic, ...]')
    parser.add_argument('-m', '--metric', type=str, required=True, metavar='', help='Wikipedia Metrics: [reading, content, contributing]')
    parser.add_argument('-q', '--query', type=str, required=True, metavar='', help='Wikipedia Queries: [pages-to-date, edited-pages, ...]')
    parser.add_argument('-p', '--period', type=str, required=False, default='all-years', metavar='', help='Time Period: [all, one-year, one-month, ...]')
    parser.add_argument('-f', '--filter', type=str, required=False, default='no-filter', metavar='', help='Metrics Filters: [no-filter, page-type-all, ...]')
    parser.add_argument('-i', '--interval', type=str, required=False, default='monthly', metavar='', help='Time Interval: [daily, monthly]')
    args = parser.parse_args()

    rich.print('''
              [dodger_blue2]▌│║▌║▌█║▌║║▌│║▌│║▌║▌█║[/][spring_green4]▌█║▌║│▌║│▌║│█║│▌[/][dodger_blue2]║▌│█║▌│▌║│▌║║▌║▌█║▌║│▌[/]
              [dodger_blue2]▌│║▌║▌█║▌║║▌│║▌│║▌║▌█║[/][red]WIKISTATS-TO-CSV[/][dodger_blue2]║▌│█║▌│▌║│▌║║▌║▌█║▌║│▌[/]
              [dodger_blue2]▌│║▌║▌█║▌║║▌│║▌│║▌║▌█║[/][spring_green4]▌█║▌║│▌║│▌║│█║│▌[/][dodger_blue2]║▌│█║▌│▌║│▌║║▌║▌█║▌║│▌[/]
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
                rich.print("[bright_red]## Error:[/][bright_white] query `top-media-requests` has only one pre-defined time period 'last-month'.[/]")
                print("          You can specify a 30-day time period between two dates following this format:")
                print("          `YYYY-MM-DD~YYYY-MM-DD`. For example, you can use: '2022-01-01~2022-01-30'.\n")

        else:
            rich.print("[bright_red]## Error:[/][bright_white] metric `content` does not have this type of query.\n[/]")

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
                rich.print("[bright_red]## Error:[/][bright_white] query `page-views-by-country` has one pre-defined time period 'last-month'.[/]")
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
                rich.print("[bright_red]## Error:[/][bright_white] query `page-views-by-country` has one pre-defined time period 'last-month'.[/]")
                print("          You can specify a 30-day time period between two dates following this format:")
                print("          `YYYY-MM-DD~YYYY-MM-DD`. For example, you can use: '2022-01-01~2022-01-30'.\n")

        else:
            rich.print("[bright_red]## Error:[/][bright_white] metric `reading` does not have this type of query.\n[/]")

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
                rich.print("[bright_red]## Error:[/][bright_white] query  `top-editors`  has  only  one  pre-defined  time period  'last-month'.[/]")
                print("          You can specify a 30-day time period between two dates following this format:")
                print("          `YYYY-MM-DD~YYYY-MM-DD`. For example, you can use: '2022-01-01~2022-01-30'.\n")

        elif args.query=='top-edited-pages':
            if args.period=='last-month':
                Contributing.top_edited_pages(args.wiki, args.period, args.filter, args.interval)
            elif args.period!=None and args.period!='all-years':
                Contributing.top_edited_pages(args.wiki, args.period, args.filter, args.interval)
            else:
                rich.print("[bright_red]## Error:[/][bright_white] query  `top-editors`  has  only  one  pre-defined  time period  'last-month'.[/]")
                print("          You can specify a 30-day time period between two dates following this format:")
                print("          `YYYY-MM-DD~YYYY-MM-DD`. For example, you can use: '2022-01-01~2022-01-30'.\n")

        elif args.query=='active-editors-by-country':
            if args.period=='last-month':
                if args.filter!='no-filter':
                    Contributing.active_editors_by_country(args.wiki, args.period, args.filter, args.interval)
                else:
                    rich.print("[bright_red]## Error:[/][bright_white] query  `active-editors-by-country`  has  only  two  pre-defined  filters:[/]")
                    print("          Use: 'activity-level-5-to-99-edits' or 'activity-level-100-or-more-edits'.\n")
            elif args.period!=None and args.period!='all-years':
                Contributing.active_editors_by_country(args.wiki, args.period, args.filter, args.interval)
            else:
                rich.print("[bright_red]## Error:[/][bright_white] query `active-editors-by-country` has one pre-defined time period 'last-month'.[/]")
                print("          You can specify a 30-day time period between two dates following this format:")
                print("          `YYYY-MM-DD~YYYY-MM-DD`. For example, you can use: '2022-01-01~2022-01-30'.\n")

        else:
            rich.print("[bright_red]## Error:[/][bright_white] metric `contributing` does not have this type of query.\n[/]")

    else:
        rich.print("[bright_red]## Error:[/][bright_white] Wikistats-to-CSV does not have this type of metric.\n[/]")


if __name__ == "__main__":
    main()
