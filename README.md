# Wikistats-to-CSV

![alt text](https://github.com/SaiedAlshahrani/Wikistats-to-CSV/blob/main/images/wikistats2csv-logo.png?raw=true)

## Install:

Wikistats-to-CSV (wikistats2csv) requires Python >=3 and the installation of a few Python packages such as `lxml==4.9.1`, `rich==12.5.1`, `numpy==1.23.2`, `pandas==1.4.3`, `selenium==3.141.0`, and `geckodriver-autoinstaller==0.1.0`. For convenience, we included the installation of these packages as a part of the setup process of Wikistats-to-CSV (wikistats2csv).  If you encounter installation errors, you might need to install these packages using `pip` manually. 

```bash
python3 -m pip install -r requirements.txt
```

To download Wikistats-to-CSV (wikistats2csv) using `pip` command , we highly recommend you first upgrade the `pip` command to the latest version.

```bash
python3 -m pip install --upgrade pip
python3 -m pip install wikistats2csv
```

If you encounter a warning of "*WARNING: the script is installed in '/Users/.../.../bin' which is not on path*", then you need to add the displayed path "/Users/.../.../bin" to the `$PATH` variable using this command: 

```bash
export PATH="/Users/.../.../bin:$PATH"
```

## Usage:

### * As CLI:

#### >> Long Flags:

```bash
$ wikistats2csv --wiki en --metric content --query pages-to-date --period all-years --filter page-type-all --interval monthly

              ▌│║▌║▌█║▌║║▌│║▌│║▌║▌█║▌█║▌║│▌║│▌║│█║│▌║▌│█║▌│▌║│▌║║▌║▌█║▌║│▌
              ▌│║▌║▌█║▌║║▌│║▌│║▌║▌█║WIKISTATS-TO-CSV║▌│█║▌│▌║│▌║║▌║▌█║▌║│▌
              ▌│║▌║▌█║▌║║▌│║▌│║▌║▌█║▌█║▌║│▌║│▌║│█║│▌║▌│█║▌│▌║│▌║║▌║▌█║▌║│▌

## Downloaded `english--pages-to-date--page-type-all--all-years--monthly.csv` successfully :-)

** Quick glance at `english--pages-to-date--page-type-all--all-years--monthly.csv` file:
                        month  total.non-content  total.content           timeRange.start             timeRange.end
0    2001-01-01T00:00:00.000Z                 28             37  2001-01-01T00:00:00.000Z  2001-02-01T00:00:00.000Z
1    2001-02-01T00:00:00.000Z                 51            175  2001-02-01T00:00:00.000Z  2001-03-01T00:00:00.000Z
..                        ...                ...            ...                       ...                       ...
257  2022-06-01T00:00:00.000Z           36945305        6518484  2022-06-01T00:00:00.000Z  2022-07-01T00:00:00.000Z
258  2022-07-01T00:00:00.000Z           37088260        6534151  2022-07-01T00:00:00.000Z  2022-08-01T00:00:00.000Z
```

#### >> Short Flags:

```bash
$ wikistats2csv -w ar -m content -q pages-to-date -p all-years -f page-type-all -i monthly

              ▌│║▌║▌█║▌║║▌│║▌│║▌║▌█║▌█║▌║│▌║│▌║│█║│▌║▌│█║▌│▌║│▌║║▌║▌█║▌║│▌
              ▌│║▌║▌█║▌║║▌│║▌│║▌║▌█║WIKISTATS-TO-CSV║▌│█║▌│▌║│▌║║▌║▌█║▌║│▌
              ▌│║▌║▌█║▌║║▌│║▌│║▌║▌█║▌█║▌║│▌║│▌║│█║│▌║▌│█║▌│▌║│▌║║▌║▌█║▌║│▌

## Downloaded `arabic--pages-to-date--page-type-all--all-years--monthly.csv` successfully :-)

** Quick glance at `arabic--pages-to-date--page-type-all--all-years--monthly.csv` file:
                        month  total.non-content  total.content           timeRange.start             timeRange.end
0    2001-01-01T00:00:00.000Z                  0            591  2001-01-01T00:00:00.000Z  2001-02-01T00:00:00.000Z
1    2001-02-01T00:00:00.000Z                  0            591  2001-02-01T00:00:00.000Z  2001-03-01T00:00:00.000Z
..                        ...                ...            ...                       ...                       ...
257  2022-06-01T00:00:00.000Z            5508072        1173410  2022-06-01T00:00:00.000Z  2022-07-01T00:00:00.000Z
258  2022-07-01T00:00:00.000Z            5538121        1180401  2022-07-01T00:00:00.000Z  2022-08-01T00:00:00.000Z 
```

### * As Python Package:

```python
>>> from wikistats2csv import Content
>>> Content.pages_to_date(wiki='es', period='all-years', filter='page-type-all', interval='monthly')

## Downloaded `spanish--pages-to-date--page-type-all--all-years--monthly.csv` successfully :-)

** Quick glance at `spanish--pages-to-date--page-type-all--all-years--monthly.csv` file:
                        month  total.non-content  total.content           timeRange.start             timeRange.end
0    2001-01-01T00:00:00.000Z                  0              0  2001-01-01T00:00:00.000Z  2001-02-01T00:00:00.000Z
1    2001-02-01T00:00:00.000Z                  0              0  2001-02-01T00:00:00.000Z  2001-03-01T00:00:00.000Z
..                        ...                ...            ...                       ...                       ...
257  2022-06-01T00:00:00.000Z            3896209        1786321  2022-06-01T00:00:00.000Z  2022-07-01T00:00:00.000Z
258  2022-07-01T00:00:00.000Z            3903963        1792329  2022-07-01T00:00:00.000Z  2022-08-01T00:00:00.000Z 
```

## Supported Features:

### Content Class/Metrics:

| Queries*/Functions**                                      | Periods                                                                 | Filters***                                                                                                                                                                                                                                                                                                                                                                      | Intervals          |
|:---------------------------------------------------------:|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------:|
| absolute-bytes-difference*<br>absolute_bytes_difference** | all-years, <br>one-year, <br>two-years, <br>three-months, <br>one-month | no-filter, <br>page-type-content, <br>page-type-non-content, <br>page-type-all, <br>editor-type-user, <br>editor-type-name-bot, <br>editor-type-anonymous, <br>editor-type-group-bot, <br>editor-type-all                                                                                                                                                                       | daily,<br> monthly |
| edited-pages*<br>edited_pages**                           | all-years, <br>one-year, <br>two-years, <br>three-months, <br>one-month | no-filter, <br>page-type-content, <br>page-type-non-content, <br>page-type-all, <br>editor-type-user, <br>editor-type-name-bot, <br>editor-type-anonymous, <br>editor-type-group-bot, <br>editor-type-all, <br>activity-level-1-to-4-edits, <br>activity-level-5-to-24-edits, <br>activity-level-25-to-99-edits, <br>activity-level-100-or-more-edits,   <br>activity-level-all | daily,<br> monthly |
| net-bytes-difference*<br>net_bytes_difference**           | all-years, <br>one-year, <br>two-years, <br>three-months, <br>one-month | no-filter, <br>page-type-content, <br>page-type-non-content, <br>page-type-all, <br>editor-type-user, <br>editor-type-name-bot, <br>editor-type-anonymous, <br>editor-type-group-bot, <br>editor-type-all                                                                                                                                                                       | daily,<br> monthly |
| pages-to-date*<br>pages_to_date**                         | all-years, <br>one-year, <br>two-years, <br>three-months, <br>one-month | no-filter, <br>page-type-content, <br>page-type-non-content, <br>page-type-all, <br>editor-type-user, <br>editor-type-name-bot, <br>editor-type-anonymous, <br>editor-type-group-bot, <br>editor-type-all                                                                                                                                                                       | daily,<br> monthly |
| total-media-requests*<br>total_media_requests**           | all-years, <br>one-year, <br>two-years, <br>three-months, <br>one-month | no-filter, <br>media-type-image, <br>media-type-video, <br>media-type-audio, <br>media-type-document, <br>media-type-other, <br>media-type-all, <br>agent-type-user, <br>agent-type-spider, <br>agent-type-all                                                                                                                                                                  | daily,<br> monthly |
| top-media-requests*<br>top_media_requests**               | last-month                                                              | no-filter, <br>media-type-image, <br>media-type-video, <br>media-type-audio, <br>media-type-document, <br>media-type-other, <br>media-type-all                                                                                                                                                                                                                                  | daily,<br> monthly |

 <i>* CLI Queries.        ** Py Functions.        *** More complex filters are coming to the new versions.</i>

### Contributing Metrics/Class:

| Queries*/Functions**                                       | Periods                                                                 | Filters***                                                                                                                                                                                                                                                                                                                                                                     | Intervals          |
|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------:|
| editors* **                                                | all-years, <br>one-year, <br>two-years, <br>three-months, <br>one-month | no-filter, <br>page-type-content, <br>page-type-non-content, <br>page-type-all, <br>editor-type-user, <br>editor-type-name-bot, <br>editor-type-anonymous, <br>editor-type-group-bot, <br>editor-type-all, <br>activity-level-1-to-4-edits, <br>activity-level-5-to-24-edits, <br>activity-level-25-to-99-edits, <br>activity-level-100-or-more-edits,  <br>activity-level-all | daily,<br> monthly |
| active-editors*<br>active_editors**                        | all-years, <br>one-year, <br>two-years, <br>three-months, <br>one-month | no-filter, <br>page-type-content, <br>page-type-non-content, <br>page-type-all                                                                                                                                                                                                                                                                                                 | daily,<br> monthly |
| edits* **                                                  | all-years, <br>one-year, <br>two-years, <br>three-months, <br>one-month | no-filter, <br>page-type-content, <br>page-type-non-content, <br>page-type-all, <br>editor-type-user, <br>editor-type-name-bot, <br>editor-type-anonymous, <br>editor-type-group-bot, <br>editor-type-all                                                                                                                                                                      | daily,<br> monthly |
| user-edits*<br>user_edits**                                | all-years, <br>one-year, <br>two-years, <br>three-months, <br>one-month | no-filter, <br>page-type-content, <br>page-type-non-content, <br>page-type-all                                                                                                                                                                                                                                                                                                 | daily,<br> monthly |
| new-pages*<br>new_pages**                                  | all-years, <br>one-year, <br>two-years, <br>three-months, <br>one-month | no-filter, <br>page-type-content, <br>page-type-non-content, <br>page-type-all, <br>editor-type-user, <br>editor-type-name-bot, <br>editor-type-anonymous, <br>editor-type-group-bot, <br>editor-type-all                                                                                                                                                                      | daily,<br> monthly |
| new-registered-users* <br>new_registered_users**           | all-years, <br>one-year, <br>two-years, <br>three-months, <br>one-month | no-filter                                                                                                                                                                                                                                                                                                                                                                      | daily,<br> monthly |
| top-editors* <br>top_editors**                             | last-month                                                              | no-filter, <br>page-type-content, <br>page-type-non-content, <br>page-type-all, <br>editor-type-user, <br>editor-type-name-bot, <br>editor-type-anonymous, <br>editor-type-group-bot, <br>editor-type-all                                                                                                                                                                      | daily,<br> monthly |
| top-edited-pages* <br>top_edited_pages**                   | last-month                                                              | no-filter, <br>page-type-content, <br>page-type-non-content, <br>page-type-all, <br>editor-type-user, <br>editor-type-name-bot, <br>editor-type-anonymous, <br>editor-type-group-bot, <br>editor-type-all                                                                                                                                                                      | daily,<br> monthly |
| active-editors-by-country* <br>active_editors_by_country** | last-month                                                              | activity-level-5-to-99-edits, <br>activity-level-100-or-more-edits                                                                                                                                                                                                                                                                                                             | daily,<br> monthly |

 <i>* CLI Queries.        ** Py Functions.        *** More complex filters are coming to the new versions.</i>

### Reading Metrics/Class:

| Queries*/Functions**                              | Periods                                                                 | Filters***                                                                                                                                                                                                             | Intervals          |
|:-------------------------------------------------:|:-----------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------:|
| total-page-views*<br>total_page_views**           | all-years, <br>one-year, <br>two-years, <br>three-months, <br>one-month | no-filter, <br/>access-method-desktop,<br/> access-method-mobile-app,<br/>access-method-mobile-web, <br/>access-method-all,<br/>agent-type-user, <br/>agent-type-spider, <br/>agent-type-automated,<br/>agent-type-all | daily,<br> monthly |
| legacy-page-views*<br>legacy_page_views**         | all-years, <br>one-year, <br>two-years, <br>three-months, <br>one-month | no-filter, <br/>access-site-mobile-site, <br/>access-site-desktop-site, <br/>access-site-all                                                                                                                           | daily,<br> monthly |
| page-views-by-country*<br>page_views_by_country** | last-month                                                              | no-filter, <br/>access-method-desktop,<br/> access-method-mobile-app,<br/>access-method-mobile-web, <br/>access-method-all                                                                                             | daily,<br> monthly |
| unique-devices* <br>unique_devices**              | all-years, <br>one-year, <br>two-years, <br>three-months, <br>one-month | no-filter, <br/>access-site-mobile-site, <br/>access-site-desktop-site, <br/>access-site-all                                                                                                                           | daily,<br> monthly |
| top-viewed-articles*<br>top_viewed_articles**     | last-month                                                              | no-filter, <br/>access-method-desktop,<br/> access-method-mobile-app,<br/>access-method-mobile-web, <br/>access-method-all                                                                                             | daily,<br> monthly |

<i> * CLI Queries.        ** Py Functions.        *** More complex filters are coming to the new versions.</i>

## Extra Features:

### List All Wikipedia Languages with its Codes:

#### * As CLI:

To return the full list of all Wikipedia's supported languages with their codes, try one of these commands:

```bash
$ wikistats2csv -lw
# OR
$ wikistats2csv --list-wikis
```

#### * As Python Package:

```python
from wikistats2csv import Helper
Helper.get_Wikis_Codes()
```
