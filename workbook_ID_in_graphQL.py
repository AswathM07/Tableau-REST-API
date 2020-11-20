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
server.version='3.9'
query="""{
  workbooks(filter:{name:"wb",projectName:"pn"}){
    id
  }
}"""
temp_0=sub("pn", Project_Name, query) 
temp_1=sub("wb", name, query)
resp= server.metadata.query(query)
datasources= resp['data']
datasources
print(datasources)
