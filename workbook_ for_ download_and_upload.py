import tableauserverclient as TSC
un=input("Enter usrer name ")
ps=input("Enter password ")
sn=input("Enter site name ")
tableau_auth = TSC.TableauAuth(un, ps, sn)
# or for a personal access token
# tableau_auth = TSC.PersonalAccessTokenAuth('TOKEN_NAME', 'TOKEN_VALUE', 'SITENAME')
server = TSC.Server('https://10ax.online.tableau.com')
server.auth.sign_in(tableau_auth)
pid=input("Enter project id") #Enter project Id to uplode your Workbook
id=input("Enter workbook id") #Enter Workbook Id to downlode 
file_path = server.workbooks.download(id)
with server.auth.sign_in(tableau_auth):
   # create a workbook item
   wb_item = TSC.WorkbookItem(name=server.workbooks.get_by_id(id).name, project_id=pid)
   # call the publish method with the workbook item
   wb_item = server.workbooks.publish(wb_item,file_path,'CreateNew')
