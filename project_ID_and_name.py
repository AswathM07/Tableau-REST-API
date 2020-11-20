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
#script to get project name and id 
with server.auth.sign_in(tableau_auth): 
        # get all projects on site
        all_project_items, pagination_item = server.projects.get()
        #project name
        print([proj.name for proj in all_project_items])
        #project ID
        print([proj.id for proj in all_project_items])