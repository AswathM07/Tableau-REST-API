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
server.auth.sign_in(tableau_auth)
all_workbooks_items, pagination_item = server.workbooks.get()
  # print names of first 100 workbooks
n=input("Enter the Workbook Name") 
for i in all_workbooks_items:
    if i.name==n:
        k=i.id
        break
     
file_path = server.workbooks.download(k)
print("\nDownloaded the file to {0}.".format(file_path))