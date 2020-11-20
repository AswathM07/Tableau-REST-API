#tableau workbook download
#import tableauserverclient as TSC
#un=input("Enter usrer name ")
#ps=input("Enter password ")
#sn=input("Enter site name ")
#tableau_auth = TSC.TableauAuth(un, ps, sn)
# or for a personal access token
# tableau_auth = TSC.PersonalAccessTokenAuth('TOKEN_NAME', 'TOKEN_VALUE', 'SITENAME')
#'https://10ax.online.tableau.com' this is for online 
#server = TSC.Server('https://10ax.online.tableau.com')
#server.auth.sign_in(tableau_auth)
#server.version='3.9'
#query="""{
#  workbooks(filter:{name:"Workbook_name",projectName:"Project_name"}){
#   id
#  }
#}"""
#resp= server.metadata.query(query)
#datasources= resp['data']
#datasources
#id=input("Enter workbook id") #Enter Workbook Id to download 
#file_path = server.workbooks.download(datasources)
#print("\nDownloaded the file to {0}.".format(file_path))