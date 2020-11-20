#tableau workbook download
import tableauserverclient as TSC
un=input("Enter usrer name ")
ps=input("Enter password ")
sn=input("Enter site name ")
tableau_auth = TSC.TableauAuth(un, ps, sn)
# or for a personal access token
# tableau_auth = TSC.PersonalAccessTokenAuth('TOKEN_NAME', 'TOKEN_VALUE', 'SITENAME')
#'https://10ax.online.tableau.com' this is for online 
server = TSC.Server('https://10ax.online.tableau.com')

pid=input("Enter project id") #Enter project Id to uplode your Workbook
with server.auth.sign_in(tableau_auth):
  all_workbooks_items, pagination_item = server.workbooks.get()
  # print names of first 100 workbooks
  print([workbook.name for workbook in all_workbooks_items])
  print([workbook.id for workbook in all_workbooks_items])
